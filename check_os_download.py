# import the aetest module
from pyats import aetest
import logging

logger = logging.getLogger(__name__)

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

class TestCase(aetest.Testcase):

    @aetest.test
    def check_os_flash(self, testbed):

        for device in testbed:
            
            os_download = False

            # Checking all the files in the bootflash
            files = device.parse('dir')
            os_target = 'csr1000v-mono-universalk9.16.09.04.SPA.pkg'

            for file in files['dir']['bootflash:/']['files']:

                if file == os_target: os_download = True

            if os_download == True:
                logger.info('{os} is successfuly copied on the following devices:'.format(os=os_target)) 
                logger.info('  - {device}'.format(device=str(device.alias)))
            
            else:
                logger.info('{os} is not copied on the following devices:'.format(os=os_target)) 
                logger.info('  - {device}'.format(device=str(device.alias)))

            assert os_download == True

    @aetest.test
    def check_current_version(self, testbed):

        for device in testbed:
            
            # Checking the current version of the device
            os_version_installed = device.parse('show version')['version']['version']
            
            if os_version_installed == '16.9.4':
                logger.info('List of devices with 16.9.4:')
                logger.info('  - {device}'.format(device=str(device.alias)))
            else:
                logger.info('List of devices with the wrong image:')
                logger.info('{device} OS version is: {version}'.format(device=device.alias, version=os_version_installed))

            assert os_version_installed == '16.9.4'

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

    # set debug level DEBUG, INFO, WARNING
    logger.setLevel(logging.INFO)

    # testbed = load('/home/cisco/pyats/test_pyats/testbed.yaml')

    # Parsing the args
    parser = argparse.ArgumentParser(description='Process the testbed.')
    parser.add_argument('--testbed', dest='testbed', default='/home/cisco/pyats/test_pyats/testbed.yaml', help = '/link/to/testbed.yaml')
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    testbed = load(args.testbed)

    aetest.main(testbed = testbed)

