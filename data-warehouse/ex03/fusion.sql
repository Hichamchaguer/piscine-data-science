CREATE TABLE items_nodup AS 
SELECT product_id,
         max(category_id) as category_id,
         max(category_code) as category_code,
         max(brand) as brand
FROM item
GROUP BY product_id

SELECT c.*, i.category_id, i.category_code, i.brand
from customers
LEFT JOIN item (
    SELECT product_id,
            max(category_id) as category_id,
            max(category_code) as category_code,
            max(brand) as brand
    FROM item
    GROUP BY product_id
) i 
ON c.product_id = i.product_id;