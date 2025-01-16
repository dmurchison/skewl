-- Lab 1
CREATE DATABASE Murch_db;

SHOW DATABASES;
USE Murch_db;
CREATE TABLE tb2 (user_id VARCHAR( 50 ));
SHOW TABLES;
ALTER TABLE tb2 add newfield VARCHAR(25);


-- Lab 3
ALTER TABLE Branches RENAME TO Department;

INSERT INTO Employee (Employee_ID, First_Name, Last_Name, Department_ID, Classification, Status, Salary)
VALUES
    (108, 'Alice', 'Brown', 1, 'Exempt', 'Full-Time', 70000),
    (109, 'Bob', 'Green', 2, 'Non-Exempt', 'Part-Time', 32000),
    (110, 'Charlie', 'Black', 3, 'Exempt', 'Full-Time', 85000),
    (111, 'Diana', 'White', 4, 'Non-Exempt', 'Full-Time', 60000),
    (112, 'Eve', 'Davis', 1, 'Exempt', 'Full-Time', 75000),
    (113, 'Frank', 'Miller', 2, 'Non-Exempt', 'Part-Time', 30000),
    (114, 'Grace', 'Wilson', 3, 'Exempt', 'Full-Time', 80000),
    (115, 'Hank', 'Moore', 4, 'Non-Exempt', 'Full-Time', 65000),
    (116, 'Ivy', 'Taylor', 1, 'Exempt', 'Full-Time', 72000),
    (117, 'Jack', 'Anderson', 2, 'Non-Exempt', 'Part-Time', 34000);


SELECT *
FROM
    Employee
WHERE
    Department_ID=1
INTO OUTFILE
    '/var/lib/mysql-files/Employee_Department_1.txt';


select
    First_Name, Last_Name, Department.Department_Name
from
    Employee
inner join
    Department
on
    Employee.Department_ID = Department.Department_ID
where
    Employee.Department_ID = 3 OR Employee.Department_ID = 2
