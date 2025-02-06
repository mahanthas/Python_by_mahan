# Copyright (C) 2022 Robert Bosch GmbH.
# The reproduction, distribution and utilization of this file as
# well as the communication of its contents to others without
# express authorization is prohibited. Offenders will be held
# liable for the payment of damages. All rights reserved in the
# event of the grant of a patent, utility model or design.
from pathlib import Path

import pytest
from toliman_flashing.deployer import rename_startup_script, revert_startup_script
from toliman_flashing.ecu_check import check_ecu_availibility_per_ping
from toliman_flashing.sftp_client import (
    sftp_get_all_files_from_dir,
    sftp_put_all_files_of_dir,
)
from toliman_flashing.ssh_client import ssh_execute

scripts_path = Path.joinpath(
    Path(__file__).resolve().parent, "resource", "vipers1_scripts", "stream_check"
).absolute()
logs_path = pytest.vipers1_logs_path
logs_path.mkdir(parents=True, exist_ok=True)
remote_path = pytest.ecu_config.get("vipers1_script_path")
vipers1_scripts = ["start_vision-p1.sh", "start_vision-p2.sh"]

"""
    test cases for Ford Dat3 USS Parking SW
"""


@pytest.mark.common
@pytest.mark.order(2)
def test_case_vipers1_perf_measurement(call_ttl_macro):
    """
    - Test Case Name - test_case_vipers1_perf_measurement
    - Description - To check Performance of the Vipers1 MCU2_0 and DDR load
    - Test case steps - ensure the ECU is up
                      - using parsing of the csv file will get the values
    - Expected Result - MCU2_0 LOAD [%] and DDR TOTAL BW AVG [MB/s] values are logged and asserted.
    """
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

    call_ttl_macro("perf.TTL")

    sftp_get_all_files_from_dir(
        logs_path,
        remote_path,
        pytest.ecu_config.get("user_name"),
        pytest.ecu_config.get("ip_address"),
        pytest.ecu_config.get("ssh_port"),
        password="",
        log_file_name="get_logs_from_ecu.log",
        include_file_list="measurement.csv",
    )

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
