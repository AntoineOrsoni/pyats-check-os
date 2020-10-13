# pyATS-checks-os
Leveragging `pyATS` and `genie` to check the current OS version, and that an OS has successfuly been downloaded on a `testbed`.

# Usage
## Installing the requirements
```bash
pip install -r requirements.txt
```

## Using the script
### Verifying the OS has been copied on the device
```bash
python check_os_download.py --testbed /link/to/testbed.yaml
```
### Veryfying the current OS version
```bash
python check_current_version.py --testbed /link/to/testbed.yaml
```

# Demo
![Demo - Check OS](demo/demo_check_os.gif)

# pyATS documentation
The official `pyATS` documentation is available on the link below.
> https://pubhub.devnetcloud.com/media/pyats/docs/index.html