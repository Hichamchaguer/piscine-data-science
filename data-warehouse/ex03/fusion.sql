BEGIN;

ALTER TABLE customers
ADD COLUMN IF NOT EXISTS category_id bigint,
ADD COLUMN IF NOT EXISTS category_code text,
ADD COLUMN IF NOT EXISTS brand text;


UPDATE customers c
SET 
    category_id = i.category_id,
    category_code = i.category_code,
    brand = i.brand
FROM (
    SELECT
        product_id,
        max(category_id) AS category_id,
        max(category_code) AS category_code,
        max(brand) AS brand
    from item
    group by product_id
) i
WHERE c.product_id = i.product_id;

COMMIT;