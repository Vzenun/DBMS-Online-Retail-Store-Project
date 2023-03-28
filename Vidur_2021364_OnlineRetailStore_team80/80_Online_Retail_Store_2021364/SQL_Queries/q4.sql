SELECT c.customer_id, c.customer_name,o.order_id
FROM Online_Retail_Store.customer as c
LEFT JOIN Online_Retail_Store.orders as o ON c.customer_id = o.customer_id
ORDER BY c.customer_id;