-- statement that we are going to write.
DELIMITER $$
-- Here we have defined the procedure which is going to be stored
CREATE PROCEDURE transaction_121() 
-- Now we begin the transaction
BEGIN
    START TRANSACTION;
    SELECT product.Quantity FROM product
    WHERE product_id =5
    INTO @present_quantity;
    IF @present_quantity < 320 THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT =
        'Requested quantity is greater than present_quantity of the product in the inventory';
    ELSE
		SELECT * FROM product WHERE product_id = 5 FOR UPDATE;
        UPDATE product
        SET product.Quantity=product.Quantity-320
        WHERE product_id=5;
        insert into orders (delivery_boy_id, total_cost, delivery_address, order_status, order_placed_date, expected_delivery_time, customer_id) values 
        (15, '54400.00', '23rd floor', 'Delivered', '2022-12-15', '2023-07-04', 13);
    END IF;
    COMMIT; 
    -- Now we are going to commit the transaction
END;$$ 
-- Now we end the transaction
DELIMITER ;
-- Now we are going to reset the delimiter to semicolon

call Online_Retail_Store.transaction_121();
