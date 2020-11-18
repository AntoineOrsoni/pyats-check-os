# import the aetest module
from pyats import aetest
import logging
import toolbox.database as db
import toolbox.pyats_checks as check

logger = logging.getLogger(__name__)

# Variables
os_target_filename = 'asr900rsp3-universalk9_npe.16.12.04.SPA.bin'
when_tested = "after"
os_target_version = "16.12.4"

# Delta
isis_neighbors_delta = 0.8    # They have to be [80%-100%] similar
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
                logger.info('  - {device}'.format(device=device))

    @aetest.subsection
    def connect_to_devices(self, testbed):

        logger.info("Verifying that I can connect to each device.")

        for device in testbed:
            # don't do the default show version
            # don't do the default config
            device.connect(init_exec_commands=[],
                           init_config_commands=[],
                           log_stdout=False)
        

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
            outputs_list = db.get_list_outputs_device(device.name, when_tested)
            
            # 6 = os_copied, os_version, route_summary, routes, isis, xconnect
            assert len(outputs_list) == 6, logger.info(f"len(outputs_list ={str(len(outputs_list))}")


class CheckOperData(aetest.Testcase):

    @aetest.test
    def check_os_current_version_device(self, testbed):

        logger.info(f"Checking that each device is using {os_target_version}")

        not_compliant = []

        for device in testbed:
            os_version = check.os_version(device.name, when_tested)

            # If OS version on the device is wrong, add it to the list
            if os_version != os_target_version: 
                not_compliant.append(device.name)
                logger.info(f"{device.name} is not using {os_target_version}. Using {os_version}")

        assert len(not_compliant) == 0, f"The above devices are not using {os_target_version}."

    # - route_summary > JSON
    # - routes        > JSON
    # - isis          > JSON
    # - xconnect      > JSON
    # - os_version    > string
    # - os_copied     > boolean

    @aetest.test
    def check_isis_differences(self, testbed):

        test_name = "isis"
        logger.info(f"Checking the differences before/after for {test_name}.")

        not_compliant = []

        for device in testbed:
            neighbors_number = check.get_isis_before_after(device.name)

            # If we have less than 80% similarity in one way OR another, something is wrong
            if (neighbors_number[0] < neighbors_number[1] * isis_neighbors_delta) or (neighbors_number[1] < neighbors_number[0] * isis_neighbors_delta):
                not_compliant.append(device.name)
                logger.info(f"{device.name} number of isis neighbors is less than {isis_neighbors_delta*100}% similar before/after.")                    

        assert len(not_compliant) == 0, f"The above devices have a number of isis neighbors exceeding the threshold."

    @aetest.test
    def check_xconnect_differences(self, testbed):
        pass


class CheckRoutesBgp(aetest.Testcase):

    @aetest.test
    def check_routes_bgp_default(self, testbed):

        test_name = "routes_summary"
        logger.info(f"Checking the differences before/after for {test_name}.")

        protocol = "bgp"
        vrf = "default"
        not_compliant_before = []
        not_compliant_after = []
        not_compliant_delta = []  

        for device in testbed:

            # Does the VRF exist in the `show ip route summary`? If not, add its name to the not_compliant list
            vrf_exists = check.vrf_exists(device.name, vrf)
            if (vrf_exists[0] == False): 
                not_compliant_before.append(device.name)
                logger.info(f"{device.name} does not have VRF {vrf} in the pre_check.")
            if (vrf_exists[0] == False): 
                not_compliant_after.append(device.name)
                logger.info(f"{device.name} does not have VRF {vrf} in the post_check.")

            # If the VRF exists in both, I can compare
            if (vrf_exists[0] == True) and (vrf_exists[1] == True):
                routes_number = check.get_routes_before_after(device.name, protocol, vrf)

                # If we have less than 80% similarity in one way OR another, something is wrong
                if (routes_number[0] < routes_number[1] * routes_delta) or (routes_number[1] < routes_number[0] * routes_delta):
                    not_compliant_delta.append(device.name)
                    logger.info(f"{device.name} number of {protocol} routes for VRF {vrf} is less than {routes_delta*100}% similar before/after.")                    

            if len(not_compliant_before) + len(not_compliant_after) + len(not_compliant_delta) != 0:
                self.failed(f"Test failed. VRF missing or too many routes difference ({routes_delta*100}%). See logs above.")


    @aetest.test
    def check_routes_bgp_sfr(self, testbed):
        
        test_name = "routes_summary"
        logger.info(f"Checking the differences before/after for {test_name}.")

        protocol = "bgp"
        vrf = "Mcast-SFR"
        not_compliant_before = []
        not_compliant_after = []
        not_compliant_delta = []  

        for device in testbed:

            # Does the VRF exist in the `show ip route summary`? If not, add its name to the not_compliant list
            vrf_exists = check.vrf_exists(device.name, vrf)
            if (vrf_exists[0] == False): 
                not_compliant_before.append(device.name)
                logger.info(f"{device.name} does not have VRF {vrf} in the pre_check.")
            if (vrf_exists[0] == False): 
                not_compliant_after.append(device.name)
                logger.info(f"{device.name} does not have VRF {vrf} in the post_check.")

            # If the VRF exists in both, I can compare
            if (vrf_exists[0] == True) and (vrf_exists[1] == True):
                routes_number = check.get_routes_before_after(device.name, protocol, vrf)

                # If we have less than 80% similarity in one way OR another, something is wrong
                if (routes_number[0] < routes_number[1] * routes_delta) or (routes_number[1] < routes_number[0] * routes_delta):
                    not_compliant_delta.append(device.name)
                    logger.info(f"{device.name} number of {protocol} routes for VRF {vrf} is less than {routes_delta*100}% similar before/after.")                    

            if len(not_compliant_before) + len(not_compliant_after) + len(not_compliant_delta) != 0:
                self.failed(f"Test failed. VRF missing or too many routes difference ({routes_delta*100}%). See logs above.")


    @aetest.test
    def check_routes_bgp_bytel(self, testbed):
        
        test_name = "routes_summary"
        logger.info(f"Checking the differences before/after for {test_name}.")

        protocol = "bgp"
        vrf = "Bytel"
        not_compliant_before = []
        not_compliant_after = []
        not_compliant_delta = []  

        for device in testbed:

            # Does the VRF exist in the `show ip route summary`? If not, add its name to the not_compliant list
            vrf_exists = check.vrf_exists(device.name, vrf)
            if (vrf_exists[0] == False): 
                not_compliant_before.append(device.name)
                logger.info(f"{device.name} does not have VRF {vrf} in the pre_check.")
            if (vrf_exists[0] == False): 
                not_compliant_after.append(device.name)
                logger.info(f"{device.name} does not have VRF {vrf} in the post_check.")

            # If the VRF exists in both, I can compare
            if (vrf_exists[0] == True) and (vrf_exists[1] == True):
                routes_number = check.get_routes_before_after(device.name, protocol, vrf)

                # If we have less than 80% similarity in one way OR another, something is wrong
                if (routes_number[0] < routes_number[1] * routes_delta) or (routes_number[1] < routes_number[0] * routes_delta):
                    not_compliant_delta.append(device.name)
                    logger.info(f"{device.name} number of {protocol} routes for VRF {vrf} is less than {routes_delta*100}% similar before/after.")                    

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

    aetest.main(testbed = testbed, current_time = current_time)