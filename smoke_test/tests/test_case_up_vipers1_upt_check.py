# Copyright (C) 2022 Robert Bosch GmbH.
# The reproduction, distribution and utilization of this file as
# well as the communication of its contents to others without
# express authorization is prohibited. Offenders will be held
# liable for the payment of damages. All rights reserved in the
# event of the grant of a patent, utility model or design.

import pytest

"""
test cases for Ford Dat3 USS Parking SW
"""
"""
    - Below test cases does the same functionality
    - Description - To check UPT(up-time) and ENT(end-time) for the Vipers1 process
    - Test case steps - parsing the processed logs and extracting the UPT and ENT
    - Expected Result - To log the UPT and ENT for every ViperS1 process
"""


@pytest.mark.common
def test_case_up_vipers1_upt_check(get_upt_from_logs):
    # List of log files
    log_files = ["log_rvpsvc.txt", "log_adasvisuservice.txt", "log_adascomp.txt"]

    for log_file in log_files:
        test_case_ttl_log = pytest.vipers1_logs_path.joinpath(log_file)
        get_UPT_from_logs = get_upt_from_logs(test_case_ttl_log)

        # Log UPT
        pytest.logger.info("UPT for %s:\n%s \n ", log_file, get_UPT_from_logs)
