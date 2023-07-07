create table cart_prod (
	prod_id INT,
    cart_id INT,
    quantity INT NOT NULL,
	CONSTRAINT cart_prod PRIMARY KEY (prod_id, cart_id),
	CONSTRAINT CPK_prod
	FOREIGN KEY (prod_id) REFERENCES product (product_id)
    ON DELETE CASCADE,
	CONSTRAINT CPK_cart
	FOREIGN KEY (cart_id) REFERENCES cart (cart_id)
    ON DELETE CASCADE
);

delimiter //
CREATE TRIGGER update_cart_total
AFTER INSERT ON cart_prod
FOR EACH ROW
BEGIN
  UPDATE cart
  SET total_cost = total_cost + (SELECT product.product_cost * NEW.quantity FROM product WHERE product.product_id = NEW.prod_id)
  WHERE cart_id = NEW.cart_id;
END;//
delimiter ;

delimiter //
CREATE TRIGGER cart_prod_quantity_check_insert_trigger
BEFORE INSERT ON cart_prod
FOR EACH ROW
BEGIN
    DECLARE product_qty INT;
    SELECT Quantity INTO product_qty FROM product WHERE product.product_id = NEW.prod_id;
    IF NEW.quantity > product_qty THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Cannot add product to cart: Quantity requested exceeds available stock';
    END IF;
END;//
delimiter ;

insert into cart_prod (prod_id,cart_id,quantity) values 
(99,39,8),
(64,31,4),
(57,51,6),
(22,9,3),
(55,100,6),
(34,72,6),
(9,69,8),
(98,13,5),
(39,64,4),
(60,17,3),
(52,26,7),
(93,11,5),
(56,41,5),
(24,59,5),
(32,73,2),
(51,54,8),
(86,68,7),
(40,68,6),
(65,15,2),
(83,25,1),
(74,48,1),
(40,88,1),
(11,58,6),
(25,28,3),
(23,58,1),
(70,77,8),
(59,23,1),
(14,88,5),
(21,42,2),
(5,35,2),
(22,72,3),
(33,10,6),
(62,85,5),
(14,91,2),
(47,45,5),
(74,1,8),
(51,100,1),
(84,51,2),
(82,67,1),
(91,77,7),
(93,88,6),
(74,44,8),
(59,96,4),
(71,81,2),
(2,9,3),
(69,67,5),
(11,65,7),
(93,80,5),
(68,93,5),
(16,29,1),
(38,52,3),
(44,20,6),
(76,63,8),
(74,99,7),
(97,37,5),
(56,72,5),
(67,100,6),
(1,50,7),
(89,91,6),
(4,62,3),
(69,11,5),
(6,83,3),
(36,19,4),
(46,15,4),
(98,75,2),
(50,76,2),
(41,32,2),
(3,46,3),
(77,79,7),
(100,45,5),
(35,39,8),
(76,98,7),
(3,71,5),
(5,84,8),
(4,93,7),
(74,17,1),
(47,57,1),
(50,16,6),
(36,21,7),
(10,96,2),
(52,85,2),
(48,44,6),
(6,21,3),
(71,24,6),
(60,70,6),
(76,34,6),
(78,99,4),
(83,39,7),
(100,71,3),
(14,94,7),
(59,77,1),
(27,63,1),
(20,52,1),
(92,69,1),
(3,69,1),
(64,3,1),
(37,76,1),
(97,7,1),
(90,77,1),
(94,17,1);