# import the aetest module
from pyats import aetest
import logging
import toolbox.database as db
import toolbox.pyats_checks as check

logger = logging.getLogger(__name__)

# Variables
os_target = 'asr900rsp3-universalk9_npe.16.12.04.SPA.bin'
when_tested = "before"

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
        
        for device in testbed:
            # don't do the default show version
            # don't do the default config
            device.connect(init_exec_commands=[],
                           init_config_commands=[],
                           log_stdout=False)

    @aetest.subsection
    def save_all_outputs_db(self, testbed, current_time):

        for device in testbed:
            check.save_os_copied_db(device, os_target, when_tested, current_time)
            check.save_os_current_version_db(device, when_tested, current_time)
            check.save_route_summary_db(device, when_tested, current_time)
            check.save_routes_db(device, when_tested, current_time)
            check.save_isis_db(device, when_tested, current_time)
            check.save_xconnect_db(device, when_tested, current_time)


class OsCopied(aetest.Testcase):

    @aetest.test
    def save_outputs_copied_db(self, testbed):
        pass


    @aetest.test
    def check_os_copied(self, testbed):
        pass


    @aetest.test
    def check_current_version(self, testbed):
        pass


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