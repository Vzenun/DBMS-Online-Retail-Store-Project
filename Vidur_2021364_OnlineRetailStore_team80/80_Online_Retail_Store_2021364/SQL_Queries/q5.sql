-- Show total sales revenue by month and region:

SELECT 
  YEAR(order_placed_date) AS year,
  MONTH(order_placed_date) AS month,
  SUM(total_cost) AS revenue
FROM 
  orders
GROUP BY 
  YEAR(order_placed_date),
  MONTH(order_placed_date)