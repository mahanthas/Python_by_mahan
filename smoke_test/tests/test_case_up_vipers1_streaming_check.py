# Copyright (C) 2022 Robert Bosch GmbH.
# The reproduction, distribution and utilization of this file as
# well as the communication of its contents to others without
# express authorization is prohibited. Offenders will be held
# liable for the payment of damages. All rights reserved in the
# event of the grant of a patent, utility model or design.

import time
from pathlib import Path
from subprocess import PIPE, run

import pytest
from toliman_flashing.deployer import rename_startup_script, revert_startup_script
from toliman_flashing.ecu_check import check_ecu_availibility_per_ping
from toliman_flashing.sftp_client import sftp_put_all_files_of_dir
from toliman_flashing.ssh_client import ssh_execute

local_FG_tool_dir = Path(pytest.tools_config.get("FG_tool"))
FG_proFrame_exes_path = Path.joinpath(
    local_FG_tool_dir, "proFRAME", "src", "win64", "x64", "Release"
)
FG_proFrame_ini_path = Path.joinpath(
    local_FG_tool_dir, "SXPF_V3_Minimal_Config_Quad_TI9702_Ver2.ini"
)
FG_proFrame_dvreg_path = Path.joinpath(
    local_FG_tool_dir, "Ford_Toliman_TI_SerDes_FPD4_20240125_sync_static_values.dvreg"
)
remote_path = pytest.ecu_config.get("vipers1_script_path")
scripts_path = Path.joinpath(
    Path(__file__).resolve().parent, "resource", "vipers1_scripts", "stream_check"
).absolute()
vipers1_scripts = ["start_vision-p1.sh", "start_vision-p2.sh"]


# intialize Frame grabber
def fg_intializing():
    pytest.logger.info("Initializing FG")
    run(
        f"{FG_proFrame_exes_path}/sxpf-init-sequence.exe /dev/sxpf0 -port 0 -ini {FG_proFrame_ini_path} --execute 0",
        timeout=5,
    )
    time.sleep(3)
    run(f"{FG_proFrame_exes_path}/rb-dvreg.exe  0 0 {FG_proFrame_dvreg_path}", timeout=5)
    time.sleep(3)


# check connection between toliman and frame grabber
def check_connection_status():
    pytest.logger.info("Checking FG connection to ECU")
    tmp = run(
        f"{FG_proFrame_exes_path}/sxpfi2c.exe 0 0 0x7a 1 0x4d", stdout=PIPE, timeout=60
    ).stdout.decode("utf-8")
    pytest.logger.info("connection status is : %s", tmp)
    x = tmp.split()
    status = 0
    for i in x:
        if i.isnumeric():
            status = int(i)
            status = status % 10
    if status != 3:
        connection_status = 0
    else:
        connection_status = 1
    return connection_status


@pytest.mark.smoketest
@pytest.mark.xfail
def test_case_up_vipers1_streaming_check(call_ttl_macro):
    """
    - Test Case Name - test_case_up_vipers1_streaming_check
    - Description - To check video streaming output
    - Test case steps - Start Frame Grabber by using ProFrame exe, send screen shot function selection
    - Expected Result - screen shots of all views are saved in Screenshots folder
    """

    video_out_screenshots = Path.joinpath(pytest.logs_path, "video_out_screenshots")
    video_out_screenshots.mkdir(parents=True, exist_ok=True)

    for script in vipers1_scripts:
        script_path = remote_path + script
        rename_startup_script(pytest.ecu_config, script_path)

    check_ecu_availibility_per_ping(pytest.ecu_config, pytest.power_config)
    sftp_put_all_files_of_dir(
        scripts_path,
        remote_path,
        pytest.ecu_config.get("user_name"),
        pytest.ecu_config.get("ip_address"),
        pytest.ecu_config.get("ssh_port"),
        password="",
        log_file_name="startup_file_copy.log",
        exclude_file_list=[],
    )
    ssh_execute(
        command=f"chmod +x {remote_path}/*",
        username=pytest.ecu_config.get("user_name"),
        server=pytest.ecu_config.get("ip_address"),
        port=pytest.ecu_config.get("ssh_port"),
        password="",
    )
    call_ttl_macro("run_sync.TTL")

    pytest.power_supply.toggle(
        pytest.power_config.get("ecu_channel"), pytest.power_config.get("channel_1_voltage")
    )

    # re-intialize Frame grabber incase of connection failure
    for loop_x in range(3):
        fg_intializing()
        status = check_connection_status()
        pytest.logger.info(
            "Connection between toliman and frame grabber failed for %s try!", loop_x
        )
        if status == 1:
            pytest.logger.info("connection status is OK")
            break

    try:
        assert status == 1, "no connection between toliman and frame grabber!"

        image_path = f"{video_out_screenshots}/Main_View"
        run(
            f"{FG_proFrame_exes_path}/sxpfapp.exe --card 0 --channel 3 -d 0x1E -l8 -O1 -n{image_path} --output-format png -T1",
            timeout=5,
        )
        time.sleep(3)
        image_path = f"{video_out_screenshots}/360_View"
        run(
            f"{FG_proFrame_exes_path}/sxpfapp.exe --card 0 --channel 3 -d 0x5E -l8 -O1 -n{image_path} --output-format png -T1",
            timeout=5,
        )
        time.sleep(3)
        image_path = f"{video_out_screenshots}/supplementary_View"
        run(
            f"{FG_proFrame_exes_path}/sxpfapp.exe --card 0 --channel 3 -d 0x9E -l8 -O1 -n{image_path} --output-format png -T1",
            timeout=5,
        )
        time.sleep(3)
        image_path = f"{video_out_screenshots}/virtual_channel_3"
        run(
            f"{FG_proFrame_exes_path}/sxpfapp.exe --card 0 --channel 3 -d 0xDE -l8 -O1 -n{image_path} --output-format png -T1",
            timeout=5,
        )
        time.sleep(2)

    finally:
        for file in vipers1_scripts:
            ssh_execute(
                command=f"rm -f {remote_path}/{file}",
                server=pytest.ecu_config.get("ip_address"),
                port=pytest.ecu_config.get("ssh_port"),
                username=pytest.ecu_config.get("user_name"),
                password="",
            )
        for script in vipers1_scripts:
            script_path = remote_path + script
            revert_startup_script(pytest.ecu_config, script_path)
