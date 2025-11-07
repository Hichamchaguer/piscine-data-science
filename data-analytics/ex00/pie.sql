SELECT event_type, COUNT(5) FROM costomers
GROUP BY event_type
ORDER BY price DESC
LIMIT 5;
