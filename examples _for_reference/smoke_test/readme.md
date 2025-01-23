<a name="flashing-&-smoke-test"></a>

# Flashing and Smoke test

**Table of content**

- [Description](#Desc)
- [How to flash using flash.bat](#Flash)
- [How to run smoke tests](#SmokeTest)
- [Required tools to run flash.bat](#Tools)
- [Directory structure of smoke test](#DirectoryStructure)
  - [Boot_Mode.py](#BootMode)
  - [Common files](#CommonFiles)
  - [ECU files](#EcuFiles)
    - [TeraTerm (TTL) Macros](#TTLMacros)
  - [Managing machine configuration](#MachineConfig)
  - [power supply controller](#PowerSupply)
  - [Tests](#Tests)

<a name="Desc"></a>

## Description

This directory contains all the required scripts to flash the Toliman ECU. To develop the smoke tests the python unit test frame work is used.

<a name="Flash"></a>

## How to flash using flash.bat

Flashing the ECU can be done with the software copied to the Test bench and passing that path to [flash.bat](./flash.bat) as below:

```batch
c:\path-to-repo\ford-oneparking\tools\cus\smoke_test\flash.bat C:\path-to-your\Toliman-flash-SW
```

All the logs will be stored under `c:\path-to-repo\ford-oneparking\tools\cus\smoke_test\logs\` directory. The names of the logs will have the flash.py step names as prefix. So each step will create its own step-name_TTL.log file.Some log files may
not have TTL as postfix as these steps don't run TTL Macros.
Always pull the latest changes of the `ford-oneparking` repository from git!

<a name="SmokeTest"></a>

## How to run smoke tests

To run the smoke tests the pytest package is used. After flashing use the following command to run the tests:

```batch
pytest c:\path-to-repo\ford-oneparking\tools\cus\smoke_test\tests\
```

All the logs will be stored under `c:\path-to-repo\ford-oneparking\tools\cus\smoke_test\logs` directory.
Tests running Teraterm macros will have two logs:

- test-name.log: Contains the special logging messages of tests
- test-name_TTL.log: Contains the output of the teraterm macro run on ECU

<a name="Tools"></a>

## Required tools to run flash.bat

|Name     |Version| link| Comment|
|---------|-------|-------|---|
|Python|3.9.5.0.2|\\\\abtvdfs2.de.bosch.com\\ismdfs\\ida\\abt\\FD3_Gen\\Prk_Project\\00_Artifact\\Tools\\3.9.5.0.2.ZIP|additional packages: hiyapico, pytest-csv, pytest-html|
|Teraterm |4.106  |\\\\abtvdfs2.de.bosch.com\\ismdfs\\ida\\abt\\FD3_Gen\\Prk_Project\\00_Artifact\\Tools\\teraterm-4.106||
|Uniflash |8.0.4026|\\\\abtvdfs2.de.bosch.com\\ismdfs\\ida\\abt\\FD3_Gen\\Prk_Project\\00_Artifact\\Tools\\uniflash_sl.8.0.0.4026.exe||

For complete test bench setup see: [Ford PRK Test Bench Setup](https://inside-docupedia.bosch.com/confluence/x/skd0ow)

<a name="DirectoryStructure"></a>

## Directory structure of smoke test

<a name="BootMode"></a>

### boot_mode.py

This file is used to set the boot mode of ECU with help of Raspberry-Pi or Banana-Pi. In this file we use SFTP execute to run some specific shell scripts which were placed on these Pi's. All our Pi's are having the shell scripts of same names which in turn control the pins. These pins control the Debug board to set the ECU in required mode.
These modes sre:

- UART: Special mode in which the ECU halts the boot and prints "C" on the command prompt in regular intervals
- Normal: In this mode ECU fires up normally but can be halt to get into OPSI-mode manually by pressing any key during the 3 sec wait time. Otherwise the ECU continues to boot normally.

<a name="CommonFiles"></a>

### common files

The files in this folder contain general implementations for specific interfaces or checks. These can be used by importing into a python file. These files can not be called directly as other python files found in other directories as these do not have argument parser implementation.

<a name="EcuFiles"></a>

### ecu files

In this directory there are TTL Macros and some other files which are closely connected to the ECU control. The serial output analyzer is used to analyze the output of the ECU after setting it in a specific boot mode.

<a name="TTLMacros"></a>

#### TeraTerm (TTL) Macros

The TTL Macros are used for flashing the ECU. These fire specific commands needed to flash the ECU. These also check the output after each command and if an error occurs then the script is aborted. These macros need teratermpro.exe to run and during their run they produce a log file mit postfix `TTL.log`.

The Timeout for the Macros is set to 50 sec. If a command or check exceeds this limit the Macro will abort, which will cause the flash.py to exit the flashing process.

There are two macros for a load_raw_ifs_image step:

- load_raw_ifs_image_marvell_init
- load_raw_ifs_image

The one with postfix `marvell_init` sets special memory values for getting the TFTP server (Ethernet connection) working with vector box VN5620. This is not needed for other Vector hardware, so the flash.py decides which file to use according to the `ECU::marvell_init` flag in the config.

More info on Flashing steps can be found [here](https://inside-docupedia.bosch.com/confluence/x/ELA2pg)

<a name="MachineConfig"></a>

## Managing machine configuration

The configuration is divided into two parts. One is default config and others are Host specific configurations. The default config must not be changed due to a different host settings.

The default config can be overridden with a host config (test bench host name). For this, one needs to copy default config yaml and change the name to Host-Name.yml (e.g. FE-C-009xx.yml). Then change the required config parts and remove the common parts to keep it tiny and tidy.

for example you can refer or copy directly [FE-C-009xx.yml](./machine_configs/FE-C-009XX.yml) and add additional values if needed. During the run of flash.py the default config is overridden with values from the host configuration yaml according to the host on which it is running.

<a name="PowerSupply"></a>

### power supply controller

Power supply controller script is written for EA power supplies only. This script can be used for Single and Dual channel EA Power Controllers.

This script can be called independently and also can be imported into a test file to start or toggle the power supply. Toggling the power supply always sets the voltage to 0 and back to given voltage.

<a name="Tests"></a>

### Tests

Tests directory has all the tests. For processor tests we are using unittest framework with the base base_test.py, which implements the common methods init, setup and teardown for every test. Test_up.py contains the tests. These can be run with pytest package directly.
