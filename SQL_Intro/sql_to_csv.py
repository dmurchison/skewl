import mysql.connector # This is the MySQL connector that allows Python to connect to MySQL
import pandas as pd # This is the pandas module that allows Python to work with data in DataFrame format

# Establish a connection to the MySQL database - The connect() method takes the following parameters: host, user, password, and database
conn = mysql.connector.connect(
    host='172.24.27.224',
    user='duck',
    password='H-ton1069',
    database='Murch_db'
)

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

# Read the query results into a pandas DataFrame
df = pd.read_sql(query, conn)

# Define the CSV file path
csv_file_path = "/home/shlacker2020/Batcave/SNHU/DAD_220/mod_3/lab/lab_3.csv"

# Write the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

# Close the connection
conn.close()
