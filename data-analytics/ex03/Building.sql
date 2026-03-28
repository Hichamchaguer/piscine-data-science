SELECT user_id, COUNT(*) as count
FROM customers
WHERE event_type='purchase'
GROUP BY user_id;