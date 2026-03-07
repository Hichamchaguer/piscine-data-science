SELECT user_id, AVG(price) as average
FROM customers
WHERE event_type = 'cart'
GROUP BY user_id