-- Write the SQL to create a Product table with the following columns:

-- ID - Integer with range 0 to 65,535
-- Name - Variable-length string with maximum 40 characters
-- ProductType - Fixed-length string with 3 characters
-- OriginDateTime - Year, month, day, and time
-- Weight - Decimal number with variable precision and 4 bytes of storage

CREATE TABLE Product (
    ID INT UNSIGNED,
    Name VARCHAR(40),
    ProductType CHAR(3),
    OriginDateTime DATETIME,
    Weight DECIMAL(10, 1)
);
