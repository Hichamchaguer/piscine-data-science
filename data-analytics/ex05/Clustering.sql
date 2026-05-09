SELECT 
	user_id,
	COUNT(*) as frequency,
	SUM(price) as monetary,
	extract(day from (select max(event_time) from customers) - max(event_time)) as recency
FROM public.customers
where event_type='purchase'
group by user_id
order by user_id;