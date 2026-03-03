SELECT DATE_TRUNC('month', event_time) as month, SUM(price) as total_sales
FROM customers
WHERE event_type = 'purchase'
GROUP BY month;