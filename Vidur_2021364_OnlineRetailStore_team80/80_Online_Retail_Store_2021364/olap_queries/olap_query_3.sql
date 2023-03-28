-- Total sales by product category and month

SELECT category_name, YEAR(order_placed_date) as year, MONTH(order_placed_date) as month, SUM(o.total_cost) as total_sales
FROM orders o
JOIN cart c ON o.customer_id = c.cart_id
JOIN cart_prod cp ON c.cart_id = cp.cart_id
JOIN product p ON cp.prod_id = p.product_id
JOIN categ_prod cg ON p.product_id = cg.prod_id
JOIN category ct ON cg.categ_id = ct.category_id
GROUP BY category_name, YEAR(order_placed_date), MONTH(order_placed_date) WITH ROLLUP
ORDER BY category_name, year, month;