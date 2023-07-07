
-- The below transaction is used to update the status of the cart
-- Set the delimiter to $$ so that within the stored procedure semicolons don't terminate the CREATE PROCEDURE
-- statement that we are going to write.
DELIMITER $$
-- Here we have defined the procedure which is going to be stored
CREATE PROCEDURE transaction_2() 
-- Now we begin the transaction
BEGIN
	START TRANSACTION;
    -- Update the status of the order from not delivered to delivered
	UPDATE orders
	SET order_status = 'Delivered'
	WHERE order_status = 'Not delivered' 
	AND delivery_boy_id = 11
	AND order_id = 2;
	COMMIT; 
    -- Now we are going to commit the transaction
END;$$ 
-- Now we end the transaction
DELIMITER ;
-- Now we are going to reset the delimiter to semicolon

call Online_Retail_Store.transaction_2();