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
      AND event_time - prev_time <= INTERVAL '10 second'
  ) t2
);
