from genie.testbed import load
import toolbox.database as db
import json

###
### CHECKING
###

# Returns True if the target OS is copied on the device
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
def save_os_copied_db(device, os_target, when_tested, current_time):

    test_name = "os_copied"

    # Boolean to store if os has been copied
    # Converted as string, because I can't store booleans in the DB
    os_copied = "False" 
    files = device.parse('dir')

    for file in files['dir']['bootflash:/']['files']:

        if file == os_target: os_copied = "True"
    
    db.add_output(device.name, test_name, os_copied, current_time)
    db.add_timestamp(device.name, test_name, when_tested, current_time)

# Save in the DB the current version of the device
def save_os_current_version_db(device, when_tested, current_time):

    test_name = "os_version"

    os_current_version = device.parse('show version')['version']['version']

    db.add_output(device.name, test_name, os_current_version, current_time)
    db.add_timestamp(device.name, test_name, when_tested, current_time)


###
### COMPARING
###

# Returns the number of neighbors before/after
def get_isis_before_after(hostname):
    output_before = json.loads(db.get_output_test(hostname, "isis", "before"))
    output_after = json.loads(db.get_output_test(hostname, "isis", "before"))

    for tag in output_before['isis']:
        number_neighbors_before = len(output_before['isis'][tag]['neighbors'])

    for tag in output_after['isis']:
        number_neighbors_after = len(output_after['isis'][tag]['neighbors'])       

    return (number_neighbors_before, number_neighbors_after)


# Returns the number of routes before/after for a specific protocol and vrf
def get_routes_before_after(hostname, protocol, vrf): 
    output_before = json.loads(db.get_output_test(hostname, "route_summary", "before"))
    output_after = json.loads(db.get_output_test(hostname, "route_summary", "before"))

    if protocol == "bgp":
        route_type = output_before['vrf'][vrf]['route_source'][protocol]
        
        for as_number in route_type:
            number_routes_before =  route_type[as_number]['external'] \
                                    + route_type[as_number]['internal'] \
                                    + route_type[as_number]['subnets'] \
                                    + route_type[as_number]['networks']

        route_type = output_after['vrf'][vrf]['route_source'][protocol]

        for as_number in route_type:
            number_routes_after =  route_type[as_number]['external'] \
                                    + route_type[as_number]['internal'] \
                                    + route_type[as_number]['subnets'] \
                                    + route_type[as_number]['networks']

        return (number_routes_before, number_routes_after)

# Checks if the VRF exists before/after
def vrf_exists(hostname, vrf_to_check):

    vrf_exists_before = False
    vrf_exists_after = False

    output_before = json.loads(db.get_output_test(hostname, "route_summary", "before"))
    output_after = json.loads(db.get_output_test(hostname, "route_summary", "before"))

    if vrf_to_check in output_before['vrf']:    vrf_exists_before = True
    if vrf_to_check in output_after['vrf']:     vrf_exists_after = True

    return(vrf_exists_before, vrf_exists_after)