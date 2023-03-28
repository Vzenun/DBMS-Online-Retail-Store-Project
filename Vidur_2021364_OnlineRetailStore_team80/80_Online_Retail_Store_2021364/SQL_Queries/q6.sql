-- Average delivery time for each delivery boy

SELECT db.delivery_boy_name, AVG(TIMESTAMPDIFF(HOUR, o.order_placed_date, o.expected_delivery_time)) as avg_delivery_time
FROM orders o
JOIN delivery_boy db ON o.delivery_boy_id = db.delivery_boy_id
GROUP BY db.delivery_boy_name;