-- In this transaction admin is updating the quantity of the product
-- Set the delimiter to $$ so that within the stored procedure semicolons don't terminate the CREATE PROCEDURE
-- statement that we are going to write.
DELIMITER $$
-- Here we have defined the procedure which is going to be stored
CREATE PROCEDURE transaction_3() 
-- Now we begin the transaction
BEGIN
	START TRANSACTION;
    -- updating the quantity of the product having product id=5
    UPDATE product
	SET product.Quantity=product.Quantity+500
	WHERE product_id=5;
	COMMIT; 
    -- Now we are going to commit the transaction
END;$$ 
-- Now we end the transaction
DELIMITER ;
-- Now we are going to reset the delimiter to semicolon

call Online_Retail_Store.transaction_3();