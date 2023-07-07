-- this tranction is used while we need to empty the cart
-- statement that we are going to write.
DELIMITER $$
-- Here we have defined the procedure which is going to be stored
CREATE PROCEDURE transaction_1() 
-- Now we begin the transaction
BEGIN
	START TRANSACTION;
	UPDATE product
	SET product.Quantity=product.Quantity-20
	WHERE product_id=5;
    insert into orders (delivery_boy_id, total_cost, delivery_address, order_status, order_placed_date, expected_delivery_time, customer_id) values 
    (12, '3400.00', '3rd floor', 'Delivered', '2022-12-10', '2023-07-01', 11);
	COMMIT; 
    -- Now we are going to commit the transaction
END;$$ 
-- Now we end the transaction
DELIMITER ;
-- Now we are going to reset the delimiter to semicolon

call Online_Retail_Store.transaction_1();