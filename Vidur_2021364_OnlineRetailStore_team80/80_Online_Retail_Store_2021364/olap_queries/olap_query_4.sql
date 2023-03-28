-- Top 10 customers by total order value

SELECT c.customer_name, c.email_id, SUM(total_cost) as total_order_value
FROM orders o
JOIN customer c ON o.customer_id = c.customer_id
GROUP BY c.customer_name, c.email_id
ORDER BY total_order_value DESC
LIMIT 10;