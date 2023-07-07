-- Product-wise order and sales count for a given month and year:

SELECT p.product_name, COUNT(o.order_id) as total_orders, SUM(o.total_cost) as total_sales
FROM orders o
JOIN cart c ON o.customer_id = c.cart_id
JOIN cart_prod cp ON c.cart_id = cp.cart_id
JOIN product p ON cp.prod_id = p.product_id
WHERE MONTH(order_placed_date) = 2 AND YEAR(order_placed_date) = 2022
GROUP BY p.product_name WITH ROLLUP
ORDER BY total_orders DESC;