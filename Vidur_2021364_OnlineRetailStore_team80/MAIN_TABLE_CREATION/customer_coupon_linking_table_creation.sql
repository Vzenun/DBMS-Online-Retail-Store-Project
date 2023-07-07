create table customer_coupon (
	coupon_id INT,
    customer_id INT,
	CONSTRAINT customer_coupon PRIMARY KEY (coupon_id, customer_id),
	CONSTRAINT CPK_coupon
	FOREIGN KEY (coupon_id) REFERENCES coupon (coupon_id)
    ON DELETE CASCADE,
	CONSTRAINT CPK_custom
	FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
    ON DELETE CASCADE
);

insert into customer_coupon (coupon_id, customer_id) values 
(1,1),
(2,1),
(3,1),
(4,1),
(5,1),
(6,1),
(7,1),
(8,1),
(9,1),
(10,1);