```
2020-12-22T09:53:18: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:18: %AETEST-INFO: |                            Starting common setup                             |
2020-12-22T09:53:18: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:18: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:18: %AETEST-INFO: |                      Starting subsection check_testbed                       |
2020-12-22T09:53:18: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:18: %SCRIPT-INFO: List of Devices:
2020-12-22T09:53:18: %SCRIPT-INFO:   - ASR903_3
2020-12-22T09:53:18: %SCRIPT-INFO:   - ASR903_4
2020-12-22T09:53:18: %SCRIPT-INFO:   - ASR903_5
2020-12-22T09:53:18: %SCRIPT-INFO:   - ASR903_6
2020-12-22T09:53:18: %AETEST-INFO: The result of subsection check_testbed is => PASSED
2020-12-22T09:53:18: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:18: %AETEST-INFO: |                    Starting subsection connect_to_devices                    |
2020-12-22T09:53:18: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:18: %SCRIPT-INFO: Verifying that I can connect to each device.
2020-12-22T09:53:33: %SCRIPT-ERROR: Could not connect to device ASR903_6.
2020-12-22T09:53:33: %AETEST-INFO: The result of subsection connect_to_devices is => PASSED
2020-12-22T09:53:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:33: %AETEST-INFO: |                   Starting subsection save_all_outputs_db                    |
2020-12-22T09:53:33: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:33: %SCRIPT-INFO: Saving outputs for each device.
2020-12-22T09:53:42: %AETEST-INFO: The result of subsection save_all_outputs_db is => PASSED
2020-12-22T09:53:42: %AETEST-INFO: The result of common setup is => PASSED
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %AETEST-INFO: |                     Starting testcase CheckSaveDatabase                      |
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %AETEST-INFO: |                    Starting section all_outputs_copied_db                    |
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %SCRIPT-INFO: Checking that all the outputs are saved in the DB for each device.
2020-12-22T09:53:42: %AETEST-INFO: The result of section all_outputs_copied_db is => PASSED
2020-12-22T09:53:42: %AETEST-INFO: The result of testcase CheckSaveDatabase is => PASSED
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %AETEST-INFO: |                       Starting testcase CheckOperData                        |
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %AETEST-INFO: |                   Starting section check_os_copied_device                    |
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %SCRIPT-INFO: Checking that the OS is copied on each device bootflash:/
2020-12-22T09:53:42: %SCRIPT-ERROR: OS files are missing on ASR903_3.
2020-12-22T09:53:42: %SCRIPT-INFO: ASR903_3 has 2 RSP.
2020-12-22T09:53:42: %AETEST-ERROR: Failed reason: OS files are not copied on the above devices,
2020-12-22T09:53:42: %AETEST-ERROR: not in the right folder, or folder doesn't exist.
2020-12-22T09:53:42: %AETEST-ERROR: If device has 2 RSP, check the standby-bootflash.
2020-12-22T09:53:42: %AETEST-INFO: The result of section check_os_copied_device is => FAILED
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %AETEST-INFO: |                   Starting section check_boot_system_order                   |
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %SCRIPT-INFO: Checking that the `boot system bootflash:/...` lines are present and in the correct order
2020-12-22T09:53:42: %SCRIPT-ERROR: `boot system bootflash:/...` command missing on ASR903_3
2020-12-22T09:53:42: %SCRIPT-ERROR: `boot system bootflash:/...` command missing on ASR903_4
2020-12-22T09:53:42: %AETEST-ERROR: Failed reason: `boot system bootflash:/...` missing, not in the right order or
2020-12-22T09:53:42: %AETEST-ERROR: not pointing to the right folder on the devices above.
2020-12-22T09:53:42: %AETEST-INFO: The result of section check_boot_system_order is => FAILED
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %AETEST-INFO: |               Starting section check_os_current_version_device               |
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %SCRIPT-INFO: Checking that each device is using 16.10.1
2020-12-22T09:53:42: %SCRIPT-ERROR: ASR903_3 is not using 16.10.1. Using 16.12.4
2020-12-22T09:53:42: %SCRIPT-ERROR: ASR903_4 is not using 16.10.1. Using 16.12.4
2020-12-22T09:53:42: %SCRIPT-ERROR: ASR903_5 is not using 16.10.1. Using 16.12.4
2020-12-22T09:53:42: %AETEST-ERROR: Failed reason: The above devices are not using 16.10.1.
2020-12-22T09:53:42: %AETEST-INFO: The result of section check_os_current_version_device is => FAILED
2020-12-22T09:53:42: %AETEST-INFO: The result of testcase CheckOperData is => FAILED
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %AETEST-INFO: |                           Starting common cleanup                            |
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:53:42: %AETEST-INFO: |                 Starting subsection disconnect_from_devices                  |
2020-12-22T09:53:42: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:54:21: %AETEST-INFO: The result of subsection disconnect_from_devices is => PASSED
2020-12-22T09:54:21: %AETEST-INFO: The result of common cleanup is => PASSED
2020-12-22T09:54:21: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:54:21: %AETEST-INFO: |                               Detailed Results                               |
2020-12-22T09:54:21: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:54:21: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
2020-12-22T09:54:21: %AETEST-INFO: --------------------------------------------------------------------------------
2020-12-22T09:54:21: %AETEST-INFO: .
2020-12-22T09:54:21: %AETEST-INFO: |-- common_setup                                                          PASSED
2020-12-22T09:54:21: %AETEST-INFO: |   |-- check_testbed                                                     PASSED
2020-12-22T09:54:21: %AETEST-INFO: |   |-- connect_to_devices                                                PASSED
2020-12-22T09:54:21: %AETEST-INFO: |   `-- save_all_outputs_db                                               PASSED
2020-12-22T09:54:21: %AETEST-INFO: |-- CheckSaveDatabase                                                     PASSED
2020-12-22T09:54:21: %AETEST-INFO: |   `-- all_outputs_copied_db                                             PASSED
2020-12-22T09:54:21: %AETEST-INFO: |-- CheckOperData                                                         FAILED
2020-12-22T09:54:21: %AETEST-INFO: |   |-- check_os_copied_device                                            FAILED
2020-12-22T09:54:21: %AETEST-INFO: |   |-- check_boot_system_order                                           FAILED
2020-12-22T09:54:21: %AETEST-INFO: |   `-- check_os_current_version_device                                   FAILED
2020-12-22T09:54:21: %AETEST-INFO: `-- common_cleanup                                                        PASSED
2020-12-22T09:54:21: %AETEST-INFO:     `-- disconnect_from_devices                                           PASSED
2020-12-22T09:54:21: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:54:21: %AETEST-INFO: |                                   Summary                                    |
2020-12-22T09:54:21: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:54:21: %AETEST-INFO:  Number of ABORTED                                                            0 
2020-12-22T09:54:21: %AETEST-INFO:  Number of BLOCKED                                                            0 
2020-12-22T09:54:21: %AETEST-INFO:  Number of ERRORED                                                            0 
2020-12-22T09:54:21: %AETEST-INFO:  Number of FAILED                                                             1 
2020-12-22T09:54:21: %AETEST-INFO:  Number of PASSED                                                             3 
2020-12-22T09:54:21: %AETEST-INFO:  Number of PASSX                                                              0 
2020-12-22T09:54:21: %AETEST-INFO:  Number of SKIPPED                                                            0 
2020-12-22T09:54:21: %AETEST-INFO:  Total Number                                                                 4 
2020-12-22T09:54:21: %AETEST-INFO:  Success Rate                                                             75.0% 
2020-12-22T09:54:21: %AETEST-INFO: --------------------------------------------------------------------------------
2020-12-22T09:54:21: %SCRIPT-INFO: 
2020-12-22T09:54:21: %SCRIPT-INFO: 
2020-12-22T09:54:21: %SCRIPT-INFO: +----------+----------------+-----------+-------------+---------+
2020-12-22T09:54:21: %SCRIPT-INFO: | hostname | connect_device | os_copied | boot_system | 16.10.1 |
2020-12-22T09:54:21: %SCRIPT-INFO: +----------+----------------+-----------+-------------+---------+
2020-12-22T09:54:21: %SCRIPT-INFO: | ASR903_3 |      Pass      |    Fail   |     Fail    |   Fail  |
2020-12-22T09:54:21: %SCRIPT-INFO: | ASR903_4 |      Pass      |    Pass   |     Fail    |   Fail  |
2020-12-22T09:54:21: %SCRIPT-INFO: | ASR903_5 |      Pass      |    Pass   |     Pass    |   Fail  |
2020-12-22T09:54:21: %SCRIPT-INFO: | ASR903_6 |      Fail      |    Fail   |     Fail    |   Fail  |
2020-12-22T09:54:21: %SCRIPT-INFO: +----------+----------------+-----------+-------------+---------+
```