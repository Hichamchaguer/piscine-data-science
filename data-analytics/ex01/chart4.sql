SELECT DATE(event_time) as day, SUM(price)/COUNT(DISTINCT user_id) as average
FROM customers
WHERE event_type = 'purchase'
group by day
order by day;