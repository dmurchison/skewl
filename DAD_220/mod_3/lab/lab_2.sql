-- Lab 2
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

CREATE TABLE Branches (
    Department_ID INT PRIMARY KEY,
    Department_Name VARCHAR(50)
);

INSERT INTO Branches (Department_ID, Department_Name)
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
