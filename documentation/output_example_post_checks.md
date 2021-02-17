```
2021-02-17T13:11:09: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:09: %AETEST-INFO: |                            Starting common setup                             |
2021-02-17T13:11:09: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:09: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:09: %AETEST-INFO: |                      Starting subsection check_testbed                       |
2021-02-17T13:11:09: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:09: %SCRIPT-INFO: List of Devices:
2021-02-17T13:11:09: %SCRIPT-INFO:   - ASR903_3
2021-02-17T13:11:09: %SCRIPT-INFO:   - ASR903_4
2021-02-17T13:11:09: %SCRIPT-INFO:   - ASR903_5
2021-02-17T13:11:09: %SCRIPT-INFO:   - ASR903_6
2021-02-17T13:11:09: %AETEST-INFO: The result of subsection check_testbed is => PASSED
2021-02-17T13:11:09: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:09: %AETEST-INFO: |                    Starting subsection connect_to_devices                    |
2021-02-17T13:11:09: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:09: %SCRIPT-INFO: Verifying that I can connect to each device.
2021-02-17T13:11:13: %SCRIPT-ERROR: Could not connect to device ASR903_6.
2021-02-17T13:11:13: %AETEST-INFO: The result of subsection connect_to_devices is => PASSED
2021-02-17T13:11:13: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:13: %AETEST-INFO: |                   Starting subsection save_all_outputs_db                    |
2021-02-17T13:11:13: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:13: %SCRIPT-INFO: Saving outputs for each device.
2021-02-17T13:11:19: %AETEST-INFO: The result of subsection save_all_outputs_db is => PASSED
2021-02-17T13:11:19: %AETEST-INFO: The result of common setup is => PASSED
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %AETEST-INFO: |                     Starting testcase CheckSaveDatabase                      |
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %AETEST-INFO: |                    Starting section all_outputs_copied_db                    |
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %SCRIPT-INFO: Checking that all the outputs are saved in the DB for each device.
2021-02-17T13:11:19: %AETEST-ERROR: Errored reason: output_lists has the wrong size. Expected 5, found 6
2021-02-17T13:11:19: %AETEST-INFO: The result of section all_outputs_copied_db is => ERRORED
2021-02-17T13:11:19: %AETEST-INFO: The result of testcase CheckSaveDatabase is => ERRORED
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %AETEST-INFO: |                       Starting testcase CheckOperData                        |
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %AETEST-INFO: |               Starting section check_os_current_version_device               |
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %SCRIPT-INFO: Checking that each device is using 16.12.4
2021-02-17T13:11:19: %SCRIPT-ERROR: ASR903_3 is not using 16.12.4. Using 16.12.5prd2
2021-02-17T13:11:19: %SCRIPT-ERROR: ASR903_5 is not using 16.12.4. Using 16.6.1
2021-02-17T13:11:19: %AETEST-ERROR: Failed reason: The above devices are not using 16.12.4.
2021-02-17T13:11:19: %AETEST-INFO: The result of section check_os_current_version_device is => FAILED
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %AETEST-INFO: |                      Starting section check_cpu_device                       |
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %SCRIPT-INFO: Checking the CPU utilisation on the device for the last 5 minutes.
2021-02-17T13:11:19: %AETEST-INFO: The result of section check_cpu_device is => PASSED
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %AETEST-INFO: |              Starting section check_isis_neighbors_differences               |
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %SCRIPT-INFO: Checking the differences before/after for isis_neighbors.
2021-02-17T13:11:19: %AETEST-INFO: The result of section check_isis_neighbors_differences is => PASSED
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %AETEST-INFO: |                 Starting section check_xconnect_differences                  |
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %SCRIPT-INFO: Checking the differences before/after for xconnect.
2021-02-17T13:11:19: %AETEST-INFO: The result of section check_xconnect_differences is => PASSED
2021-02-17T13:11:19: %AETEST-INFO: The result of testcase CheckOperData is => FAILED
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %AETEST-INFO: |                 Starting testcase CheckRoutes[protocol=bgp]                  |
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %AETEST-INFO: |        Starting section check_routes_delta_before_after[vrf=default]         |
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %SCRIPT-INFO: Checking the differences before/after for {'bgp': 'default'}.
2021-02-17T13:11:19: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=default] is => PASSED
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v16]           |
2021-02-17T13:11:19: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:19: %SCRIPT-INFO: Checking the differences before/after for {'bgp': 'v16'}.
2021-02-17T13:11:19: %SCRIPT-INFO: v16 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2021-02-17T13:11:20: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v16] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v26]           |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %SCRIPT-INFO: Checking the differences before/after for {'bgp': 'v26'}.
2021-02-17T13:11:20: %SCRIPT-INFO: v26 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2021-02-17T13:11:20: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v26] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: The result of testcase CheckRoutes[protocol=bgp] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |                 Starting testcase CheckRoutes[protocol=isis]                 |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |        Starting section check_routes_delta_before_after[vrf=default]         |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %SCRIPT-INFO: Checking the differences before/after for {'isis': 'default'}.
2021-02-17T13:11:20: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=default] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v16]           |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %SCRIPT-INFO: Checking the differences before/after for {'isis': 'v16'}.
2021-02-17T13:11:20: %SCRIPT-INFO: v16 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2021-02-17T13:11:20: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v16] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v26]           |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %SCRIPT-INFO: Checking the differences before/after for {'isis': 'v26'}.
2021-02-17T13:11:20: %SCRIPT-INFO: v26 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2021-02-17T13:11:20: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v26] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: The result of testcase CheckRoutes[protocol=isis] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |              Starting testcase CheckRoutes[protocol=connected]               |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |        Starting section check_routes_delta_before_after[vrf=default]         |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %SCRIPT-INFO: Checking the differences before/after for {'connected': 'default'}.
2021-02-17T13:11:20: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=default] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v16]           |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %SCRIPT-INFO: Checking the differences before/after for {'connected': 'v16'}.
2021-02-17T13:11:20: %SCRIPT-INFO: v16 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2021-02-17T13:11:20: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v16] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v26]           |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %SCRIPT-INFO: Checking the differences before/after for {'connected': 'v26'}.
2021-02-17T13:11:20: %SCRIPT-INFO: v26 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2021-02-17T13:11:20: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v26] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: The result of testcase CheckRoutes[protocol=connected] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |               Starting testcase CheckRoutes[protocol=internal]               |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |        Starting section check_routes_delta_before_after[vrf=default]         |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %SCRIPT-INFO: Checking the differences before/after for {'internal': 'default'}.
2021-02-17T13:11:20: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=default] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v16]           |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %SCRIPT-INFO: Checking the differences before/after for {'internal': 'v16'}.
2021-02-17T13:11:20: %SCRIPT-INFO: v16 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2021-02-17T13:11:20: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v16] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v26]           |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %SCRIPT-INFO: Checking the differences before/after for {'internal': 'v26'}.
2021-02-17T13:11:20: %SCRIPT-INFO: v26 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2021-02-17T13:11:20: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v26] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: The result of testcase CheckRoutes[protocol=internal] is => PASSED
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |                           Starting common cleanup                            |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:20: %AETEST-INFO: |                 Starting subsection disconnect_from_devices                  |
2021-02-17T13:11:20: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:26: %AETEST-INFO: The result of subsection disconnect_from_devices is => PASSED
2021-02-17T13:11:26: %AETEST-INFO: The result of common cleanup is => PASSED
2021-02-17T13:11:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:26: %AETEST-INFO: |                               Detailed Results                               |
2021-02-17T13:11:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:26: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
2021-02-17T13:11:26: %AETEST-INFO: --------------------------------------------------------------------------------
2021-02-17T13:11:26: %AETEST-INFO: .
2021-02-17T13:11:26: %AETEST-INFO: |-- common_setup                                                          PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   |-- check_testbed                                                     PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   |-- connect_to_devices                                                PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   `-- save_all_outputs_db                                               PASSED
2021-02-17T13:11:26: %AETEST-INFO: |-- CheckSaveDatabase                                                    ERRORED
2021-02-17T13:11:26: %AETEST-INFO: |   `-- all_outputs_copied_db                                            ERRORED
2021-02-17T13:11:26: %AETEST-INFO: |-- CheckOperData                                                         FAILED
2021-02-17T13:11:26: %AETEST-INFO: |   |-- check_os_current_version_device                                   FAILED
2021-02-17T13:11:26: %AETEST-INFO: |   |-- check_cpu_device                                                  PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   |-- check_isis_neighbors_differences                                  PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   `-- check_xconnect_differences                                        PASSED
2021-02-17T13:11:26: %AETEST-INFO: |-- CheckRoutes[protocol=bgp]                                             PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=default]                      PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=v16]                          PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   `-- check_routes_delta_before_after[vrf=v26]                          PASSED
2021-02-17T13:11:26: %AETEST-INFO: |-- CheckRoutes[protocol=isis]                                            PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=default]                      PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=v16]                          PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   `-- check_routes_delta_before_after[vrf=v26]                          PASSED
2021-02-17T13:11:26: %AETEST-INFO: |-- CheckRoutes[protocol=connected]                                       PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=default]                      PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=v16]                          PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   `-- check_routes_delta_before_after[vrf=v26]                          PASSED
2021-02-17T13:11:26: %AETEST-INFO: |-- CheckRoutes[protocol=internal]                                        PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=default]                      PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=v16]                          PASSED
2021-02-17T13:11:26: %AETEST-INFO: |   `-- check_routes_delta_before_after[vrf=v26]                          PASSED
2021-02-17T13:11:26: %AETEST-INFO: `-- common_cleanup                                                        PASSED
2021-02-17T13:11:26: %AETEST-INFO:     `-- disconnect_from_devices                                           PASSED
2021-02-17T13:11:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:26: %AETEST-INFO: |                                   Summary                                    |
2021-02-17T13:11:26: %AETEST-INFO: +------------------------------------------------------------------------------+
2021-02-17T13:11:26: %AETEST-INFO:  Number of ABORTED                                                            0 
2021-02-17T13:11:26: %AETEST-INFO:  Number of BLOCKED                                                            0 
2021-02-17T13:11:26: %AETEST-INFO:  Number of ERRORED                                                            1 
2021-02-17T13:11:26: %AETEST-INFO:  Number of FAILED                                                             1 
2021-02-17T13:11:26: %AETEST-INFO:  Number of PASSED                                                             6 
2021-02-17T13:11:26: %AETEST-INFO:  Number of PASSX                                                              0 
2021-02-17T13:11:26: %AETEST-INFO:  Number of SKIPPED                                                            0 
2021-02-17T13:11:26: %AETEST-INFO:  Total Number                                                                 8 
2021-02-17T13:11:26: %AETEST-INFO:  Success Rate                                                             75.0% 
2021-02-17T13:11:26: %AETEST-INFO: --------------------------------------------------------------------------------
2021-02-17T13:11:26: %SCRIPT-INFO: 
2021-02-17T13:11:26: %SCRIPT-INFO: 
2021-02-17T13:11:26: %SCRIPT-INFO: +----------+----------------+---------+-------+----------------+----------+------+------+-----------+----------+
2021-02-17T13:11:26: %SCRIPT-INFO: | hostname | connect_device | 16.12.4 | CPU % | isis_neighbors | xconnect | bgp  | isis | connected | internal |
2021-02-17T13:11:26: %SCRIPT-INFO: +----------+----------------+---------+-------+----------------+----------+------+------+-----------+----------+
2021-02-17T13:11:26: %SCRIPT-INFO: | ASR903_3 |      Pass      |   Fail  |   1   |      Pass      |   Pass   | Pass | Pass |    Pass   |   Pass   |
2021-02-17T13:11:26: %SCRIPT-INFO: | ASR903_4 |      Pass      |   Pass  |   2   |      Pass      |   Pass   | Pass | Pass |    Pass   |   Pass   |
2021-02-17T13:11:26: %SCRIPT-INFO: | ASR903_5 |      Pass      |   Fail  |   1   |      Pass      |   Pass   | Pass | Pass |    Pass   |   Pass   |
2021-02-17T13:11:26: %SCRIPT-INFO: | ASR903_6 |      Fail      |   Fail  |  Fail |      Fail      |   Fail   | Fail | Fail |    Fail   |   Fail   |
2021-02-17T13:11:26: %SCRIPT-INFO: +----------+----------------+---------+-------+----------------+----------+------+------+-----------+----------+
```