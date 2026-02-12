DROP TABLE IF EXISTS temp;
CREATE TABLE temp AS
SELECT c.*, i.category_id, i.category_code, i.brand
FROM customers c
LEFT JOIN item i ON c.product_id = i.product_id;