# import the aetest module
from pyats import aetest
import logging
import toolbox.database as db
import toolbox.pyats_checks as check

logger = logging.getLogger(__name__)

# Variables
os_target_filename = 'asr900rsp3-universalk9_npe.16.12.04.SPA.bin'
when_tested = "before"
os_target_version = "16.10.1"

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
    def check_os_copied_device(self, testbed):

        logger.info("Checking that the OS is copied on each device bootflash:/")
        
        not_compliant = []

        for device in testbed:
            # If OS is not copied, add its name to the list
            if check.os_copied(device.name, os_target_filename, when_tested) != "True": 
                not_compliant.append(device.name)
                logger.info(f"{os_target_filename} is not copied on {device.name}.")

        assert len(not_compliant) == 0, "OS is not copied on the above devices"

    @aetest.test
    def check_os_current_version_device(self, testbed):

        logger.info("Checking that each device is using 16.10.1")

        not_compliant = []

        for device in testbed:
            os_version = check.os_version(device.name, when_tested)

            # If OS version on the device is wrong, add it to the list
            if os_version != os_target_version: 
                not_compliant.append(device.name)
                logger.info(f"{device.name} is not using {os_target_version}. Using {os_version}")

        assert len(not_compliant) == 0, f"The above devices are not using {os_target_version}."


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