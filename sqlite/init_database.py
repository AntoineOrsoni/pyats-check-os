import sqlite3
db_connection = sqlite3.connect('sqlite/db/checks.db')
db_cursor = db_connection.cursor()

# Setting up the database
## timestamp table
db_cursor.execute('''CREATE TABLE timestamps (hostname text, test_name text, when_tested text, timestamp text)''')

## outputs table
db_cursor.execute('''CREATE TABLE outputs (hostname text, test_name text, output text, timestamp text)''')

db_connection.commit()