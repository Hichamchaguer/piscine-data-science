SELECT 
	user_id,
	COUNT(*) as frequency,
	SUM(price) as monetary,
	MAX(event_time) as last_purchase
FROM public.customers
where event_type='purchase'
group by user_id
order by user_id;