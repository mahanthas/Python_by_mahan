# Copyright (C) 2024 Robert Bosch GmbH.
# The reproduction, distribution and utilization of this file as
# well as the communication of its contents to others without
# express authorization is prohibited. Offenders will be held
# liable for the payment of damages. All rights reserved in the
# event of the grant of a patent, utility model or design.

import argparse
import glob
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from toliman_flashing.archiver import extract_archive_file
from toliman_flashing.artifactory import download_archive_file, download_file
from toliman_flashing.boot_mode import boot_mode
from toliman_flashing.conan_helper import (
    conan_download,
    conan_download_package_from_lockfile,
    find_conan_package_ref_in_lock_file,
)
from toliman_flashing.config_merger import get_host_config
from toliman_flashing.deployer import (
    auto_deploy_test_binaries,
    cleanup_deploy_dirs,
    overwrite_flash_files_on_tftp_server,
    reflash_dsps,
    rename_startup_script,
    revert_startup_script,
)
from toliman_flashing.ecu_check import (
    call_sync_shutdown_per_ssh,
    check_ecu_availibility_per_ping,
)
from toliman_flashing.globals import Globals
from toliman_flashing.jenkins_build_info import (
    get_artifacts_of_a_build,
    get_last_succesful_build_id,
)
from toliman_flashing.logger import Logger
from toliman_flashing.powershell_cmd import powershell_command
from toliman_flashing.sftp_client import sftp_get_file, sftp_put_all_files_of_dir
from toliman_flashing.ssh_client import ssh_connect, ssh_execute

# fmt: on
LOGGER: logging.Logger = logging.Logger("")
VIPERS1_BUILD_VARIANT = "neutrino-7.1-armv8-qcc-8.3-qos-2.2.6-release"
# for ev5 kernels neutrino profile
LIB_KERNELES_BUILD_TARGET_VARIANT = "neutrino-7.1-armv8-qcc-8.3-qos-2.2.6-release"
LIB_KERNAL_QUERY_TARGET_STRING = "BOARD=Toliman5 AND os=Neutrino AND arch=armv8 AND build_type=Release AND DL_SCOPE=CALIB AND compiler.sdp=qos2.2.6-aarch64-toolchain/1.x.x@saturn/develop"
# for EV5 c7x-dsp profile
LIB_KERNEL_C7X_BUILD_VARIANT = "freertos-dsp-c7x-ti-cgt-c7000-ev5-release"
LIB_KERNEL_C7X_QUERY_STRING = "BOARD=Toliman5 AND os=FreeRTOS AND arch=dsp-c7x-c7000 AND build_type=Release AND compiler=ti-cgt-c7000 AND compiler.version=4.1.0.LTS"
# FOR EV5 armv7-r5f profile
LIB_KERNEL_R5F_BUILD_VARIANT = "freertos-armv7-r5f-vfpv3-d16-ti-arm-clangllvm-ev5-release"
LIB_KERNEL_R5F_QUERY_STRING = "BOARD=Toliman5 AND os=FreeRTOS AND arch=armv7-r5f-vfpv3_d16 AND build_type=Release AND compiler=ti-arm-clangllvm AND compiler.version=3.2.2.LTS"
JENKINS_DEVELOP_JOB_URL = "https://oneparking-integration-env-ocp.de.bosch.com/jenkins-master-ford-oneparking/job/subsys-vipers1-ti-ford_target/job/develop/lastSuccessfulBuild/"
STRING_TO_DETECT_BLUEOCEAN_URL = "blue/organizations/jenkins"
DSP_FILE_LIST = [
    "vx_app_rtos_qnx_c7x_1.out",
    "vx_app_rtos_qnx_c7x_2.out",
    "vx_app_rtos_qnx_c7x_3.out",
    "vx_app_rtos_qnx_c7x_4.out",
    "app_remoteswitchcfg_server_strip.xer5f",
    "vx_app_rtos_qnx_mcu2_1.out",
]


def rename_dsp_file_in_tftp(
    raspi_config: Dict,
    dsp_file_path: str = "/srv/tftp/",
    list_of_files: List = DSP_FILE_LIST,
) -> None:
    """Rename dsp files with .bak.

    Args:
        raspi_config (Dict): ECU configuration from host config
        dsp_file_path (str): Startup script path. Defaults to "/opt/vrte/etc/startup.sh".
        list-of_files (list): List of all the dsp files
    """
    logger = Logger.get_logger("rename_dsp_file_in_tftp.log")

    for i in range(len(list_of_files)):
        logger.info("===Renaming dsp files ===")
        ssh_execute(
            command=f"mv {dsp_file_path}{list_of_files[i]} {dsp_file_path}{list_of_files[i]}.bak",
            username=raspi_config["user_name"],
            server=raspi_config["ip_address"],
            port=raspi_config["ssh_port"],
        )
        logger.info("===Renaming dsp files Done===")


def revert_dsp_file_in_tftp(
    raspi_config: Dict,
    dsp_file_path: str = "/srv/tftp/",
    list_of_files: List = DSP_FILE_LIST,
) -> None:
    """Revert dsp files.

    Args:
        raspi_config (Dict): ECU configuration from host config
        dsp_file_path (str): Startup script path. Defaults to "/opt/vrte/etc/startup.sh".
        list-of_files (list): List of all the dsp files
    """
    logger = Logger.get_logger("revert_dsp_file_in_tftp.log")

    for i in range(len(list_of_files)):
        logger.info("===Revert dsp files ===")
        ssh_execute(
            command=f"mv {dsp_file_path}{list_of_files[i]}.bak {dsp_file_path}{list_of_files[i]}",
            username=raspi_config["user_name"],
            server=raspi_config["ip_address"],
            port=raspi_config["ssh_port"],
        )
        logger.info("===Revert dsp files Done===")


def announce_step(input_str: str, char: str = "="):
    """Print highlighted content

    Args:
        content (string): string to be placed in between the highlighting lines
    """
    LOGGER.info(char * 90)
    LOGGER.info(input_str)
    LOGGER.info(char * 90)


def set_vipers2_activities_permision_to_non_executable(ecu_config):
    """Remount /m3 directoy with write access.

    Args:
        ecu_config (Dict): ECU config from host config.
    """
    file_list = ecu_config.get("vipers2_activity_list")
    for file_name in file_list:
        ssh_execute(
            command=f"chmod 644 {file_name}",
            username=ecu_config.get("user_name"),
            server=ecu_config.get("ip_address"),
            port=ecu_config.get("ssh_port"),
            password="",
        )


def remount_m3_dir(ecu_config):
    """Set vipers2 activities permission to non-execution.

    Args:
        ecu_config (Dict): ECU config from host config.
    """
    ssh_execute(
        command=f"mount -uw /m3",
        username=ecu_config.get("user_name"),
        server=ecu_config.get("ip_address"),
        port=ecu_config.get("ssh_port"),
        password="",
    )
    ssh_execute(
        command=f"mkdir -p /nvm/bosch/prk/rbp_vipers1_ti_ford/",
        username=ecu_config.get("user_name"),
        server=ecu_config.get("ip_address"),
        port=ecu_config.get("ssh_port"),
        password="",
    )


def find_lockfile_path(GIT_IGNORE_PATH, profile_name):
    file_path = glob.glob(
        f"{GIT_IGNORE_PATH}/**/{profile_name}**/**/{VIPERS1_BUILD_VARIANT}/full_lockfile.lock",
        recursive=True,
    )
    for lockfile_path in file_path:
        LOGGER.info(f"Lockfile path: {lockfile_path}")
        return lockfile_path


def conan_download_package_from_name(
    conan_package_name: str,
    conan_remote: str = Globals.CONAN_REMOTE_ONEP_NAME,
) -> None:
    """Download the last four versions of a package from the Conan remote.

    Args:
        conan_remote_name (str): Conan remote name
        package_name (str): The name of the package to search for and download
    """
    # Search for available versions of the package
    conan_search_cmd = (
        f"$ENV:CONAN_REVISIONS_ENABLED=1; conan search {conan_package_name} -r {conan_remote} --raw"
    )
    versions = powershell_command(conan_search_cmd)

    # Split the result to get versions and keep only the last six
    version_list = versions.splitlines()[-6:]
    print(f"the version downloading is {version_list}")

    if not version_list:
        raise ValueError(f"No versions found for package {conan_package_name} in {conan_remote}.")

    # Download the last four versions
    for version in version_list:
        # Build the correct package reference without duplicating the package name
        print(f"the version downloading is {version}")
        full_package_name = f"{version}"
        conan_download_cmd = f"conan download {full_package_name} -r {conan_remote}"
        powershell_command(conan_download_cmd)
        print(f"Downloaded package {full_package_name}")


def target_build_download(
    artifactory_user: str,
    artifactory_token: str,
    target_build_url: str,
    package_extract_dir_postfix: str,
    package_name: str,
    query_string: str = "",
):
    if target_build_url is not None and target_build_url != "None":
        if STRING_TO_DETECT_BLUEOCEAN_URL in target_build_url:
            # Blueocean URL will be changed as shown below
            # Blueocen: https://oneparking-integration-env-ocp.de.bosch.com/jenkins-master-ford-oneparking/blue/organizations/jenkins/ford-oneparking_target/detail/develop/56/pipeline/
            # API URL: https://oneparking-integration-env-ocp.de.bosch.com/jenkins-master-ford-oneparking/job/ford-oneparking_target/job/develop/56
            target_build_url = (
                target_build_url.replace(STRING_TO_DETECT_BLUEOCEAN_URL, "job")
                .replace("detail", "job")
                .replace("pipeline", "")
                .strip("/")
            )

        build_id = target_build_url.strip("/").split("/")[-1]
        job_url = target_build_url.strip("/").strip(f"{build_id}")
        if build_id == "lastSuccessfulBuild":
            build_id = get_last_succesful_build_id(job_url=job_url, non_nightly=True)
        LOGGER.info(f"Downloading conan packages for build {build_id} from {job_url}")
    else:
        raise IOError("FORD_TARGET_BUILD_URL not passed!")

    build_artifacts_zip_path = get_artifacts_of_a_build(job_url=job_url, build_id=build_id)
    build_artifacts_path = Globals.GIT_IGNORE_PATH.joinpath(build_artifacts_zip_path.stem)
    extract_archive_file(build_artifacts_zip_path, build_artifacts_path)
    lock_file_path = find_lockfile_path(build_artifacts_path, package_name)

    conan_download_package_from_lockfile(
        lockfile_path=lock_file_path,
        conan_package_name=package_name,
        query_string=query_string,
        package_extract_dir_postfix=package_extract_dir_postfix,
    )

    return lock_file_path


def run_deploy_steps(
    step_to_run: str,
    vipers1_target_build_url: str,
    vision_kernels_target_build_url: str,
    multibranch_build_url: str,
    artifactory_user: str,
    artifactory_token: str,
):
    """_summary_

    Args:
        step_to_run (str): _description_
        vipers1_target_build_url (str): _description_
        vision_kernels_target_build_url (str): _description_
        artifactory_user (str): _description_
        artifactory_token (str): _description_
    """
    global LOGGER
    LOGGER = Logger.get_logger(f"{step_to_run}.log", sub_dir="deploy_vs1", create_new=True)

    announce_step(f"Executing step {step_to_run}")

    vrte_scripts = Path.joinpath(
        Path(__file__).resolve().parent, "tests", "resource", "vrte"
    ).absolute()

    host_config = get_host_config(host_config_dir=Globals.DEFAULT_MACHINE_CONFIG_DIR)
    power_config = host_config["PowerSupply"]
    ecu_config = host_config["ECU"]
    raspi_config = host_config["RaspberryPi"]
    tools_config = host_config["Tools"]
    vrte_path = ecu_config.get("vrte_path")
    vrte_script_path = vrte_path + "start_vrte.sh"

    if step_to_run == "download_conan_package":
        conan_download_package_from_name("rbp_conan_common")
        if multibranch_build_url is not None:
            lock_file_path = target_build_download(
                artifactory_user,
                artifactory_token,
                target_build_url=multibranch_build_url,
                package_name="rbp_vipers1_ti_ford",
                package_extract_dir_postfix="cp",
            )
        elif vipers1_target_build_url is not None:
            # Download vipers1 conan packages
            lock_file_path = target_build_download(
                artifactory_user,
                artifactory_token,
                target_build_url=vipers1_target_build_url,
                package_name="rbp_vipers1_ti_ford",
                package_extract_dir_postfix="cp",
            )

        if vision_kernels_target_build_url is not None:
            # Download lib kernal vison conan package
            lock_file_path = target_build_download(
                artifactory_user,
                artifactory_token,
                target_build_url=vision_kernels_target_build_url,
                query_string=LIB_KERNAL_QUERY_TARGET_STRING,
                package_name="rbp_vision_kernels",
                package_extract_dir_postfix="Neutrino",
            )
            # Download dsp-c7x conan package
            lock_file_path = target_build_download(
                artifactory_user,
                artifactory_token,
                target_build_url=vision_kernels_target_build_url,
                query_string=LIB_KERNEL_C7X_QUERY_STRING,
                package_name="rbp_vision_kernels",
                package_extract_dir_postfix="C7X",
            )
            # Download arm-r5f conan package
            lock_file_path = target_build_download(
                artifactory_user,
                artifactory_token,
                target_build_url=vision_kernels_target_build_url,
                query_string=LIB_KERNEL_R5F_QUERY_STRING,
                package_name="rbp_vision_kernels",
                package_extract_dir_postfix="R5F",
            )
        else:
            print(
                "Downloading the Packages from the conan_download function when lib_vision_kernel link is not available"
            )
            conan_download_package_from_lockfile(
                lockfile_path=lock_file_path,
                conan_package_name="rbp_vision_kernels",
                query_string=LIB_KERNAL_QUERY_TARGET_STRING,
                package_extract_dir_postfix="Neutrino",
            )
            conan_download_package_from_lockfile(
                lockfile_path=lock_file_path,
                conan_package_name="rbp_vision_kernels",
                query_string=LIB_KERNEL_C7X_QUERY_STRING,
                package_extract_dir_postfix="C7X",
            )
            conan_download_package_from_lockfile(
                lockfile_path=lock_file_path,
                conan_package_name="rbp_vision_kernels",
                query_string=LIB_KERNEL_R5F_QUERY_STRING,
                package_extract_dir_postfix="R5F",
            )

    if step_to_run == "auto_deploy":
        # +++++++ start prepare for deployment +++++++
        check_ecu_availibility_per_ping(ecu_config, power_config)
        # rename dsp files with .bak extension
        rename_dsp_file_in_tftp(raspi_config)
        # rename the main vrte script
        rename_startup_script(ecu_config, vrte_script_path)
        sftp_put_all_files_of_dir(
            vrte_scripts,
            vrte_path,
            ecu_config.get("user_name"),
            ecu_config.get("ip_address"),
            ecu_config.get("ssh_port"),
            password="",
            log_file_name="vrte_file_copy.log",
        )
        # Changed the file permission for vipers2 activities to 644
        set_vipers2_activities_permision_to_non_executable(ecu_config)
        # +++++++ end prepare for deployment +++++++
        # +++++++ start deploy firmware +++++++
        overwrite_flash_files_on_tftp_server(Globals.GIT_IGNORE_PATH, raspi_config)
        reflash_dsps(ecu_config, tools_config)
        check_ecu_availibility_per_ping(ecu_config, power_config)
        # +++++++ end deploy firmware +++++++
        # +++++++ start deploy vipers1 +++++++
        remount_m3_dir(ecu_config)
        auto_deploy_test_binaries(Globals.GIT_IGNORE_PATH, ecu_config)
        check_ecu_availibility_per_ping(ecu_config, power_config)
        # +++++++ end deploy vipers1 +++++++
    announce_step(f"Executing step {step_to_run} done!")

    if step_to_run == "prepare_for_deployment":
        check_ecu_availibility_per_ping(ecu_config, power_config)
        # rename dsp files with .bak extension
        rename_dsp_file_in_tftp(raspi_config)
        # rename the main vrte script
        rename_startup_script(ecu_config, vrte_script_path)
        sftp_put_all_files_of_dir(
            vrte_scripts,
            vrte_path,
            ecu_config.get("user_name"),
            ecu_config.get("ip_address"),
            ecu_config.get("ssh_port"),
            password="",
            log_file_name="vrte_file_copy.log",
        )
        # Changed the file permission for vipers2 activities to 644
        set_vipers2_activities_permision_to_non_executable(ecu_config)

    if step_to_run == "deploy_firmware":
        overwrite_flash_files_on_tftp_server(Globals.GIT_IGNORE_PATH, raspi_config)
        reflash_dsps(ecu_config, tools_config)
        check_ecu_availibility_per_ping(ecu_config, power_config)

    if step_to_run == "deploy_vipers1":
        remount_m3_dir(ecu_config)
        auto_deploy_test_binaries(Globals.GIT_IGNORE_PATH, ecu_config)
        check_ecu_availibility_per_ping(ecu_config, power_config)

    if step_to_run == "revert_after_deployment":
        # Boot the ECU to normal boot
        announce_step(f"\t\tExecuting ECU mode change to normal...")
        boot_mode(
            raspi_config["normal_boot_script"],
            raspi_config["ip_address"],
            raspi_config["ssh_port"],
            raspi_config["user_name"],
        )
        check_ecu_availibility_per_ping(ecu_config, power_config)
        # Revert dsp files by removing .bak extension
        revert_dsp_file_in_tftp(raspi_config)
        reflash_dsps(ecu_config, tools_config)
        # Revert the startup bak script to startup.sh
        ssh_execute(
            command=f"rm -f {vrte_script_path}",
            server=ecu_config.get("ip_address"),
            port=ecu_config.get("ssh_port"),
            username=ecu_config.get("user_name"),
            password="",
        )
        revert_startup_script(ecu_config, vrte_script_path)
        # Changed the file permission for vipers2 activities to 755
        file_list = ecu_config.get("vipers2_activity_list")
        for file_name in file_list:
            ssh_execute(
                command=f"chmod +x {file_name}",
                username=ecu_config.get("user_name"),
                server=ecu_config.get("ip_address"),
                port=ecu_config.get("ssh_port"),
                password="",
            )
    announce_step(f"Executing step {step_to_run} done!")


def parse_args(script_args):
    """Script arguments Parser

    Args:
        script_args (dict): script args

    Returns:
        Namespace: Arguments supplied to the scripts
    """
    # overwrite settings in case they are given on the console as well
    commandLineParser = argparse.ArgumentParser(
        description="Provides steps to flash the Tolliman ECU.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    commandLineParser.add_argument(
        "-s",
        "--step-to-run",
        choices=[
            "prepare_for_deployment",
            "deploy_firmware",
            "deploy_vipers1",
            "revert_after_deployment",
            "auto_deploy",
            "download_conan_package",
        ],
        type=str,
    )
    commandLineParser.add_argument(
        "-vu",
        "--vipers1-target-build-url",
        default=JENKINS_DEVELOP_JOB_URL,
        type=str,
    )
    commandLineParser.add_argument(
        "-lu",
        "--vision-kernels-target-build-url",
        default=None,
        type=str,
    )
    commandLineParser.add_argument(
        "-mu",
        "--multibranch-build-url",
        default=None,
        type=str,
    )
    commandLineParser.add_argument(
        "-au",
        "--artifactory-user",
        default=None,
        type=str,
    )
    commandLineParser.add_argument(
        "-at",
        "--artifactory-token",
        default=None,
        type=str,
    )

    return commandLineParser.parse_args(script_args)


def main(script_args):
    parsed_args = parse_args(script_args)

    run_deploy_steps(
        step_to_run=parsed_args.step_to_run,
        vipers1_target_build_url=parsed_args.vipers1_target_build_url,
        vision_kernels_target_build_url=parsed_args.vision_kernels_target_build_url,
        multibranch_build_url=parsed_args.multibranch_build_url,
        artifactory_user=parsed_args.artifactory_user,
        artifactory_token=parsed_args.artifactory_token,
    )


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
