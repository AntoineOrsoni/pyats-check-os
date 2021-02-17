[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/AntoineOrsoni/pyats-check-os)

# pyATS-checks-os
Leveragging `pyATS` and `Genie` to check run `pre_checks` and `post_check` on a `testbed`.

# Installing the requirements
pyATS supports Python versions from 3.5 to 3.8 (i.e. 3.9 is not yet supported). You can check the latest information here:

> https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/install/installpyATS.html

```bash
pip install -r requirements.txt
touch sqlite/db/checks.db
python sqlite/init_database.py
```

First line will install the right librairies.
Second and third line will create and initiate the database with the right tables and headers.

# Code versions

Below the release notes for each version. You can download an older version [here](https://github.com/AntoineOrsoni/pyats-check-os/tags).

## v1.0

* Initial version.

## v1.1

* Minor update, mainly bug fixes.
* Adding the README documentation for `pre_checks` and `post_checks`.

## v1.2

* Minor update, mainly bug fixes.

## v1.3

* Minor update, mainly bug fixes.

## v1.4

* In the `pre_checks` we are now verifying the Rommon files as well.
* Adding a few error handlings (ex: empty Genie output before folder does not exist).

## v1.5

* Adding the support for devices with 2 RSP.
* Adding a check to verify the commands `boot system bootflash:/...` are pushed, and in the right order. 
* If the VRF doesn't exist on the device before and after, the test is Passed.

## v1.6

* Documentation update
    * `./documentation/README*` has been updated,
    * Adding `./documentation/USECASE.md` to describe the use case,
    * Added the supported python release for pyATS.

## v1.7

* `rommon` files can be put in a specific folder (not always the root folder),
* Documentation has been updated accordingly.

## v1.8

* fixing dual RSP issue. Device has two RSP slots but only one of the two RSP is inserted.

## v 1.9

* Adding a check for CPU utilisation for the last 5 minutes.

# Using the scripts
## Testbed

The two below scripts below (`pre_checks` and `post_checks`) will use a testbed file, with all the information about the devices we will verify. Information will include elements such as:
* IP address,
* Port,
* Credentials,
* Protocol (SSH, telnet),
* Type of device.

A sample testbed file is provided: `./testbed_template.yaml`. You can read the documentation on how to create a testbed file, here: 

> https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/quickstart/manageconnections.html#creating-testbed-yaml-file

## Pre-checks
```bash
python pre_checks.py --testbed /link/to/testbed.yaml
```
[Complete details are explained here.](documentation/README_pre_checks.md)

## Post-checks
```bash
python post_checks.py --testbed /link/to/testbed.yaml
```
[Complete details are explained here.](documentation/README_post_checks.md)

## Printing the diff

To be used after the migration, in case you need to print a specific output, or compare an output before and after the migration.

```bash
python check_diff.py --hostname "device_hostname" --testname "test_name" --when "when_tested"
```
* `--hostname` is the complete hostname of the device, as saved in the database.
* `--testname` is the name of the test. On the left, the `testname`, on the right the related IOS XE command:
    - `route_summary` > `show ip route summary`
    - `routes`        > `show ip route`
    - `isis`          > `show ip isis neighbors`
    - `xconnect`      > `show xconnect all`
    - `cpu`           > `show cpu processes`
* `--when` is when the test has been run.
    - `both`      > for a diff `before/after`
    - `after`     > for a specific output `after`
    - `before`    > for a specific output `before`

## Toolbox
The toolbox includes multiple librairies to clarify the code.
* `database.py`: includes all functions relating to database interaction. 
    * Getting outputs from the DB.
    * Adding outputs to the DB.
* `pyats_checks.py`: contains all the check functions.
    * Leveraging Genie Parsers to extract a specific output, and saving it to the database.
    * Leveraging the `database.py` library to compare before/after outputs for a given `hostname` and `test_name`.
    * Printting the recap table.
* `pyats_diff.py`: leveraging the Genie Diff library to highlight differences for a given `hostname` and `test_name`.

## Database

We use `SQLite3` to store and retrieve information. Table schemes are stored in the `table-scheme` folder.

## Testbed

The devices used in the scripts must be added to a `testbed.yaml` file. A `testbed_template.yaml` file is provided as example.

Testbed file examples can also be found in the official documentation.

> https://pubhub.devnetcloud.com/media/pyats/docs/topology/example.html

# Demo
![Demo - Check OS](demo/demo_check_os.gif)

## Pre_checks

An example of the expected output can be found [here](./documentation/output_example_pre_checks.md).

## Post_checks

An example of the expected output can be found [here](./documentation/output_example_post_checks.md).


# pyATS documentation

The official `pyATS` documentation is available on the link below.
> https://pubhub.devnetcloud.com/media/pyats/docs/index.html

# AETest documentation

AEtest (Automation Easy Testing) is the standard test engineering automation harness. It offers a simple and straight-forward way for users to define, execute and debug testcases and testscripts, serving as a basis for other testscript templates & engines.

The official `AETest` documentation is available on the link below.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/introduction.html

## Difference between FAIL and ERROR

Except is configured differently, if a test is `FAIL`, it will continue with the next tests. If a test is `ERROR` it will move directly to the CommonCleanup section.

Complete documentation can be found here:

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/control.html