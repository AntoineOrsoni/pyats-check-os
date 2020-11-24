from genie.testbed import load
from genie.metaparser.util.exceptions import SchemaEmptyParserError
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

### 
### SAVING OUTPUTS IN THE DB
###

# Save in the DB the `show ip route summary`
def save_route_summary_db(device, when_tested, current_time):

    test_name = "route_summary"

    # Converting as a string to be saved in the DB
    output = json.dumps(device.parse('show ip route summary'))

    db.add_output(device.name, test_name, output, current_time)
    db.add_timestamp(device.name, test_name, when_tested, current_time)


# Save in the DB the `show ip route`
def save_routes_db(device, when_tested, current_time):

    test_name = "routes"

    # Converting as a string to be saved in the DB
    output = json.dumps(device.parse('show ip route'))

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


# Save in the DB if the OS has been copied on the device
def save_os_copied_db(device, os_target, rommon_target, when_tested, current_time):

    test_name = "os_copied"

    # List to store the names of files that have been successfully copied on the device.
    # Will compare to len(os_target)
    number_files_copied = []

    # Boolean to store if os has been copied
    # Converted as string, because I can't store booleans in the DB
    os_copied = "False" 

    # Verify that the folder exists
    try:

        # Checking OS files
        files = device.parse('dir bootflash:ImageTarget')

        for file in files['dir']['bootflash:/ImageTarget/']['files']:
            for os in os_target:

                # If we have a match
                if file == os: 
                    number_files_copied.append(os)
        
        # Checking Rommon
        files = device.parse('dir')

        for file in files['dir']['bootflash:/']['files']:
            for rommon in rommon_target:

                # If we have a match
                if file == rommon:
                    number_files_copied.append(rommon)

        # If we have all OS + Rommon files
        if len(number_files_copied) == len(os_target) + len(rommon_target): os_copied = "True"

    # If the parser is empty == the directory doesn't exist, catch the Error
    except SchemaEmptyParserError as e:
        # Silently discard it, test is failed by default 
        pass
        
    db.add_output(device.name, test_name, os_copied, current_time)
    db.add_timestamp(device.name, test_name, when_tested, current_time)

# Save in the DB the current version of the device
def save_os_current_version_db(device, when_tested, current_time):

    test_name = "os_version"

    os_current_version = device.parse('show version')['version']['version']

    db.add_output(device.name, test_name, os_current_version, current_time)
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
        route_source = output_before['vrf'][vrf]['route_source'][protocol]
        
        for as_number in route_source:
            number_routes_before = route_source[as_number]['subnets']

        route_source = output_after['vrf'][vrf]['route_source'][protocol]

        for as_number in route_source:
            number_routes_after = route_source[as_number]['subnets']

        return (number_routes_before, number_routes_after)

    ## ISIS
    if protocol == "isis":
        route_source = output_before['vrf'][vrf]['route_source'][protocol]

        for tag in route_source:
            number_routes_before = route_source[tag]['subnets']

        route_source = output_after['vrf'][vrf]['route_source'][protocol]

        for tag in route_source:
            number_routes_after = route_source[tag]['subnets']

        return (number_routes_before, number_routes_after)

    ## Connected
    if protocol == "connected":
        route_source = output_before['vrf'][vrf]['route_source'][protocol]
        number_routes_before = route_source['subnets']

        route_source = output_after['vrf'][vrf]['route_source'][protocol]
        number_routes_after = route_source['subnets']

        return (number_routes_before, number_routes_after)    

    ## Internal -- For internal we take `networks` not `subnets` (doesn't exist)
    if protocol == "internal":
        route_source = output_before['vrf'][vrf]['route_source'][protocol]
        number_routes_before = route_source['networks']

        route_source = output_after['vrf'][vrf]['route_source'][protocol]
        number_routes_after = route_source['networks']

        return (number_routes_before, number_routes_after)       

# Checks if the VRF exists before/after
# Returns a tuple of 2 booleans 
# (vrf_exists_before, vrf_exists_after)
def vrf_exists(hostname, vrf_to_check):

    vrf_exists_before = False
    vrf_exists_after = False

    output_before = json.loads(db.get_output_test(hostname, "route_summary", "before"))
    output_after = json.loads(db.get_output_test(hostname, "route_summary", "after"))

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
            
            if isinstance(result, str): 
                table_line.append(result)

        table.add_row(table_line)

    return str(table)