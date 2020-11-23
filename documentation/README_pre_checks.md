# Utilisation
```bash
python pre_checks.py --testbed /link/to/testbed.yaml
```

# Variables that can be changed
```python
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
when_tested = "before"
os_target_version = "16.10.1"
```
* `os_target_filenames`: list of filenames that will be checked on the router.
* `when_tested`: when has the test been run. This value will be saved in the DB. It will indicate if the output is `pre_check` or `post_check`.
* `os_target_version`: the current OS version to be checked on the router.

# Backbone of the script

The script is divided in three main parts:
* `CommonSetup`: which takes care of the initial setup. If one of these steps fails, other main parts will not be run. Ex: if we can't connect to the devices, there's no point to run the tests.
    * Loading the devices from the `testbed`,
    * Connecting to the devices,
    * Saving outputs to the database.
* `TestCase`: which takes care of the testing itself. Comparing outputs and expectations.
* `CommonCleanup`: which takes care of the final setup. Disconnecting from the devices.

# Tests run

### `all_outputs_copied_db(self, testbed)`

For a given `testbed`, verifies that the outputs have been correctly saved to the db. If not, triggers and `ERROR`: further tests will not be run.

### `check_os_copied_device(self, testbed)`

For a given `testbed`, verifies that the list of files have been copied successfully.

### `check_os_current_version_device(self, testbed)`

For a given `testbed`, verifies the current version of the device.
