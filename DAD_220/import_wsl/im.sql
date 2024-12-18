CREATE SCHEMA Quantigration_RMA;


SHOW DATABASES;


USE Quantigration_RMA;


CREATE TABLE Quantigration_RMA.Customers (
    Customer_ID INT PRIMARY KEY,
    First_Name VARCHAR(25),
    Last_Name VARCHAR(25),
    Street VARCHAR(50),
    City VARCHAR(50),
    State VARCHAR(25),
    ZipCode VARCHAR(10),
    Telephone VARCHAR(15)
);


SHOW TABLES;


CREATE TABLE Quantigration_RMA.Orders (
    Order_ID INT PRIMARY KEY,
    Customer_ID INT,
    SKU VARCHAR(20),
    Description VARCHAR(50),
    FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID)
);


CREATE TABLE Quantigration_RMA.RMA (
    RMA_ID INT PRIMARY KEY,
    Order_ID INT,
    Step VARCHAR(50),
    Status VARCHAR(15),
    Reason VARCHAR(15),
    FOREIGN KEY (Order_ID)  REFERENCES Orders(Order_ID)
);


GRANT CREATE VIEW ON *.* TO 'duck'@;
GRANT CREATE VIEW ON *.* TO 'username'@'host';


CREATE VIEW Quantigration_RMA.Collaborators AS
SELECT
    Customer_ID AS CollaboratorID,
    First_Name,
    Last_Name,
    Street,
    City,
    State,
    ZipCode,
    Telephone
FROM
    Quantigration_RMA.Customers;


INSERT INTO Quantigration_RMA.Customers (Customer_ID, First_Name, Last_Name, Street, City, State, ZipCode, Telephone)
VALUES
    (1, 'John', 'Doe', '123 Elm St', 'Springfield', 'IL', '62701', '555-1234'),
    (2, 'Jane', 'Smith', '456 Oak St', 'Springfield', 'IL', '62702', '555-5678'),
    (3, 'Jim', 'Brown', '789 Pine St', 'Springfield', 'IL', '62703', '555-8765'),
    (4, 'Jake', 'White', '101 Maple St', 'Springfield', 'IL', '62704', '555-4321'),
    (5, 'Jill', 'Green', '202 Birch St', 'Springfield', 'IL', '62705', '555-6789'),
    (6, 'Jerry', 'Black', '303 Cedar St', 'Springfield', 'IL', '62706', '555-9876'),
    (7, 'Janet', 'Blue', '404 Walnut St', 'Springfield', 'IL', '62707', '555-5432'),
    (8, 'Jeff', 'Yellow', '505 Ash St', 'Springfield', 'IL', '62708', '555-2109'),
    (9, 'Jessica', 'Purple', '606 Cherry St', 'Springfield', 'IL', '62709', '555-6543'),
    (10, 'Jordan', 'Orange', '707 Poplar St', 'Springfield', 'IL', '62710', '555-3210');


