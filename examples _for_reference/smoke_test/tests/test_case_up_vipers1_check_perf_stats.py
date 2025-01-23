# Copyright (C) 2022 Robert Bosch GmbH.
# The reproduction, distribution and utilization of this file as
# well as the communication of its contents to others without
# express authorization is prohibited. Offenders will be held
# liable for the payment of damages. All rights reserved in the
# event of the grant of a patent, utility model or design.
from pathlib import Path

import pytest

yaml_file = Path(__file__).parent.joinpath("resource", "perf_stats.yml").absolute()
perf_log = pytest.TTL_logs_path.joinpath("perf_TTL.log")
perf_csv = pytest.vipers1_logs_path.joinpath("measurement.csv")

keywords_list = [
    "Timestamp [us]",
    "A72_0 LOAD [%]",
    "A72_1 LOAD [%]",
    " c7x_1 LOAD [%]",
    "mcu2_0 LOAD [%]",
    "mcu2_1 LOAD [%]",
    "DDD AVG READ BW [MB/s]",
    "DDR AVG WRITE BW [MB/s]",
]

"""
    test cases for Ford Dat3 USS Parking SW
"""


@pytest.mark.common
@pytest.mark.order(5)
def test_case_vipers1_check_perf_stats(get_perf_stats, get_perf_from_csv):
    print(f"content of perf_log is : {perf_log} ")
    failures = []

    results = get_perf_stats(perf_log, yaml_file)

    # Assert FPS values are in range or not
    graph_counter = 0
    for graph_name, fps_value, message in results:
        pytest.logger.info(f"{graph_name}: FPS {fps_value} - {message}")
        graph_counter += 1

        if graph_counter % 5 == 0:
            pytest.logger.info("")
        if "OUT OF RANGE" in message:
            failures.append(f"Test failed for {graph_name}: {message}")

    get_perf_from_csv_file = get_perf_from_csv(perf_csv, keywords_list)

    pytest.logger.info(str(get_perf_from_csv_file))

    # Process the returned string to extract the values and perform assertions
    perf_entries = get_perf_from_csv_file.split("\n")
    for entry in perf_entries:
        if (
            "mcu2_0 LOAD [%]" in entry
            and "mcu2_1 LOAD [%]" in entry
            and "DDR TOTAL BW AVG [MB/s]" in entry
        ):
            parts = entry.split(", ")
            mcu2_0_value = float(parts[1].split(" is ")[1])
            mcu2_1_value = float(parts[2].split(" is ")[1])
            ddr_total_bw_avg_value = float(parts[3].split(" is ")[1])

            # Assert the values do not exceed the maximum limits
            assert mcu2_0_value <= 80, f"mcu2_0 LOAD [%] exceeded 80%: {mcu2_0_value}"
            assert mcu2_1_value <= 80, f"mcu2_1 LOAD [%] exceeded 80%: {mcu2_1_value}"
            assert (
                ddr_total_bw_avg_value <= 11000
            ), f"DDR TOTAL BW AVG [MB/s] exceeded 11000: {ddr_total_bw_avg_value}"

    pytest.logger.info(" \n Performance measurements are within expected limits.  \n")

    if failures:
        pytest.fail("\n".join(failures))
