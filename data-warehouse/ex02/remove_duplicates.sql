-- create a temp table that delete duplicates based on all columns
CREATE TABLE temp AS SELECT DISTINCT * FROM customers;

-- drop or truncate the original table
TRUNCATE TABLE customers;

-- recreate the original table and insert the data from the temp table
INSERT INTO customers SELECT * FROM temp;

-- drop the temp table
TRUNCATE TABLE temp;