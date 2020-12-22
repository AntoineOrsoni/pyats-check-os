```
2020-12-22T09:50:44: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:50:44: %AETEST-INFO: |                            Starting common setup                             |
2020-12-22T09:50:44: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:50:44: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:50:44: %AETEST-INFO: |                      Starting subsection check_testbed                       |
2020-12-22T09:50:44: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:50:44: %SCRIPT-INFO: List of Devices:
2020-12-22T09:50:44: %SCRIPT-INFO:   - ASR903_3
2020-12-22T09:50:44: %SCRIPT-INFO:   - ASR903_4
2020-12-22T09:50:44: %SCRIPT-INFO:   - ASR903_5
2020-12-22T09:50:44: %SCRIPT-INFO:   - ASR903_6
2020-12-22T09:50:44: %AETEST-INFO: The result of subsection check_testbed is => PASSED
2020-12-22T09:50:44: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:50:44: %AETEST-INFO: |                    Starting subsection connect_to_devices                    |
2020-12-22T09:50:44: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:50:44: %SCRIPT-INFO: Verifying that I can connect to each device.
2020-12-22T09:51:06: %SCRIPT-ERROR: Could not connect to device ASR903_6.
2020-12-22T09:51:06: %AETEST-INFO: The result of subsection connect_to_devices is => PASSED
2020-12-22T09:51:06: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:06: %AETEST-INFO: |                   Starting subsection save_all_outputs_db                    |
2020-12-22T09:51:06: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:06: %SCRIPT-INFO: Saving outputs for each device.
2020-12-22T09:51:14: %AETEST-INFO: The result of subsection save_all_outputs_db is => PASSED
2020-12-22T09:51:14: %AETEST-INFO: The result of common setup is => PASSED
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |                     Starting testcase CheckSaveDatabase                      |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |                    Starting section all_outputs_copied_db                    |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %SCRIPT-INFO: Checking that all the outputs are saved in the DB for each device.
2020-12-22T09:51:14: %AETEST-INFO: The result of section all_outputs_copied_db is => PASSED
2020-12-22T09:51:14: %AETEST-INFO: The result of testcase CheckSaveDatabase is => PASSED
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |                       Starting testcase CheckOperData                        |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |               Starting section check_os_current_version_device               |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %SCRIPT-INFO: Checking that each device is using 16.12.4
2020-12-22T09:51:14: %AETEST-INFO: The result of section check_os_current_version_device is => PASSED
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |              Starting section check_isis_neighbors_differences               |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %SCRIPT-INFO: Checking the differences before/after for isis_neighbors.
2020-12-22T09:51:14: %AETEST-INFO: The result of section check_isis_neighbors_differences is => PASSED
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |                 Starting section check_xconnect_differences                  |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %SCRIPT-INFO: Checking the differences before/after for xconnect.
2020-12-22T09:51:14: %SCRIPT-ERROR: ASR903_3 number of xconnect UP is less than 80.0% similar before/after.
2020-12-22T09:51:14: %AETEST-ERROR: Failed reason: The above devices have a number of xconnect UP exceeding the threshold.
2020-12-22T09:51:14: %AETEST-INFO: The result of section check_xconnect_differences is => FAILED
2020-12-22T09:51:14: %AETEST-INFO: The result of testcase CheckOperData is => FAILED
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |                 Starting testcase CheckRoutes[protocol=bgp]                  |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |        Starting section check_routes_delta_before_after[vrf=default]         |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %SCRIPT-INFO: Checking the differences before/after for {'bgp': 'default'}.
2020-12-22T09:51:14: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=default] is => PASSED
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v16]           |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %SCRIPT-INFO: Checking the differences before/after for {'bgp': 'v16'}.
2020-12-22T09:51:14: %SCRIPT-INFO: v16 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2020-12-22T09:51:14: %SCRIPT-ERROR: ASR903_4 number of bgp routes for VRF v16 is less than 80.0% similar before/after.
2020-12-22T09:51:14: %SCRIPT-ERROR: ASR903_5 number of bgp routes for VRF v16 is less than 80.0% similar before/after.
2020-12-22T09:51:14: %AETEST-ERROR: Failed reason: Test failed. VRF missing or too many routes difference (80.0%). See logs above.
2020-12-22T09:51:14: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v16] is => FAILED
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v26]           |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %SCRIPT-INFO: Checking the differences before/after for {'bgp': 'v26'}.
2020-12-22T09:51:14: %SCRIPT-INFO: v26 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2020-12-22T09:51:14: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v26] is => PASSED
2020-12-22T09:51:14: %AETEST-INFO: The result of testcase CheckRoutes[protocol=bgp] is => FAILED
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |                 Starting testcase CheckRoutes[protocol=isis]                 |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |        Starting section check_routes_delta_before_after[vrf=default]         |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %SCRIPT-INFO: Checking the differences before/after for {'isis': 'default'}.
2020-12-22T09:51:14: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=default] is => PASSED
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v16]           |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %SCRIPT-INFO: Checking the differences before/after for {'isis': 'v16'}.
2020-12-22T09:51:14: %SCRIPT-INFO: v16 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2020-12-22T09:51:14: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v16] is => PASSED
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v26]           |
2020-12-22T09:51:14: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:14: %SCRIPT-INFO: Checking the differences before/after for {'isis': 'v26'}.
2020-12-22T09:51:14: %SCRIPT-INFO: v26 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2020-12-22T09:51:15: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v26] is => PASSED
2020-12-22T09:51:15: %AETEST-INFO: The result of testcase CheckRoutes[protocol=isis] is => PASSED
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %AETEST-INFO: |              Starting testcase CheckRoutes[protocol=connected]               |
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %AETEST-INFO: |        Starting section check_routes_delta_before_after[vrf=default]         |
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %SCRIPT-INFO: Checking the differences before/after for {'connected': 'default'}.
2020-12-22T09:51:15: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=default] is => PASSED
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v16]           |
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %SCRIPT-INFO: Checking the differences before/after for {'connected': 'v16'}.
2020-12-22T09:51:15: %SCRIPT-INFO: v16 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2020-12-22T09:51:15: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v16] is => PASSED
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v26]           |
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %SCRIPT-INFO: Checking the differences before/after for {'connected': 'v26'}.
2020-12-22T09:51:15: %SCRIPT-INFO: v26 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2020-12-22T09:51:15: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v26] is => PASSED
2020-12-22T09:51:15: %AETEST-INFO: The result of testcase CheckRoutes[protocol=connected] is => PASSED
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %AETEST-INFO: |               Starting testcase CheckRoutes[protocol=internal]               |
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %AETEST-INFO: |        Starting section check_routes_delta_before_after[vrf=default]         |
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %SCRIPT-INFO: Checking the differences before/after for {'internal': 'default'}.
2020-12-22T09:51:15: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=default] is => PASSED
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v16]           |
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %SCRIPT-INFO: Checking the differences before/after for {'internal': 'v16'}.
2020-12-22T09:51:15: %SCRIPT-INFO: v16 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2020-12-22T09:51:15: %SCRIPT-ERROR: ASR903_4 number of internal routes for VRF v16 is less than 80.0% similar before/after.
2020-12-22T09:51:15: %SCRIPT-ERROR: ASR903_5 number of internal routes for VRF v16 is less than 80.0% similar before/after.
2020-12-22T09:51:15: %AETEST-ERROR: Failed reason: Test failed. VRF missing or too many routes difference (80.0%). See logs above.
2020-12-22T09:51:15: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v16] is => FAILED
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %AETEST-INFO: |          Starting section check_routes_delta_before_after[vrf=v26]           |
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %SCRIPT-INFO: Checking the differences before/after for {'internal': 'v26'}.
2020-12-22T09:51:15: %SCRIPT-INFO: v26 doesn't exist on ASR903_3, and did not exist in the pre_checks.
2020-12-22T09:51:15: %AETEST-INFO: The result of section check_routes_delta_before_after[vrf=v26] is => PASSED
2020-12-22T09:51:15: %AETEST-INFO: The result of testcase CheckRoutes[protocol=internal] is => FAILED
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %AETEST-INFO: |                           Starting common cleanup                            |
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:15: %AETEST-INFO: |                 Starting subsection disconnect_from_devices                  |
2020-12-22T09:51:15: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:54: %AETEST-INFO: The result of subsection disconnect_from_devices is => PASSED
2020-12-22T09:51:54: %AETEST-INFO: The result of common cleanup is => PASSED
2020-12-22T09:51:54: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:54: %AETEST-INFO: |                               Detailed Results                               |
2020-12-22T09:51:54: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:54: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
2020-12-22T09:51:54: %AETEST-INFO: --------------------------------------------------------------------------------
2020-12-22T09:51:54: %AETEST-INFO: .
2020-12-22T09:51:54: %AETEST-INFO: |-- common_setup                                                          PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   |-- check_testbed                                                     PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   |-- connect_to_devices                                                PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   `-- save_all_outputs_db                                               PASSED
2020-12-22T09:51:54: %AETEST-INFO: |-- CheckSaveDatabase                                                     PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   `-- all_outputs_copied_db                                             PASSED
2020-12-22T09:51:54: %AETEST-INFO: |-- CheckOperData                                                         FAILED
2020-12-22T09:51:54: %AETEST-INFO: |   |-- check_os_current_version_device                                   PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   |-- check_isis_neighbors_differences                                  PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   `-- check_xconnect_differences                                        FAILED
2020-12-22T09:51:54: %AETEST-INFO: |-- CheckRoutes[protocol=bgp]                                             FAILED
2020-12-22T09:51:54: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=default]                      PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=v16]                          FAILED
2020-12-22T09:51:54: %AETEST-INFO: |   `-- check_routes_delta_before_after[vrf=v26]                          PASSED
2020-12-22T09:51:54: %AETEST-INFO: |-- CheckRoutes[protocol=isis]                                            PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=default]                      PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=v16]                          PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   `-- check_routes_delta_before_after[vrf=v26]                          PASSED
2020-12-22T09:51:54: %AETEST-INFO: |-- CheckRoutes[protocol=connected]                                       PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=default]                      PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=v16]                          PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   `-- check_routes_delta_before_after[vrf=v26]                          PASSED
2020-12-22T09:51:54: %AETEST-INFO: |-- CheckRoutes[protocol=internal]                                        FAILED
2020-12-22T09:51:54: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=default]                      PASSED
2020-12-22T09:51:54: %AETEST-INFO: |   |-- check_routes_delta_before_after[vrf=v16]                          FAILED
2020-12-22T09:51:54: %AETEST-INFO: |   `-- check_routes_delta_before_after[vrf=v26]                          PASSED
2020-12-22T09:51:54: %AETEST-INFO: `-- common_cleanup                                                        PASSED
2020-12-22T09:51:54: %AETEST-INFO:     `-- disconnect_from_devices                                           PASSED
2020-12-22T09:51:54: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:54: %AETEST-INFO: |                                   Summary                                    |
2020-12-22T09:51:54: %AETEST-INFO: +------------------------------------------------------------------------------+
2020-12-22T09:51:54: %AETEST-INFO:  Number of ABORTED                                                            0 
2020-12-22T09:51:54: %AETEST-INFO:  Number of BLOCKED                                                            0 
2020-12-22T09:51:54: %AETEST-INFO:  Number of ERRORED                                                            0 
2020-12-22T09:51:54: %AETEST-INFO:  Number of FAILED                                                             3 
2020-12-22T09:51:54: %AETEST-INFO:  Number of PASSED                                                             5 
2020-12-22T09:51:54: %AETEST-INFO:  Number of PASSX                                                              0 
2020-12-22T09:51:54: %AETEST-INFO:  Number of SKIPPED                                                            0 
2020-12-22T09:51:54: %AETEST-INFO:  Total Number                                                                 8 
2020-12-22T09:51:54: %AETEST-INFO:  Success Rate                                                             62.5% 
2020-12-22T09:51:54: %AETEST-INFO: --------------------------------------------------------------------------------
2020-12-22T09:51:54: %SCRIPT-INFO: 
2020-12-22T09:51:54: %SCRIPT-INFO: 
2020-12-22T09:51:54: %SCRIPT-INFO: +----------+----------------+---------+----------------+----------+------+------+-----------+----------+
2020-12-22T09:51:54: %SCRIPT-INFO: | hostname | connect_device | 16.12.4 | isis_neighbors | xconnect | bgp  | isis | connected | internal |
2020-12-22T09:51:54: %SCRIPT-INFO: +----------+----------------+---------+----------------+----------+------+------+-----------+----------+
2020-12-22T09:51:54: %SCRIPT-INFO: | ASR903_3 |      Pass      |   Pass  |      Pass      |   Fail   | Pass | Pass |    Pass   |   Pass   |
2020-12-22T09:51:54: %SCRIPT-INFO: | ASR903_4 |      Pass      |   Pass  |      Pass      |   Pass   | Fail | Pass |    Pass   |   Fail   |
2020-12-22T09:51:54: %SCRIPT-INFO: | ASR903_5 |      Pass      |   Pass  |      Pass      |   Pass   | Fail | Pass |    Pass   |   Fail   |
2020-12-22T09:51:54: %SCRIPT-INFO: | ASR903_6 |      Fail      |   Fail  |      Fail      |   Fail   | Fail | Fail |    Fail   |   Fail   |
2020-12-22T09:51:54: %SCRIPT-INFO: +----------+----------------+---------+----------------+----------+------+------+-----------+----------+
```