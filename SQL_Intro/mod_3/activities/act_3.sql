-- Create the schema
CREATE SCHEMA Quantigration_RMA;

-- Create the Customers table
CREATE TABLE Quantigration_RMA.Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(25),
    LastName VARCHAR(25),
    StreetAddress VARCHAR(50),
    City VARCHAR(50),
    State VARCHAR(25),
    ZipCode VARCHAR(10),
    Telephone VARCHAR(15)
);

-- Create the Orders table
CREATE TABLE Quantigration_RMA.Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    SKU VARCHAR(20),
    Description VARCHAR(50),
    FOREIGN KEY (CustomerID) REFERENCES Quantigration_RMA.Customers(CustomerID)
);

-- Create the RMA table
CREATE TABLE Quantigration_RMA.RMA (
    RMAID INT PRIMARY KEY,
    OrderID INT,
    Step VARCHAR(50),
    Status VARCHAR(15),
    Reason VARCHAR(25),
    FOREIGN KEY (OrderID) REFERENCES Quantigration_RMA.Orders(OrderID)
);

CREATE VIEW Quantigration_RMA.Collaborators AS
SELECT
    CustomerID AS CollaboratorID,
    FirstName,
    LastName,
    StreetAddress,
    City,
    State,
    ZipCode,
    Telephone
FROM
    Quantigration_RMA.Customers;

-- Insert records into the Customers table
INSERT INTO Quantigration_RMA.Customers (CustomerID, FirstName, LastName, StreetAddress, City, State, ZipCode, Telephone)
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
