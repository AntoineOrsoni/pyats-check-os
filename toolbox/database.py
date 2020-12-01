import sqlite3
db_connection = sqlite3.connect('sqlite/db/checks.db')
db_cursor = db_connection.cursor()


# Add a `timestamp` in the `timestamps` table
def add_timestamp(hostname, test_name, when_tested, current_time):

    # Creating a `timestamps_tuple` to insert in the `outputs` table.
    # | MyRouter | TestName | WhenTested | Timestamp |
    timestamps_tuple = []
    timestamps_tuple.extend((hostname, test_name, when_tested, current_time))

    # Inserting a line in the `timestamp` table
    db_cursor.execute('''INSERT INTO timestamps VALUES (?,?,?,?)''', timestamps_tuple)
    db_connection.commit()


# Add an `output` in the `outputs` table
def add_output(hostname, test_name, output, current_time):

    # Creating a `output_tuple` to insert in the `outputs` table.
    # | hostname | test_name | output   | timestamp           |
    output_tuple = []
    output_tuple.extend((hostname, test_name, output, current_time))    

    # Inserting a line in the `output` table
    db_cursor.execute('''INSERT INTO outputs VALUES (?,?,?,?)''', output_tuple)
    db_connection.commit()


# Get the older timestamp for a device before or after.
# All test from the same batch will have the same timestamp. 
# I don't chare which test I get.
def get_oldest_timestamp(hostname, when_tested):
    
    filter_tuple = []
    filter_tuple.extend((when_tested, hostname))

    db_cursor.execute('''   SELECT * FROM timestamps 
                            WHERE when_tested = (?) AND hostname = (?)
                            ORDER BY timestamp DESC
                            LIMIT 1''', filter_tuple)

    # Sample output of db_cursor.fetchone()
    # ('ASR903_5', 'isis', 'before', '2020-11-17 11:51:45')
    return db_cursor.fetchone()[3]


# Return the list of all outputs for a specific device and the oldest timestamp
# Sample output
# ASR903_5    os_copied   True        2020-11-18 13:37:56
# ASR903_5    os_version  16.10.1     2020-11-18 13:37:56
# ASR903_5    route_summ  {"vrf": {"  2020-11-18 13:37:56
# ASR903_5    routes      {"vrf": {"  2020-11-18 13:37:56
# ASR903_5    isis        {"isis": {  2020-11-18 13:37:56
# ASR903_5    xconnect    {"segment_  2020-11-18 13:37:56
def get_list_outputs_device(hostname, when_tested, timestamp):

    filter_tuple = []
    filter_tuple.extend((hostname, timestamp))

    db_cursor.execute('''   SELECT * FROM outputs
                            WHERE hostname = (?) AND timestamp = (?)''', filter_tuple)
    
    output = db_cursor.fetchall()

    # Verify we've been able to get an output which is not empty
    if output is not None:
        return output
    else:
        raise ValueError(   f"output is empty. Check we have an output for :\n"
                            f"   - hostname = {hostname},\n"
                            f"   - timestamp = {timestamp}")


# Return the output for a specific test, oldest timestamp -- The entire line
# Sample output
# ASR903_5    os_version  16.10.1     2020-11-18 16:21:43
def get_output_line(hostname, test_name, when_tested):

    timestamp = get_oldest_timestamp(hostname, when_tested)

    filter_tuple = []
    filter_tuple.extend((hostname, timestamp, test_name))   

    db_cursor.execute('''   SELECT * FROM outputs
                            WHERE hostname = (?) AND timestamp = (?) AND test_name = (?)''', filter_tuple)

    output = db_cursor.fetchone()

    # Verify we've been able to get an output which is not empty
    if output is not None:
        return output
    else:
        raise ValueError(   f"output is empty. Check we have an output for :\n"
                            f"   - hostname = {hostname},\n"
                            f"   - test_name = {test_name},\n"
                            f"   - timestamp = {timestamp}") 


# Return the output for a specific test, oldest timestamp -- Only the `output` of the `test_name`
# Sample output
# 16.10.1
def get_output_test(hostname, test_name, when_tested):

    timestamp = get_oldest_timestamp(hostname, when_tested)

    filter_tuple = []
    filter_tuple.extend((hostname, timestamp, test_name))   

    db_cursor.execute('''   SELECT * FROM outputs
                            WHERE hostname = (?) AND timestamp = (?) AND test_name = (?)''', filter_tuple)

    output = db_cursor.fetchone()[2]

    # Verify we've been able to get an output which is not empty
    if output is not None:
        return output
    else:
        raise ValueError(   f"output is empty. Check we have an output for :\n"
                            f"   - hostname = {hostname},\n"
                            f"   - test_name = {test_name},\n"
                            f"   - timestamp = {timestamp}")
    

# Print all lines from table `outputs`
def print_outputs():
    db_cursor.execute('''SELECT * FROM outputs''')
    for line in db_cursor.fetchall():
        print(line)


# Print all ines from table `timestamps`
def print_timestamps():
    db_cursor.execute('''SELECT * FROM timestamps''')
    for line in db_cursor.fetchall():
        print(line)