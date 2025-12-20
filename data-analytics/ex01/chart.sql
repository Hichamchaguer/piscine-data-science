SELECT event_time, event_type, COUNT(*) AS event_count
FROM costumers
WHERE event_type = 'purchase'
AND event_time >= '2022-10-01'
AND event_time < '2023-03-01'
GROUP BY event_time, event_type
ORDER BY event_time ASC;