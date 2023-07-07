-- Number of products sold by brand for a given year:

SELECT p.Brand_name, COUNT(cp.prod_id) as total_products_sold
FROM orders o
JOIN cart c ON o.customer_id = c.cart_id
JOIN cart_prod cp ON c.cart_id = cp.cart_id
JOIN product p ON cp.prod_id = p.product_id
WHERE YEAR(order_placed_date) = 2022
GROUP BY p.Brand_name WITH ROLLUP;