import os
import socket
import time
from pathlib import Path
from subprocess import run

import pytest
from toliman_flashing.deployer import rename_startup_script, revert_startup_script
from toliman_flashing.ecu_check import check_ecu_availibility_per_ping
from toliman_flashing.sftp_client import (
    sftp_get_all_files_from_dir,
    sftp_put_all_files_of_dir,
)
from toliman_flashing.ssh_client import ssh_execute

svs_dump_path = pytest.svs_dump_path
svs_dump_path.mkdir(parents=True, exist_ok=True)
scripts_path = Path.joinpath(
    Path(__file__).resolve().parent, "resource", "vipers1_scripts", "stream_check"
).absolute()
remote_path = pytest.ecu_config.get("vipers1_script_path")
tmp_path = pytest.ecu_config.get("tmp_path")
cam_ip = pytest.ecu_config.get("ip_address")
cam_port = pytest.ecu_config.get("svs_port")
svs_dump_pix = pytest.ecu_config.get("svs_dumps")
vipers1_scripts = ["start_vision-p1.sh", "start_vision-p2.sh"]


def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    print("Connection closed.")
    s.close()


def dump(testname="null"):
    netcat(cam_ip, cam_port, "dump pix")
    svs_test_dump = Path.joinpath(pytest.svs_dump_path, testname)
    svs_test_dump.mkdir(parents=True, exist_ok=True)

    ssh_execute(
        command=f"ls -lha {tmp_path}",
        server=pytest.ecu_config.get("ip_address"),
        port=pytest.ecu_config.get("ssh_port"),
        username=pytest.ecu_config.get("user_name"),
        password="",
    )
    try:
        sftp_get_all_files_from_dir(
            svs_test_dump,
            tmp_path,
            pytest.ecu_config.get("user_name"),
            pytest.ecu_config.get("ip_address"),
            pytest.ecu_config.get("ssh_port"),
            password="",
            log_file_name="get_dumps_from_ecu.log",
            include_file_list=svs_dump_pix,
        )
    except OverflowError as e:
        pytest.logger.info(f"Encounterd an OverflowError: {e}")

    for file in svs_dump_pix:
        ssh_execute(
            command=f"rm -f {tmp_path}/{file}",
            server=pytest.ecu_config.get("ip_address"),
            port=pytest.ecu_config.get("ssh_port"),
            username=pytest.ecu_config.get("user_name"),
            password="",
        )

    for file in svs_dump_pix:
        input_file = svs_test_dump.joinpath(file)
        if input_file.exists():
            output_file = svs_test_dump.joinpath(f"output_{file.split('_')[1].split('.')[0]}.png")
            run(
                [
                    "python3",
                    "./libs/cc_ovxpipeline_ford/scripts/visualize/visualize_YUV422_UYVY_GPU.py",
                    str(input_file),
                    str(output_file),
                    "1920",
                    "1248",
                ]
            )
            file_size = os.path.getsize(output_file)
            print(f"Parsed Output File size: {file_size}")
            if file_size < 10000:
                pytest.fail(
                    f"The parsed output is either black output or corrupted, as the file size is {file_size} -> below threshold"
                )
            pytest.logger.info(f"Successfully parsed {input_file} using visualize_YUV422_UYVY.py")
        else:
            pytest.fail(f"File {input_file} not found in svs_test_dump directory")


def set_off_all_streams():
    pytest.logger.info("Setting Off all streams...")
    netcat(cam_ip, cam_port, "ssi stream1 0")
    netcat(cam_ip, cam_port, "ssi stream2 0")
    netcat(cam_ip, cam_port, "ssi stream3 0")


@pytest.mark.common
@pytest.mark.order(3)
def test_case_vipers1_svs_dump(call_ttl_macro):
    check_ecu_availibility_per_ping(pytest.ecu_config, pytest.power_config)

    for script in vipers1_scripts:
        script_path = remote_path + script
        rename_startup_script(pytest.ecu_config, script_path)

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
        command=f"chmod 777 {remote_path}/*",
        username=pytest.ecu_config.get("user_name"),
        server=pytest.ecu_config.get("ip_address"),
        port=pytest.ecu_config.get("ssh_port"),
        password="",
    )
    call_ttl_macro("run_sync.TTL")

    pytest.power_supply.toggle(
        pytest.power_config.get("ecu_channel"), pytest.power_config.get("channel_1_voltage")
    )

    try:
        pytest.logger.info("Test_1: Starting 360 view ,Rearview and chmsl view")
        set_off_all_streams()
        netcat(cam_ip, cam_port, 'view show "RearNormalViewRVCStream"')
        netcat(cam_ip, cam_port, 'view show "ChmslView"')
        netcat(cam_ip, cam_port, 'view show "360 Normal View"')
        call_ttl_macro("run_sync.TTL")
        dump("test_1")
        pytest.logger.info("Test_1: Dumped 360 view and Rear View and chmsl view ")

        pytest.logger.info("Test_2: Starting 360 view ,Rearview and left turn view and chmsl view")
        set_off_all_streams()
        netcat(cam_ip, cam_port, 'view show "RearNormalView"')
        netcat(cam_ip, cam_port, 'view show "ChmslView"')
        netcat(cam_ip, cam_port, 'view show "360 Normal View"')
        netcat(cam_ip, cam_port, 'view show "LeftTurnSignalView"')
        call_ttl_macro("run_sync.TTL")
        dump("test_2")
        pytest.logger.info(
            "Test_2: Dumped 360 view and Rear View and left turn view and chmsl view"
        )

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

        check_ecu_availibility_per_ping(pytest.ecu_config, pytest.power_config)
