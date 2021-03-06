from genie.testbed import load
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError
import toolbox.database as db
import json
from prettytable import PrettyTable

###
### CHECKING
###

# Returns True if the target OS is copied on the device, else False
def os_copied(hostname, os_target, when_tested):

    # Sample output
    # ASR903_5    os_copied   True        2020-11-18 13:07:57
    return db.get_output_line(hostname, "os_copied", when_tested)[2]

# Returns the current os_version on the device
def os_version(hostname, when_tested):

    # Sample output
    # ASR903_5    os_version  16.10.1     2020-11-18 13:37:56
    return db.get_output_line(hostname, "os_version", when_tested)[2]

# Returns True if the `boot system bootflash:/...` command are present, in the right order
def boot_system(hostname, when_tested):

    # Sample output
    # ASR903_5    boot_system  True     2020-11-18 13:37:56
    return db.get_output_line(hostname, "boot_system", when_tested)[2]

# Returns the CPU utilisation for the last 5 minutes on the device
def cpu(hostname, when_tested):

    # Sample output
    # ASR903_5    cpu  25     2020-11-18 13:37:56
    return db.get_output_line(hostname, "cpu", when_tested)[2]

### 
### SAVING OUTPUTS IN THE DB
###

# Save in the DB the `show ip route summary`
def save_route_summary_db(device, list_vrf, when_tested, current_time):

    test_name = "route_summary"
    dict_final = {'vrf': {}}

    # Building the full dict, adding route_summary from each vrf
    for vrf in list_vrf:

        if vrf == "default":
            dict_vrf = device.parse(f"show ip route summary")

            # Adding the dict for the vrf to the concatenated dict
            dict_final['vrf'][vrf] = dict_vrf['vrf'][vrf]
        else: 
            try:   
                dict_vrf = device.parse(f"show ip route vrf {vrf} summary")

                # Adding the dict for the vrf to the concatenated dict
                dict_final['vrf'][vrf] = dict_vrf['vrf'][vrf]
            
            # The VRF doesn't exist
            except SchemaEmptyParserError as e:
                # Silently dicard the error, and move to the next VRF
                pass

    # Converting as a string to be saved in the DB
    output = json.dumps(dict_final)

    db.add_output(device.name, test_name, output, current_time)
    db.add_timestamp(device.name, test_name, when_tested, current_time)


# Save in the DB the `show ip route`
def save_routes_db(device, when_tested, current_time):

    test_name = "routes"

    # Converting as a string to be saved in the DB
    output = json.dumps(device.parse('show ip route vrf *'))

    db.add_output(device.name, test_name, output, current_time)
    db.add_timestamp(device.name, test_name, when_tested, current_time)


# Save in the DB the `show isis neighbors`
def save_isis_db(device, when_tested, current_time):

    test_name = "isis"

    # Converting as a string to be saved in the DB
    output = json.dumps(device.parse('show isis neighbors'))

    db.add_output(device.name, test_name, output, current_time)
    db.add_timestamp(device.name, test_name, when_tested, current_time)


# Save in the DB the `show xconnect all`
def save_xconnect_db(device, when_tested, current_time):

    test_name = "xconnect"

    # Converting as a string to be saved in the DB
    output = json.dumps(device.parse('show xconnect all'))

    db.add_output(device.name, test_name, output, current_time)
    db.add_timestamp(device.name, test_name, when_tested, current_time)


# Check if the device has 2 RSP
# Assign the device `number_rsp` attribute with the number of RSP on the device
def set_number_rsp(device):

    platform = device.parse('show platform')

    # If R0 and R1 are in the list, the device supports two RSP
    if 'R0' and 'R1' in platform['slot'].keys(): 
        # Makes a list with the RSP inserted in each slot. Name of the RSP or empty
        # Sample output:
        #   'R0': {'other': {'A900-RSP3C-400-W': {'insert_time': '1w2d',
        #                                         'name': 'A900-RSP3C-400-W',
        #                                         'slot': 'R0',
        #                                         'state': 'ok, active'}}},
        #   'R1': {'other': {'': {'insert_time': '1w2d',
        #                         'name': '',
        #                         'slot': 'R1',
        #                         'state': 'unknown'}}}}}
        rsp = list(platform['slot']['R0']['other'].keys()) + list(platform['slot']['R1']['other'].keys()) 
        # 2 - (number of empty slots)
        device.number_rsp = 2 - rsp.count('')
    else: device.number_rsp = 1


# Save in the DB if the new OS and the rommon have been copied on the device
# We don't check if the old_os is copied (no need)
# If the router has dual RSP, check in the bootflash and stby-bootflash
def save_os_copied_db(device, os_target, rommon_target, folder_images, when_tested, current_time):

    test_name = "os_copied"
    folder_new_os = folder_images['new_os']
    folder_rommon = folder_images['rommon']

    # List of Booleans to store if os has been copied
    # Each item in the list will be the result for each RSP
    # Converted as string, because I can't store booleans in the DB
    os_copied = [] 

    # Set device attribute `number_rsp` with the number of RSP inserted on the device
    set_number_rsp(device)

    # If device has two RSP, we will also check the files on the standby-bootflash
    if device.number_rsp == 2: 
        bootflash_list = ['bootflash', 'stby-bootflash']
    if device.number_rsp == 1:
        bootflash_list = ['bootflash']

    for bootflash in bootflash_list:

        # List to store the names of files that have been successfully copied on the device.
        # Reset to empty for each RSP
        # Will compare to len(os_target)
        number_files_copied = []

        # Verify that the folder exists
        try:

            # Checking OS files
            files = device.parse(f"dir {bootflash}:{folder_new_os}")

            for file in files['dir'][f'{bootflash}:/{folder_new_os}/']['files']:
                for os in os_target:

                    # If we have a match
                    if file == os: 
                        number_files_copied.append(os)
            
            # Checking Rommon
            files = device.parse(f'dir {bootflash}:{folder_rommon}')

            for file in files['dir'][f'{bootflash}:/{folder_rommon}/']['files']:
                for rommon in rommon_target:

                    # If we have a match
                    if file == rommon:
                        number_files_copied.append(rommon)

            # If we have all OS + Rommon files
            if len(number_files_copied) == len(os_target) + len(rommon_target): os_copied.append("True")
            else: os_copied.append("False")

        # If the parser is empty == the directory doesn't exist
        except SchemaEmptyParserError as e:
            # Silently discard it, test is failed by default
            os_copied.append("False")

        # If the parser is not empty == the directory exist, but it is empty
        except SchemaMissingKeyError as e:
            # Silently discard it, test is failed by default 
            os_copied.append("False")
        
    # If the test has not failed for all the RSP, True
    # Else False    
    if "False" not in os_copied: os_copied_result = "True"
    else: os_copied_result = "False"    

    db.add_output(device.name, test_name, os_copied_result, current_time)
    db.add_timestamp(device.name, test_name, when_tested, current_time)

# Save in the DB the current version of the device
def save_os_current_version_db(device, when_tested, current_time):

    test_name = "os_version"

    os_current_version = device.parse('show version')['version']['version']

    db.add_output(device.name, test_name, os_current_version, current_time)
    db.add_timestamp(device.name, test_name, when_tested, current_time)

# Save in the DB the CPU utilisation for the last 5 minutes
def save_cpu(device, when_tested, current_time):

    test_name = "cpu"

    # Converting int as str, to be saved in the DB
    cpu = str(device.parse('show processes cpu')['five_sec_cpu_total'])

    db.add_output(device.name, test_name, cpu, current_time)
    db.add_timestamp(device.name, test_name, when_tested, current_time)

# Save in the DB if the `boot system bootflash:/...` commands are present in the rigth order
def save_boot_system_db(device, folder_images, when_tested, current_time):

    test_name = "boot_system"
    boot_flash = 'False'
    folder_new_os = folder_images['new_os']
    folder_backup_os = folder_images['backup_os']

    # This will return a big string
    config_string = device.execute('show startup')
    # Splitting in a list, for each line in the config
    config = config_string.split('\n')

    for line in config:
        
        # Matching the first line
        if line in f"boot system bootflash:/{folder_new_os}/packages.conf\r":
            
            # If the next line is the backup OS (the old one), expected answer.
            if config[config.index(line) + 1] in f"boot system bootflash:/{folder_backup_os}/packages.conf\r":
                boot_flash = 'True'

                # No need to continue
                break
    
    db.add_output(device.name, test_name, boot_flash, current_time)
    db.add_timestamp(device.name, test_name, when_tested, current_time)    

# Adding one more test to the total_number_tests
def add_result_device(device, test_name, test_result):
    
    # if test_name is a string
    if isinstance(test_name, str):
        device.test_results[test_name] = test_result

    # if test_name is a dict
    if isinstance(test_name, dict):
        for key, value in test_name.items():
            # if the key does not exist
            if key not in device.test_results.keys():
                device.test_results[key] = {}

            device.test_results[key][value] = test_result
            
###
### COMPARING
###

# Returns the number of neighbors before/after
# Returns a tuple of 2 integers 
# (number_neighbors_before, number_neighbors_after)
def get_isis_before_after(hostname):
    output_before = json.loads(db.get_output_test(hostname, "isis", "before"))
    output_after = json.loads(db.get_output_test(hostname, "isis", "after"))

    for tag in output_before['isis']:
        number_neighbors_before = len(output_before['isis'][tag]['neighbors'])

    for tag in output_after['isis']:
        number_neighbors_after = len(output_after['isis'][tag]['neighbors'])       

    return (number_neighbors_before, number_neighbors_after)


# Returns the number of routes before/after for a specific protocol and vrf
# Returns a tuple of 2 integers 
# (number_routes_before, number_routes_after)
def get_routes_before_after(hostname, protocol, vrf): 
    output_before = json.loads(db.get_output_test(hostname, "route_summary", "before"))
    output_after = json.loads(db.get_output_test(hostname, "route_summary", "after"))

    ## BGP
    if protocol == "bgp":
        try:
            route_source = output_before['vrf'][vrf]['route_source'][protocol]
            
            for as_number in route_source:
                number_routes_before = route_source[as_number]['subnets']
        
        # If the key doesn't exist, we have no routes for this protocol
        except KeyError as e:
            number_routes_before = 0

        try:
            route_source = output_after['vrf'][vrf]['route_source'][protocol]

            for as_number in route_source:
                number_routes_after = route_source[as_number]['subnets']

        # If the key doesn't exist, we have no routes for this protocol
        except KeyError as e:
            number_routes_after = 0

    ## ISIS
    if protocol == "isis":
        try:
            route_source = output_before['vrf'][vrf]['route_source'][protocol]
            
            for tag in route_source:
                number_routes_before = route_source[tag]['subnets']

        # If the key doesn't exist, we have no routes for this protocol
        except KeyError as e:
            number_routes_before = 0

        try:
            route_source = output_after['vrf'][vrf]['route_source'][protocol]
            for tag in route_source:
                number_routes_after = route_source[tag]['subnets']

        # If the key doesn't exist, we have no routes for this protocol
        except KeyError as e:
            number_routes_after = 0

    ## Connected
    if protocol == "connected":
        try:
            route_source = output_before['vrf'][vrf]['route_source'][protocol]
            number_routes_before = route_source['subnets']

        # If the key doesn't exist, we have no routes for this protocol
        except KeyError as e:
            number_routes_before = 0

        try:
            route_source = output_after['vrf'][vrf]['route_source'][protocol]
            number_routes_after = route_source['subnets']

        # If the key doesn't exist, we have no routes for this protocol
        except KeyError as e:
            number_routes_after = 0

    ## Internal -- For internal we take `networks` not `subnets` (doesn't exist)
    if protocol == "internal":
        try:
            route_source = output_before['vrf'][vrf]['route_source'][protocol]
            number_routes_before = route_source['networks']

        # If the key doesn't exist, we have no routes for this protocol
        except KeyError as e:
            number_routes_before = 0

        try:
            route_source = output_after['vrf'][vrf]['route_source'][protocol]
            number_routes_after = route_source['networks']

        # If the key doesn't exist, we have no routes for this protocol
        except KeyError as e:
            number_routes_after = 0

    return (number_routes_before, number_routes_after)       

# Checks if the VRF exists before/after
# Returns a tuple of 2 booleans 
# (vrf_exists_before, vrf_exists_after)
def vrf_exists(hostname, vrf_to_check):

    vrf_exists_before = False
    vrf_exists_after = False

    output_before = json.loads(db.get_output_test(hostname, "routes", "before"))
    output_after = json.loads(db.get_output_test(hostname, "routes", "after"))

    if vrf_to_check in output_before['vrf']:    vrf_exists_before = True
    if vrf_to_check in output_after['vrf']:     vrf_exists_after = True

    return(vrf_exists_before, vrf_exists_after)
        
# Returns the number of neighbors before/after
# Returns a tuple of 2 integers 
# (number_xconnect_before, number_xconnect_after)
def get_xconnect_before_after(hostname):
    
    number_xconnect_before = 0
    number_xconnect_after = 0

    output_before = json.loads(db.get_output_test(hostname, "xconnect", "before"))
    output_after = json.loads(db.get_output_test(hostname, "xconnect", "after"))

    for segment_1 in output_before['segment_1']:
        for segment_2 in output_before['segment_1'][segment_1]['segment_2']:

            # If the xconnect is UP, increment number_xconnect
            if output_before['segment_1'][segment_1]['segment_2'][segment_2]['xc'] == 'UP':
                number_xconnect_before +=1

    for segment_1 in output_after['segment_1']:
        for segment_2 in output_after['segment_1'][segment_1]['segment_2']:

            # If the xconnect is UP, increment number_xconnect
            if output_after['segment_1'][segment_1]['segment_2'][segment_2]['xc'] == 'UP':
                number_xconnect_after +=1      

    return (number_xconnect_before, number_xconnect_after)


###
### RESULTS
###

def table_results(testbed):

    table = PrettyTable()
    
    ## BUILDING THE HEADER
    # | Hostname | Test1 | Test2 |...
    table_header = ["hostname"]

    for test in testbed.tests_run:

        if isinstance(test, dict): 

            for key, value in test.items():  

                if key not in table_header: 
                    table_header.append(key)

        if isinstance(test, str):
            table_header.append(test)

    table.field_names = table_header

    ## BUILDING THE LINES
    # We can make another loop here. The `testbed.tests_run` tests and
    # `device.test_results` tests will be in the same order. They are added at the same time.
    for device in testbed:

        # | Hostname | Test1_result | Test2_result |
        table_line = [device.name]

        for test, result in device.test_results.items():

            # If the result is a dict, compare the sub-tests results. 
            # If one of them fails, the test fails.
            if isinstance(result, dict):

                # By default, assume Pass
                end_result = "Pass"

                # Prove me wrong
                for sub_test, sub_result in result.items():
                    if sub_result == "Fail": end_result = "Fail"

                table_line.append(end_result)
            
            if isinstance(result, str) or isinstance(result, int): 
                table_line.append(result)

        table.add_row(table_line)

    return str(table)