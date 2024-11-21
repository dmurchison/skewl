CREATE DATABASE Murch_db;

SHOW DATABASES;
USE Murch_db;
CREATE TABLE tb2 (user_id VARCHAR( 50 ));
SHOW TABLES;
ALTER TABLE tb2 add newfield VARCHAR(25);

CREATE TABLE Employee (
    Employee_ID SMALLINT,
    First_Name VARCHAR(40),
    Last_Name VARCHAR(60),
    Department_ID SMALLINT,
    Classification VARCHAR(10),
    Status VARCHAR(10),
    Salary DECIMAL(7,2));

DESCRIBE Employee;

INSERT INTO Employee (Employee_ID, First_Name, Last_Name, Department_ID, Classification, Status, Salary)
VALUES
(100, 'John', 'Smith', 1, 'Exempt', 'Full-Time', 90000),
(101, 'Mary', 'Jones', 2, 'Non-Exempt', 'Part-Time', 35000),
(102, 'Mary', 'Williams', 3, 'Exempt', 'Full-Time', 80000),
(103, 'Gwen', 'Johnson', 2, NULL, 'Full-Time', 40000),
(104, 'Michael', 'Jones', 3, 'Non-Exempt', 'Full-Time', 90000);

CREATE TABLE branches (
    Department_ID INT PRIMARY KEY,
    Department_Name VARCHAR(50)
);
INSERT INTO branches (Department_ID, Department_Name)
VALUES
(1, 'Accounting'),
(2, 'Human Resources'),
(3, 'Information Systems'),
(4, 'Marketing');

Select sum(Salary) from Employee where Department_ID=3;

INSERT INTO Employee (Employee_ID, First_Name, Last_Name, Department_ID, Classification, Status, Salary)
VALUES
    (103, 'Gwen', 'Johnson', 4, NULL, 'Full-Time', 40000),
    (104, 'Michael', 'Jones', 4, 'Non-Exempt', 'Full-Time', 90000);

INSERT INTO Employee (Employee_ID, First_Name, Last_Name, Department_ID, Classification, Status, Salary)
VALUES
    (105, 'Duncan', 'Murchison', 1, 'Non-Exempt', 'Full-Time', 75000),
    (106, 'Lawrence', 'Taylor', 2, 'Exempt', 'Part-Time', 45000),
    (107, 'Kerry', 'Collins', 3, 'Non-Exempt', 'Full-Time', 85000),
    (108, 'Michael', 'Vick', 4, 'Exempt', 'Full-Time', 95000);

ALTER TABLE branches RENAME TO Department;

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
    Department_ID=1;
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
