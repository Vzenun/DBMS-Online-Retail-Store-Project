-- this tranction is used while we need to empty the cart
-- statement that we are going to write.
DELIMITER $$
-- Here we have defined the procedure which is going to be stored
CREATE PROCEDURE transaction_1() 
-- Now we begin the transaction
BEGIN
	START TRANSACTION;
    -- Delete all the cart_prod rows having cart_id=3
    -- thus emptying the cart
	DELETE FROM cart_prod
	WHERE cart_prod.cart_id=3;
    -- Here after emptying the cart we are going to set the value of the total_cost of al products in the cart to be equal to 0
    UPDATE cart
	SET total_cost=0
	WHERE cart_id=3;
	COMMIT; 
    -- Now we are going to commit the transaction
END;$$ 
-- Now we end the transaction
DELIMITER ;
-- Now we are going to reset the delimiter to semicolon

call Online_Retail_Store.transaction_1();