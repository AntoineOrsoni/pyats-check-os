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

