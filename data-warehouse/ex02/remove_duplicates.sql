DELETE FROM customers t1
USING customers t2
WHERE t1.ctid > t2.ctid 
  AND t1.event_type = t2.event_type
  AND t1.product_id = t2.product_id
  AND t1.price = t2.price
  AND t1.user_id = t2.user_id
  AND t1.user_session = t2.user_session
  AND DATE(t1.event_time) = DATE(t2.event_time);