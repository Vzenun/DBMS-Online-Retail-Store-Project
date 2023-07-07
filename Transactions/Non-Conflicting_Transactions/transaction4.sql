-- In this transaction quantity is being decreased of the product during the checkout
-- Set the delimiter to $$ so that within the stored procedure semicolons don't terminate the CREATE PROCEDURE
-- statement that we are going to write.
DELIMITER $$
-- Here we have defined the procedure which is going to be stored
CREATE PROCEDURE transaction_4() 
-- Now we begin the transaction
BEGIN
	START TRANSACTION;
    -- updating the quantity of the product during checkout having product id=5 or product_id=9 during the checkout process
    UPDATE product
	SET product.Quantity=product.Quantity-30
	WHERE product_id=5 or product_id=9;
	COMMIT; 
    -- Now we are going to commit the transaction
END;$$ 
-- Now we end the transaction
DELIMITER ;
-- Now we are going to reset the delimiter to semicolon

call Online_Retail_Store.transaction_4();