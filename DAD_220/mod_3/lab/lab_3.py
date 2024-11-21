import mysql.connector
import csv

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host='172.23.50.25',
    user='duck',
    password='H-ton1069',
    database='Murch_db'
)

# Create a cursor object
cursor = conn.cursor()

# Define the SQL query
query = """
SELECT
    First_Name,
    Last_Name,
    Department.Department_Name
FROM
    Employee
INNER JOIN
    Department
ON
    Employee.Department_ID = Department.Department_ID
WHERE
    Employee.Department_ID = 3
    OR Employee.Department_ID = 2;
"""

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Define the CSV file path
csv_file_path = "/home/shlacker2020/Batcave/SNHU/DAD_220/mod_1/lab_1.csv"

# Write the results to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['First_Name', 'Last_Name', 'Department_Name'])
    # Write the data
    writer.writerows(results)

# Close the cursor and connection
cursor.close()
conn.close()
