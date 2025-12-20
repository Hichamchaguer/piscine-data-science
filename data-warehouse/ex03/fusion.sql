-- add column names in customers table
ALTER TABLE customers
ADD COLUMN category_id BIGINT,
ADD COLUMN category_code VARCHAR(200),
ADD COLUMN brand VARCHAR(200);

-- update customers table by joining with item table
UPDATE customers c
SET 
    category_id = i.category_id,
    category_code = i.category_code,
    brand = i.brand
FROM item i
WHERE c.product_id = i.product_id;