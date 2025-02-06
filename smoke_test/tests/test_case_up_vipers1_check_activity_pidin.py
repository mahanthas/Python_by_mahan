# Copyright (C) 2022 Robert Bosch GmbH.
# The reproduction, distribution and utilization of this file as
# well as the communication of its contents to others without
# express authorization is prohibited. Offenders will be held
# liable for the payment of damages. All rights reserved in the
# event of the grant of a patent, utility model or design.

from pathlib import Path

import pytest


@pytest.mark.common
def test_case_up_viper1_activity_check_pidin(call_ttl_macro):
    """
    - Test Case Name - test_case_up_viper1_activity_check_pidin
    - Description - To read activities running from the Flashed SW in the ECU
    - Test case steps - ensure the ECU is up
                        - using Terraterm send [pidin -f n]
    - Expected Result - activities in the log are checked against the project_activity_list
                        all the activities must be found in the log
    """

    test_case_ttl_log = pytest.vipers1_logs_path.joinpath("pidin_f_n.log")

    project_activity_list = pytest.ecu_config["vipers1_activity_list"]

    ecu_running_activity_list = []
    try:
        with open(test_case_ttl_log, "r") as log_read:
            for line in log_read.readlines():
                ecu_running_activity_list.append(line.strip())

    except Exception as exc:
        pytest.logger.error(f"Could not load activity from TTL log {test_case_ttl_log}!")
        raise exc

    pytest.logger.info("project activity list:" + str(project_activity_list))
    pytest.logger.info("ECU activity list:" + str(ecu_running_activity_list))
    pytest.logger.info(
        "Project activities running on the ECU:"
        + str(set(project_activity_list).intersection(set(ecu_running_activity_list)))
    )
    pytest.logger.info(
        "Project activities not running on the ECU:"
        + str(set(project_activity_list).difference(set(ecu_running_activity_list)))
    )

    assert set(project_activity_list).issubset(set(ecu_running_activity_list))
