from pathlib import Path

import pytest

# Paths to the logs directory
logs_path = pytest.vipers1_logs_path
logs_path.mkdir(parents=True, exist_ok=True)

# Paths to store the processed logs
stderr_output_dir = Path.joinpath(logs_path, "stderr")
stderr_output_dir.mkdir(parents=True, exist_ok=True)

yaml_file = Path(__file__).parent.joinpath("resource", "expected_errors.yml").absolute()

log_filenames = [
    "log_adasvisuservice.txt",
    "log_adascomp.txt",
    "log_rvpsvc.txt",
    "log_rvpchmsl.txt",
]


@pytest.mark.common
@pytest.mark.order(4)
def test_case_up_vipers1_logs_check(get_unexpected_errors):
    all_unexpected_errors = []

    # Separate and process logs
    for log_file_name in log_filenames:
        log_file_path = logs_path.joinpath(log_file_name)
        if log_file_path.exists():
            stderr_lines = []
            with log_file_path.open("r", encoding="utf-8", errors="ignore") as file:
                for line in file:
                    if "VX_ZONE_ERROR" in line:
                        stderr_lines.append(line)

            # Write stderr lines to a file in the stderr directory
            if stderr_lines:
                stderr_output_file = stderr_output_dir.joinpath(log_file_path.name)
                stderr_output_file.write_text("".join(stderr_lines))
                pytest.logger.info(f"Stored stderr log to {stderr_output_file}")

                # Parse the logs and check for unexpected errors
                unexpected_errors = get_unexpected_errors(stderr_output_file, yaml_file)

                # Accumulate unexpected errors
                if unexpected_errors:
                    error_message = (
                        f"Test failed for {log_file_path.name}. Unexpected errors:\n"
                        + "\n".join(unexpected_errors)
                    )
                    all_unexpected_errors.append(error_message)
        else:
            pytest.fail(f"Log file {log_file_path} does not exist.")

    # Fail the test if there are any accumulated unexpected errors
    if all_unexpected_errors:
        error_message = "\n\n".join(all_unexpected_errors)
        pytest.logger.error(error_message)
        pytest.fail(error_message)

    pytest.logger.info("All tests passed. No unexpected errors in stderr.")
