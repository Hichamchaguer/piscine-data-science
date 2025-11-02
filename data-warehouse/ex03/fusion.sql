-- add column names in cotumer table
ALTER TABLE cotumer
ADD COLUMN category_id BIGINT,
ADD COLUMN category_code VARCHAR(200),
ADD COLUMN brand VARCHAR(200);

-- update cotumer table by joining with item table
UPDATE costumer c
SET 
    category_id = i.category_id,
    category_code = i.category_code,
    brand = i.brand
FROM item i
WHERE c.product_id = i.product_id;