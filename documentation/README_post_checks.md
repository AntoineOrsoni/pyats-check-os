# Utilisation
```bash
python post_checks.py --testbed /link/to/testbed.yaml
```

# Output example

An example of the expected output can be found [here](./output_example_post_checks.md).

# Variables that can be changed

```python
os_target_version = "16.12.4"
isis_neighbors_delta = 0.8
xconnect_delta = 0.8
routes_delta = 0.8
list_vrf = ["default", "v16", "v26"]
```

* `os_target_version`: target version. Script will test that this version is running on the device.
* `isis_neighbors_delta`: delta between the number of `isis_neighbors` between `pre_checks` and `post_checks`. Possible value = [0-1].
    * 0: they can be completely different,
    * 1: they have to be 100% similar.
* `xconnect_delta`: same as above, for the number of `xconnects`. Possible value = [0-1].
    * 0: they can be completely different,
    * 1: they have to be 100% similar.
* `routes_delta` same as above, for the numebr of `routes` per protocol and per VRF. Possible value = [0-1].
    * 0: they can be completely different,
    * 1: they have to be 100% similar.
    * ex: number of `BGP` routes of vrf `default`, will be compared between `pre_checks` and `post_checks`. This test is independant to the number of `ISIS` routes of the vrf `Management`.
* `list_vrf`: list of VRF that will be checked on the router.

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

## Check the current OS version of the device

`check_os_current_version_device(self, testbed)`

For a given `testbed`, verifies the current version of each device.

## Check the CPU utilisation for the last 5 minutes of the device

`check_cpu_device(self, testbed)`

For a given `testbed`, verifies the CPU utilisation for the last 5 minutes of each device.

## Check the delta between the quantity of ISIS neighbors before and after the migration

`check_isis_neighbors_differences(self, testbed)`

For a given `testbed`, compares the number of `isis_neighbors` between `pre_checks` and `post_checks` with the `delta` value configured.

## Check the delta between the quantity of xconnects before and after the migration

`check_xconnect_differences(self, testbed)`

For a given `testbed`, compares the number of `xconnects` between `pre_checks` and `post_checks` with the `delta` value configured.

## Check the delta between the quantity of routes per protocol, per VRF, before and after the migration

`check_routes_delta_before_after(self, testbed, protocol, vrf)`

For a given `testbed`, `protocol` and `vrf` compares the number of `xconnects` between `pre_checks` and `post_checks` with the `delta` value configured. It does the comparison for each tuple of `(protocol, vrf)`.
* ex: number of `BGP` routes of vrf `default`, will be compared between `pre_checks` and `post_checks`. This test is independant to the number of `ISIS` routes of the vrf `Management`.

Test can fail for two reasons:
* The ratio of routes between `pre_checks` and `post_checks` is lower is the threshold.
* The VRF does not exist in the `pre_checks` and/or `post_checks`: it cannot be compared.