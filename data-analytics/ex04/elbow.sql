SELECT user_id, COUNT(*) as purchases
FROM customers
WHERE event_type = 'purchase'
GROUP BY user_id
ORDER BY purchases DESC;