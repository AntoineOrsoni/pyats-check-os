# Utilisation
```bash
python pre_checks.py --testbed /link/to/testbed.yaml
```

# Output example

An example of the expected output can be found [here](./output_example_pre_checks.md).

# Variables that can be changed
```python
when_tested = "before"
os_target_version = "16.10.1"
os_target_filenames = [
    "asr900rsp3-rpios-universalk9_npe.16.12.04.SPA.pkg",
    "asr900rsp3-rpbase.16.12.04.SPA.pkg",
    "asr900rsp3-rpaccess.16.12.04.SPA.pkg",
    "asr900rsp3-espbase.16.12.04.SPA.pkg",
    "packages.conf",
    "asr900rsp3-sipspa.16.12.04.SPA.pkg",
    "asr900rsp3-rpcontrol.16.12.04.SPA.pkg",
    "asr900rsp3-rpboot.16.12.04.SPA.pkg",
    "asr900rsp3-sipbase.16.12.04.SPA.pkg"
]
rommon_target_filenames = [
    "asr900-rommon.156-42r.S.pkg"
]
list_vrf = ["default", "v16", "v26"]
folder_images = {
    "new_os": "ImageTarget",
    "backup_os": "Image",
    "rommon": "Rommon"
}
```

* `when_tested`: when has the test been run. This value will be saved in the DB. It will indicate if the output is `pre_check` or `post_check`.
* `os_target_version`: the current OS version to be checked on the router.
* `os_target_filenames`: list of `os files` that will be checked on the router.
* `rommon_target_filenames`: list of rommon files that will be checked on the router.
* `list_vrf`: list of VRF that will be checked on the router.
* `folder_images`: dictionnary of the `new_os`, `backup_os` and `rommon` folders on the router.

# Backbone of the script

The script is divided in three main parts:
* `CommonSetup`: which takes care of the initial setup. If one of these steps fails, other main parts will not be run. Ex: if we can't connect to the devices, there's no point to run the tests.
    * Loading the devices from the `testbed`,
    * Connecting to the devices,
    * Saving outputs to the database.
* `TestCase`: which takes care of the testing itself. Comparing outputs and expectations. Tests are detailed in the next part.
* `CommonCleanup`: which takes care of the final setup. Disconnecting from the devices.

# Tests run

## Check that all outputs are properly copied in the SQLite database

`all_outputs_copied_db(self, testbed)`

For a given `testbed`, verifies that the outputs have been correctly saved to the db. If not, triggers and `ERROR`: further tests will not be run.

## Check that the new OS files are copied on the device

`check_os_copied_device(self, testbed)`

For a given `testbed`, verifies that the list of files have been copied successfully.
* `os_files` should be in the folder `folder_images['new_os']`. 
* `rommon_files` should be in the folder `folder_images['backup_os']`.

If the device has 2 RSP, files will be checked on the active and standby RSP. Folders on the standby RSP must have the same naming.

## Check the OS boot order

`check_boot_system_order(self, testbed)`

For a given `testbed`, verifies the correct order of the two `boot system bootflash:/...` commands. 
* First line must be `boot system bootflash:/{folder_new_os}/packages.conf`,
* Second line should be `boot system bootflash:/{folder_backup_os}/packages.conf`.

`folder_new_os` and `folder_backup_os` refer to the `folder_images` dictionnary.

## Check the current OS version of the device

`check_os_current_version_device(self, testbed)`

For a given `testbed`, verifies the current version of each device.

## Check the CPU utilisation for the last 5 minutes of the device

`check_cpu_device(self, testbed)`

For a given `testbed`, verifies the CPU utilisation for the last 5 minutes of each device.
