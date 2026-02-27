SELECT DATE(event_time) as dayy, event_type, COUNT(*) AS purchase_count
FROM customers
WHERE event_type = 'purchase'
AND event_time >= '2022-10-01'
AND event_time < '2023-03-01'
GROUP BY dayy, event_type
ORDER BY dayy ASC;