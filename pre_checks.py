# import the aetest module
from pyats import aetest
import logging
import toolbox.database as db
import toolbox.pyats_checks as check
from unicon.core.errors import ConnectionError

logger = logging.getLogger(__name__)

# Variables
when_tested = "before"
os_target_version = "16.10.1"
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
rommon_target_filenames = [
    "asr900-rommon.156-42r.S.pkg"
]
list_vrf = ["default", "v16", "v26"]
folder_images = {
    "new_os": "ImageTarget",
    "backup_os": "Image",
    "rommon": "Rommon"
}

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
                check.add_result_device(device, test_name, "Fail")
                logger.error(f"Could not connect to device {device.name}.")
        

    @aetest.subsection
    def save_all_outputs_db(self, testbed, current_time):

        logger.info("Saving outputs for each device.")

        # Only if I could connect to the device
        for device in (device for device in testbed if device.is_connected() == True):
            check.save_os_copied_db(device, os_target_filenames, rommon_target_filenames, folder_images, when_tested, current_time)
            check.save_os_current_version_db(device, when_tested, current_time)
            check.save_boot_system_db(device, folder_images, when_tested, current_time)
            check.save_route_summary_db(device, list_vrf, when_tested, current_time)
            check.save_routes_db(device, when_tested, current_time)
            check.save_isis_db(device, when_tested, current_time)
            check.save_xconnect_db(device, when_tested, current_time)
            check.save_cpu(device, when_tested, current_time)


class CheckSaveDatabase(aetest.Testcase):

    @aetest.test
    def all_outputs_copied_db(self, testbed):
        
        logger.info("Checking that all the outputs are saved in the DB for each device.")

        # Only if I could connect to the device
        for device in (device for device in testbed if device.is_connected() == True):
            outputs_list = db.get_list_outputs_device(device.name, when_tested, current_time)
            
            # If outputs not copied, ERROR, stopping the script (not doing the other tests)
            # 7 = os_copied, os_version, boot_system, route_summary, routes, isis, xconnect, cpu
            if len(outputs_list) != 8: self.errored(f"Output_lists has the wrong size. Expected 8, found {len(outputs_list)}")


class CheckOperData(aetest.Testcase):

    @aetest.test
    def check_os_copied_device(self, testbed):

        test_name = "os_copied"
        testbed.tests_run.append(test_name)
        logger.info("Checking that the OS is copied on each device bootflash:/")
        
        not_compliant = []

        for device in testbed:

            # If I couldn't connect to the device, this test auto fails
            if device.test_results['connect_device'] == "Fail":
                check.add_result_device(device, test_name, "Fail")
            
            # Else, let's get the data and test
            if device.test_results['connect_device'] == "Pass":

                # Assume the test Pass
                check.add_result_device(device, test_name, "Pass")
            
                # If OS is not copied, add its name to the list
                if check.os_copied(device.name, os_target_filenames, when_tested) != "True": 
                    not_compliant.append(device.name)
                    check.add_result_device(device, test_name, "Fail")
                    logger.error(f"OS files are missing on {device.name}.")

                if device.number_rsp == 2:
                    logger.info(f"{device.name} has 2 RSP.")

        if len(not_compliant) != 0: self.failed(("OS files are not copied on the above devices,\n"
                                                "not in the right folder, or folder doesn't exist.\n"
                                                "If device has 2 RSP, check the standby-bootflash."))

    @aetest.test
    def check_boot_system_order(self, testbed):

        test_name = "boot_system"
        testbed.tests_run.append(test_name)
        logger.info("Checking that the `boot system bootflash:/...` lines are present and in the correct order")
        
        not_compliant = []

        for device in testbed:

            # If I couldn't connect to the device, this test auto fails
            if device.test_results['connect_device'] == "Fail":
                check.add_result_device(device, test_name, "Fail")
            
            # Else, let's get the data and test
            if device.test_results['connect_device'] == "Pass":

                # Assume the test Pass
                check.add_result_device(device, test_name, "Pass")
            
                # If OS is not copied, add its name to the list
                if check.boot_system(device.name, when_tested) != "True": 
                    not_compliant.append(device.name)
                    check.add_result_device(device, test_name, "Fail")
                    logger.error(f"`boot system bootflash:/...` command missing on {device.name}")

        if len(not_compliant) != 0: self.failed(("`boot system bootflash:/...` missing, not in the right order or\n"
                                                "not pointing to the right folder on the devices above."))

    @aetest.test
    def check_os_current_version_device(self, testbed):

        test_name = os_target_version
        testbed.tests_run.append(test_name)
        logger.info(f"Checking that each device is using {os_target_version}")

        not_compliant = []

        for device in testbed:

            # If I couldn't connect to the device, this test auto fails
            if device.test_results['connect_device'] == "Fail":
                check.add_result_device(device, test_name, "Fail")
            
            # Else, let's get the data and test
            if device.test_results['connect_device'] == "Pass":

                os_version = check.os_version(device.name, when_tested)
                check.add_result_device(device, test_name, "Pass")

                # If OS version on the device is wrong, add it to the list
                if os_version != os_target_version: 
                    not_compliant.append(device.name)
                    check.add_result_device(device, test_name, "Fail")
                    logger.error(f"{device.name} is not using {os_target_version}. Using {os_version}")

        if len(not_compliant) != 0: self.failed(f"The above devices are not using {os_target_version}.")


    @aetest.test
    def check_cpu_device(self, testbed):

        test_name = "CPU %"
        testbed.tests_run.append(test_name)
        logger.info(f"Checking the CPU utilisation on the device for the last 5 minutes.")

        not_compliant = []

        for device in testbed:

            # If I couldn't connect to the device, this test auto fails
            if device.test_results['connect_device'] == "Fail":
                check.add_result_device(device, test_name, "Fail")
            
            # Else, let's get the data and test
            if device.test_results['connect_device'] == "Pass":

                # converting str to int
                cpu = int(check.cpu(device.name, when_tested))
                check.add_result_device(device, test_name, cpu)

                # CPU utilisation above 70% => NOK
                if cpu >= 70: 
                    not_compliant.append(device.name)
                    logger.error(f"{device.name} CPU is {cpu}.")

        if len(not_compliant) != 0: self.failed(f"The above devices CPU utilisation is above 70%.")


class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        for device in testbed:

            # Only disconnect if we are connected to the device
            if device.is_connected() == True:
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
    parser.add_argument('--testbed', dest='testbed', help = '/link/to/testbed.yaml', required = True)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    testbed = load(args.testbed)

    # List of tests_run
    testbed.tests_run = []

    aetest.main(testbed = testbed, current_time = current_time)

    # Adding two blank lines for formatting
    logger.info("")
    logger.info("")
    logger.info(check.table_results(testbed))