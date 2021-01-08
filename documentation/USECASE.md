Automating OS migration pre-checks and post-checks with pyATS
=====================================
Leveragging `pyATS` and `Genie` to check run `pre_checks` and `post_check` on a `testbed`.

Migrating from one OS version to the next is not always easy. It can get even more complex when you are running a service provider network, and you have 350 units to upgrade.

This page is an overview of the use case. [Complete details are explained in the README here](../README.md).

This project can be found on [DevNet Automation Exchange](https://developer.cisco.com/network-automation/): it provides shared code repositories for gathering information from your network, performing audits, activating policy changes, or managing applications, users, or devices. This file serves as a template to collect related links for Automation Exchange submissions.

# Backbone of the script

This repo contains three scripts that ease the migration : `pre_checks`, `post_checks` and `check_diff`, detailed below.

## Pre-checks

To be run before the migration. Run a defined set of tests, and save each output in the database.

```bash
python pre_checks.py --testbed /link/to/testbed.yaml
```
[Complete details are explained here.](./README_pre_checks.md)

## Post-checks

To be run after the migration. Run a defined set of tests, and save each output in the database.

```bash
python post_checks.py --testbed /link/to/testbed.yaml
```
[Complete details are explained here.](./README_post_checks.md)

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
* `--when` is when the test has been run.
    - `both`      > for a diff `before/after`
    - `after`     > for a specific output `after`
    - `before`    > for a specific output `before`

# White Paper

## pyATS community on Webex

You can join the pyATS community by clicking [here](https://eurl.io/#r18UzrQVr).

You can sign up, or create a Webex account [here](https://www.webex.com/).

## pyATS documentation

The official `pyATS` documentation is available on the link below.
> https://pubhub.devnetcloud.com/media/pyats/docs/index.html

## AETest documentation

AEtest (Automation Easy Testing) is the standard test engineering automation harness. It offers a simple and straight-forward way for users to define, execute and debug testcases and testscripts, serving as a basis for other testscript templates & engines.

The official `AETest` documentation is available on the link below.

> https://pubhub.devnetcloud.com/media/pyats/docs/aetest/introduction.html

# Related Sandbox
You can use the DevNet IOS XE sandbox (or a physical device) in order to run the code. You can find DevNet sandboxes [here](http://devnetsandbox.cisco.com/RM/Topology).

For instance, you can use the [always-on IOS XE sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology).

Please note that you might need to adapt the device configuration in order to run all the tests successfuly. For example, you might need to configure a few ISIS neighbors and xconnects. You might also need to adapt certain variables such as the current OS version. Please refer to the documentation, above.

## Links to DevNet Learning Labs
You can refer to [this page](https://developer.cisco.com/docs/pyats/#!hands-on-learning/learning-labs) which lists all available Learning Labs on pyATS and related subjects.

You can also refer to [this repo](https://github.com/AntoineOrsoni/pyats-devnet-se-hour) which includes 5 hands-on exercices on pyATS and Genie.

## Solutions on Ecosystem Exchange
You can find other pyATS related projects on [DevNet Automation Exchange](https://developer.cisco.com/codeexchange/explore/#search=pyats).
