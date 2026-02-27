begin;

CREATE TABLE IF NOT EXISTS customers AS
    SELECT * FROM data_2022_oct
    UNION ALL
    SELECT * FROM data_2022_nov
    UNION ALL
    SELECT * FROM data_2022_dec
    UNION ALL
    SELECT * FROM data_2023_jan
    UNION ALL
    SELECT * FROM data_2023_feb;

DELETE FROM customers
WHERE ctid IN (
  SELECT ctid
  FROM (
    SELECT
      ctid,
      event_time,
      prev_time
    FROM (
      SELECT
        ctid,
        event_time,
        LAG(event_time) OVER (
          PARTITION BY
            event_type,
            product_id,
            price,
            user_id,
            user_session
          ORDER BY event_time
        ) AS prev_time
      FROM customers
    ) t1
    WHERE prev_time IS NOT NULL
      AND event_time - prev_time <= INTERVAL '5 second'
  ) t2
);

commit;ALTER TABLE customers
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

commit;