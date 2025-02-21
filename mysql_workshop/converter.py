import csv
import sqlite3

# Function to create the SQL table
def create_table(cursor, table_name, columns):
    column_string = ', '.join(columns)
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({column_string})")

# Function to insert data into the SQL table
def insert_data(cursor, table_name, data):
    placeholders = ', '.join(['?'] * len(data))
    cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", data)

# Specify the CSV file path
csv_file = './'

# Specify the SQL database file path
sql_file = 'path/to/your/sql_file.db'

# Specify the table name for the SQL database
table_name = 'your_table_name'

# Specify the SQL column names (corresponding to CSV headers)
columns = ['column_1', 'column_2', 'column_3']

# Create an SQLite connection
connection = sqlite3.connect(sql_file)
cursor = connection.cursor()

# Create the SQL table
create_table(cursor, table_name, columns)

# Read the CSV file and insert data into the SQL table
with open(csv_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        insert_data(cursor, table_name, row)

# Commit changes and close the connection
connection.commit()
connection.close()
