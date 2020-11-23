# pyATS-checks-os
Leveragging `pyATS` and `genie` to check run `pre_checks` and `post_check` on a `testbed`.

# Installing the requirements
```bash
pip install -r requirements.txt
touch sqlite/db/checks.db
python sqlite/init_database.py
```

# Using the script
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
```bash
python check_diff.py --hostname "device_hostname" --testname "test_name" --when "when_tested"
```
* `--hostname` is the complete hostname of the device, as saved in the database.
* `--testname` is the name of the test.
    - `route_summary` > `show ip route summary`
    - `routes`        > `show ip route`
    - `isis`          > `show ip isis neighbors`
    - `xconnect`      > `show xconnect all`
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

# Demo
![Demo - Check OS](demo/demo_check_os.gif)

# pyATS documentation
The official `pyATS` documentation is available on the link below.
> https://pubhub.devnetcloud.com/media/pyats/docs/index.html