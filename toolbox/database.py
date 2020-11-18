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


# Add `output in the `outputs` table
def add_output(hostname, test_name, output, current_time):

    # Creating a `output_tuple` to insert in the `outputs` table.
    # | hostname | test_name | output   | timestamp           |
    output_tuple = []
    output_tuple.extend((hostname, test_name, output, current_time))    

    # Inserting a line in the `output` table
    db_cursor.execute('''INSERT INTO outputs VALUES (?,?,?,?)''', output_tuple)
    db_connection.commit()


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