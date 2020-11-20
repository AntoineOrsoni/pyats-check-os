# import the aetest module
from pyats import aetest
import logging
import toolbox.database as db
import toolbox.pyats_checks as check
from unicon.core.errors import ConnectionError

logger = logging.getLogger(__name__)

# Variables
os_target_filename = 'asr900rsp3-universalk9_npe.16.12.04.SPA.bin'
when_tested = "after"
os_target_version = "16.12.4"

# Delta
isis_neighbors_delta = 0.8    # They have to be [80%-100%] similar
xconnect_delta = 0.8
routes_delta = 0.8


class CommonSetup(aetest.CommonSetup):
    
    # Checking testbed info
    @aetest.subsection
    def check_testbed(self, testbed):

        if len(testbed.devices) == 0: 
            self.failed('{testbed} is empty'.format(testbed=str(testbed)))
        
        else:
            # Listing the devices
            logger.info('List of Devices:')
            for device in testbed.devices:
                logger.info(f'  - {device}')


    @aetest.subsection
    def connect_to_devices(self, testbed):

        logger.info("Verifying that I can connect to each device.")
        test_name = "connect_device"
        testbed.tests_run.append(test_name)

        not_compliant = []

        for device in testbed:

            # Tracking each device.test_result
            device.test_results = {}

            # Try if I can connect to the device.
            try:
                device.connect( init_exec_commands=[],
                                init_config_commands=[],
                                log_stdout=False) 
                check.add_result_device(device, test_name, "Pass")

            except ConnectionError as e:
                not_compliant.append(device.name)
                check.add_result_device(device, test_name, "Fail")
                logger.error(f"Could not connect to device {device.name}.")

        if len(not_compliant) != 0: 

            # Removing the devices from the testbed, if I can't connect
            for device_name in not_compliant:
                
                testbed.devices.pop(device_name)
                logger.error(f"{device_name} has been removed from the testbed.")


    @aetest.subsection
    def save_all_outputs_db(self, testbed, current_time):

        logger.info("Saving outputs for each device.")

        for device in testbed:
            check.save_os_copied_db(device, os_target_filename, when_tested, current_time)
            check.save_os_current_version_db(device, when_tested, current_time)
            check.save_route_summary_db(device, when_tested, current_time)
            check.save_routes_db(device, when_tested, current_time)
            check.save_isis_db(device, when_tested, current_time)
            check.save_xconnect_db(device, when_tested, current_time)


class CheckSaveDatabase(aetest.Testcase):

    @aetest.test
    def all_outputs_copied_db(self, testbed):
        
        logger.info("Checking that all the outputs are saved in the DB for each device.")
        
        for device in testbed:
            outputs_list = db.get_list_outputs_device(device.name, when_tested, current_time)

            # If outputs not copied, ERROR, stopping the script (not doing the other tests)
            # 6 = os_copied, os_version, route_summary, routes, isis, xconnect
            if len(outputs_list) != 6: self.errored(f"output_lists has the wrong size. Expected 6, found {len(outputs_list)}")


class CheckOperData(aetest.Testcase):

    @aetest.test
    def check_os_current_version_device(self, testbed):

        test_name = os_target_version
        testbed.tests_run.append(test_name)
        logger.info(f"Checking that each device is using {os_target_version}")

        not_compliant = []

        for device in testbed:
            os_version = check.os_version(device.name, when_tested)
            check.add_result_device(device, test_name, "Pass")

            # If OS version on the device is wrong, add it to the list
            if os_version != os_target_version: 
                not_compliant.append(device.name)
                check.add_result_device(device, test_name, "Fail")
                logger.info(f"{device.name} is not using {os_target_version}. Using {os_version}")

        if len(not_compliant) != 0: self.failed(f"The above devices are not using {os_target_version}.")


    @aetest.test
    def check_isis_neighbors_differences(self, testbed):

        test_name = "isis_neighbors"
        testbed.tests_run.append(test_name)
        logger.info(f"Checking the differences before/after for {test_name}.")

        not_compliant = []

        for device in testbed:
            neighbors_number = check.get_isis_before_after(device.name)
            check.add_result_device(device, test_name, "Pass")

            # If we have less than 80% similarity in one way OR another, something is wrong
            if (neighbors_number[0] < neighbors_number[1] * isis_neighbors_delta) or (neighbors_number[1] < neighbors_number[0] * isis_neighbors_delta):
                not_compliant.append(device.name)
                check.add_result_device(device, test_name, "Fail")
                logger.info(f"{device.name} number of isis neighbors is less than {isis_neighbors_delta*100}% similar before/after.")                    

        if len(not_compliant) != 0: self.failed(f"The above devices have a number of isis neighbors exceeding the threshold.")


    @aetest.test
    def check_xconnect_differences(self, testbed):
        
        test_name = "xconnect"
        testbed.tests_run.append(test_name)
        logger.info(f"Checking the differences before/after for {test_name}.")

        not_compliant = []

        for device in testbed:
            xconnect_number = check.get_xconnect_before_after(device.name)
            check.add_result_device(device, test_name, "Pass")

            # If we have less than 80% similarity in one way OR another, something is wrong
            if (xconnect_number[0] < xconnect_number[1] * xconnect_delta) or (xconnect_number[1] < xconnect_number[0] * xconnect_delta):
                not_compliant.append(device.name)
                check.add_result_device(device, test_name, "Fail")
                logger.info(f"{device.name} number of xconnect UP is less than {xconnect_delta*100}% similar before/after.")                    

        if len(not_compliant) != 0: self.failed(f"The above devices have a number of xconnect UP exceeding the threshold.")


@aetest.loop(protocol = ["bgp", "isis", "connected", "internal"])
class CheckRoutes(aetest.Testcase):

    @aetest.test.loop(vrf=["default", "Bytel", "Mcast-SFR"])
    def check_routes_delta_before_after(self, testbed, protocol, vrf):

        # test_name is a dict
        test_name = {protocol: vrf}
        testbed.tests_run.append(test_name)
        logger.info(f"Checking the differences before/after for {test_name}.")

        not_compliant_before = []
        not_compliant_after = []
        not_compliant_delta = []  

        for device in testbed:

            check.add_result_device(device, test_name, "Pass")

            # Does the VRF exist in the `show ip route summary`? If not, add its name to the not_compliant list
            vrf_exists = check.vrf_exists(device.name, vrf)
            if (vrf_exists[0] == False): 
                not_compliant_before.append(device.name)
                check.add_result_device(device, test_name, "Fail")
                logger.error(f"{device.name} does not have VRF {vrf} in the pre_check.")
            if (vrf_exists[1] == False): 
                not_compliant_after.append(device.name)
                check.add_result_device(device, test_name, "Fail")
                logger.error(f"{device.name} does not have VRF {vrf} in the post_check.")

            # If the VRF exists in both, I can compare
            if (vrf_exists[0] == True) and (vrf_exists[1] == True):
                routes_number = check.get_routes_before_after(device.name, protocol, vrf)

                # If we have less than 80% similarity in one way OR another, something is wrong
                if (routes_number[0] < routes_number[1] * routes_delta) or (routes_number[1] < routes_number[0] * routes_delta):
                    not_compliant_delta.append(device.name)
                    # check.add_result_device(device, test_name, "Fail")
                    logger.error(f"{device.name} number of {protocol} routes for VRF {vrf} is less than {routes_delta*100}% similar before/after.")                    

        if len(not_compliant_before) + len(not_compliant_after) + len(not_compliant_delta) != 0:
            self.failed(f"Test failed. VRF missing or too many routes difference ({routes_delta*100}%). See logs above.")


class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        for device in testbed:
            device.disconnect()


if __name__ == '__main__':

    # local imports
    from genie.testbed import load
    import argparse
    import sys
    import time

    # set debug level DEBUG, INFO, WARNING
    logger.setLevel(logging.INFO)

    # Getting the current_time before the test
    t = time.localtime()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

    # Parsing the args
    parser = argparse.ArgumentParser(description='Process the testbed.')
    parser.add_argument('--testbed', dest='testbed', default='/home/anorsoni/Projets/2020-CAP-Altitude/pyats-check-os/testbed.yaml', help = '/link/to/testbed.yaml')
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    ## TODO verify arguments has been given

    testbed = load(args.testbed)
    
    # List of tests_run
    testbed.tests_run = []

    aetest.main(testbed = testbed, current_time = current_time)

    print("end")