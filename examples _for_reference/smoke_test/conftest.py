import csv
import re
from pathlib import Path
from typing import List

import pytest
import yaml
from toliman_flashing.config_merger import get_host_config
from toliman_flashing.ea_power_supply_controller import EAPowerSupplyControl
from toliman_flashing.logger import Logger
from toliman_flashing.teraterm_macro_runner import run_ttl_macros
from toliman_flashing.windows_task_helper import kill_tasks


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "standalone_test: Run only in target_test pipeline"
    )  # for future usage
    config.addinivalue_line("markers", "smoketest: Run only in smoketest pipeline")
    config.addinivalue_line("markers", "common: Run on both smoke and target pipeline ")


def pytest_sessionstart(session):
    pytest.logs_subdir = "smoke_tests"
    logger = Logger.get_logger("session_start.log", sub_dir=pytest.logs_subdir, create_new=True)
    pytest.logs_path = Path.joinpath(Path.cwd(), "logs", pytest.logs_subdir)
    pytest.TTL_logs_path = Path.joinpath(pytest.logs_path, "TTL_logs")
    pytest.vipers1_logs_path = Path.joinpath(pytest.logs_path, "vipers1_logs")
    pytest.svs_dump_path = Path.joinpath(pytest.logs_path, "svs_dump")
    pytest.host_config = get_host_config(
        host_config_dir=Path.joinpath(Path(__file__).resolve().parent, "machine_configs")
    )
    pytest.power_config = pytest.host_config["PowerSupply"]
    pytest.tools_config = pytest.host_config["Tools"]
    pytest.ecu_config = pytest.host_config["ECU"]

    try:
        tasks_to_kill = ["plink", "putty", "ttermpro"]
        kill_tasks(tasks_to_kill)
        pytest.power_supply = EAPowerSupplyControl(
            pytest.power_config["com_port"],
            int(pytest.power_config["baud_rate"]),
            int(pytest.power_config["stop_bits"]),
            int(pytest.power_config["byte_size"]),
            pytest.power_config["parity"],
        )
    except Exception as ex:
        logger.exception(ex)
        raise ex


@pytest.fixture(autouse=True)
def run_around_tests(request):
    # Code that will run before your test, for example:
    pytest.logger = Logger.get_logger(
        f"{request.node.name}.log", sub_dir=pytest.logs_subdir, create_new=True
    )
    pytest.logger.info("Running %s", request.node.name)
    ecu_channel = pytest.power_config.get("ecu_channel")
    try:
        ecu_voltage = pytest.power_supply.get_voltage(ecu_channel)
        if ecu_voltage > 13 and ecu_voltage < 14.2:
            pytest.logger.info("ECU running. Power supply Voltage: %s", str(ecu_voltage))
        elif ecu_voltage > 14.2:
            pytest.fail(f"ECU over voltage! Power supply Voltage above 14.2V: {ecu_voltage}")
        else:
            pytest.fail(f"ECU down! Power supply Voltage below 13V: {ecu_voltage}")
        # A test function will be run at this point
        yield
    except Exception as ex:
        pytest.logger.exception(ex)
    # Code that will run after your test, for example:
    pytest.logger.handlers.clear()


@pytest.fixture
def call_ttl_macro():
    def core(ttl_file):
        pytest.logger.info("Running: %s", ttl_file)

        return run_ttl_macros(
            tterm_exe=pytest.tools_config.get("teraterm_exe"),
            tterm_macro_full_path=Path.joinpath(
                Path(__file__).resolve().parent, "tests", "ttl_macros", ttl_file
            ),
            com_port=pytest.ecu_config.get("com_port"),
            baud_rate=pytest.ecu_config.get("baud_rate"),
            log_subdir=pytest.logs_subdir,
        )

    return core


@pytest.fixture
def get_config_activity():
    """Function to get the activities from the activities configured in AOS model activity graph"""
    # path of the activity graph yaml,
    # aos_deployment/ford_dat3/RbpFordDat3.activity_graph.yaml
    config_activity = Path.joinpath(
        Path(__file__).resolve().parent.parent.parent.parent,
        "aos_deployment",
        "ford_dat3",
        "RbpFordDat3.activity_graph.yaml",
    )

    with open(config_activity, "r") as stream:
        activity_graph = yaml.safe_load(stream)

    activity_list = [
        conf_activity.replace(".", "_") for conf_activity in activity_graph.get("imports")
    ]

    return activity_list


@pytest.fixture
def check_mark():
    def core(request, input_var: str, required: bool = False) -> str:
        for mark in request.node.iter_markers(input_var):
            if mark.args:
                if input_var is not None:
                    pytest.fail("Only one {input_var} can be mentioned in marks")
                input_var = mark.args[0]
        if required and input_var is None:
            pytest.fail("{input_var} is a required mark")
        return input_var

    return core


@pytest.fixture
def get_activities_from_TTL_log():
    def core(test_case_ttl_log, splitter, dont_filter=False) -> List:
        """Function to get the activities from the activities from the log file"""
        log_list = []

        with open(test_case_ttl_log, "r") as log_read:
            for line in log_read:
                log_list.append(line.split(splitter)[-1].strip())

        if not dont_filter:
            ecu_activity_list = [
                entry for entry in log_list if "_activity" in entry or "_gateway" in entry
            ]
        else:
            ecu_activity_list = log_list
        return ecu_activity_list

    return core


@pytest.fixture
def get_upt_from_logs():
    """function to get the UPT from the generated logs"""

    def core(test_case_ttl_log) -> str:
        upt_info = []
        try:
            with open(test_case_ttl_log, "r") as log_file:
                target_words = ["UPT", "ENT"]
                for line in log_file:
                    if any(word in line for word in target_words):
                        upt_info.append(line.strip())

        except Exception:
            pytest.fail(f"Could not load the log from Generated Logs folder {test_case_ttl_log}!")
        return "\n".join(upt_info)

    return core


@pytest.fixture
def get_perf_from_csv():
    """function to get the perf measurement from the csv file"""

    def core(test_case_ttl_log, keywords) -> str:
        perf_info = []
        try:
            with open(test_case_ttl_log) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                line_count = 0
                header = None
                keyword_indices = []

                for row in csv_reader:
                    if line_count == 0:
                        header = row
                        for keyword in keywords:
                            if keyword not in header:
                                pytest.fail(
                                    f"Keyword '{keyword}' not found in the CSV file header!"
                                )
                                return "Keyword not found in CSV file."
                            keyword_indices.append(header.index(keyword))
                        line_count += 1
                    else:
                        row_info = []
                        for index in keyword_indices[0:]:
                            row_info.append(f"{header[index]} is {row[index]}")
                        perf_info.append("\t" + ", ".join(row_info))
                        line_count += 1

                    if line_count >= 40:  # Stop after 40 rows
                        break

                pytest.logger.info(f"Processed {line_count} lines. ")
        except Exception as exc:
            pytest.fail(f"Could not load the CSV file from the logs folder {test_case_ttl_log}!")
            raise exc
        return "\n".join(perf_info)

    return core


@pytest.fixture
def get_unexpected_errors():
    def core(log_file: Path, yml_file: Path) -> list:
        unexpected_errors = []

        # Load expected errors and their max counts from YAML file
        with yml_file.open("r") as yaml_file:
            expected_errors_config = yaml.safe_load(yaml_file)["expected_errors"]

        # Initialize error occurrence tracking per pattern
        error_counts = {
            entry["pattern"]: {key: 0 for key in entry if key.endswith("_count")}
            for entry in expected_errors_config
        }

        # Parse logs and check against each pattern and count limit
        with log_file.open("r") as file:
            for line in file:
                matched_expected_error = False
                for error_config in expected_errors_config:
                    pattern = error_config["pattern"]

                    # Determine the count key specific to the log file
                    log_file_key = f"{log_file.stem.replace('log_', '')}_count"
                    max_count = error_config.get(log_file_key, 0)

                    # Ensure the pattern and log file key exist in `error_counts`
                    if pattern not in error_counts:
                        error_counts[pattern] = {}
                    if log_file_key not in error_counts[pattern]:
                        error_counts[pattern][log_file_key] = 0

                    # Increment count if pattern is found in the line
                    if re.search(pattern, line):
                        error_counts[pattern][log_file_key] += 1

                        # Directly log an error if count exceeds the max allowed count
                        if error_counts[pattern][log_file_key] > max_count:
                            error_message = (
                                f"Exceeded max occurrences for {pattern} -> in {log_file.stem}. "
                                f"Allowed: {max_count}, Actual: {error_counts[pattern][log_file_key]}"
                            )
                            unexpected_errors.append(error_message)
                        else:
                            pytest.logger.info(
                                f"Matched expected pattern: {pattern}, Occurrences: {error_counts[pattern][log_file_key]}"
                            )
                        matched_expected_error = True
                        break  # Skip remaining patterns if matched

                # If no expected error matched and "VX_ZONE_ERROR" is present, log as an unexpected error
                if not matched_expected_error and "VX_ZONE_ERROR" in line:
                    error_message = f"Unexpected VX_ZONE_ERROR in {log_file.stem}: {line.strip()}"
                    unexpected_errors.append(error_message)

        return unexpected_errors

    return core


@pytest.fixture
def get_perf_stats():
    def core(log_file_path: Path, yaml_file_path: Path) -> list:
        # Load the YAML file
        with open(yaml_file_path, "r") as yaml_file:
            graphs_info = yaml.safe_load(yaml_file)

        # Use a dictionary to store the latest FPS result for each graph
        graphs = {graph["name"]: graph for graph in graphs_info["graphs"]}
        fps_results = []

        # Read the perf log file line by line
        with open(log_file_path, "r") as log_file:
            log_lines = log_file.readlines()

            # Search for the graph in perf log and record FPS value
            for line in log_lines:
                for graph_name, graph_config in graphs.items():
                    if graph_name in line:
                        # Extract FPS value from the line
                        fps_match = re.search(r"FPS:(\d+)", line)
                        if fps_match:
                            fps_value = int(fps_match.group(1))
                            min_fps = graph_config["min_fps"]
                            max_fps = graph_config["max_fps"]
                            # Determine if FPS is within range
                            if min_fps <= fps_value <= max_fps:
                                message = "PASSED."
                            else:
                                message = f"FPS {fps_value} OUT OF RANGE ({min_fps}-{max_fps})"
                            fps_results.append((graph_name, fps_value, message))
        # Returns results as a list
        return fps_results

    return core


@pytest.fixture
def get_resource_limit():
    """Function to get the limit values from the resource_limits.yml"""

    # path of the resource_limits.yml,
    # tools/cus/smoke_test/tests/resource_limits.yml
    def core(resource):
        resource_limit_file = Path.joinpath(
            Path(__file__).resolve().parent, "tests", "resource_limits.yml"
        ).resolve()

        with open(resource_limit_file, "r") as stream:
            resource_limit = yaml.safe_load(stream)

        keyword_val = resource_limit.get(resource)

        return keyword_val

    return core
