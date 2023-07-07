create table coupon (
	coupon_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	percentage_discount INT NOT NULL,
	coupon_code VARCHAR(50) NOT NULL UNIQUE,
    admin_id INT NOT NULL,
    FOREIGN KEY (admin_id) REFERENCES admins (admin_id)
    ON DELETE CASCADE
);

insert into coupon (coupon_id, percentage_discount, coupon_code, admin_id) values 
 (1, 23, 'vsGzoRI0w',1),
 (2, 21, 'N8Yr78', 2),
 (3, 48, 'QOoIW6Ebt', 3),
 (4, 71, 'fuEPbl0OSOP',4),
 (5, 16, 'dT7a6y6Gozh', 5),
 (6, 37, 'RhjeHhc5i', 6),
 (7, 59, 'aEXdbz060', 7),
 (8, 53, 'wqeMJJE9ZWBK',8),
 (9, 40, 'N6b3tTZ5', 9),
 (10, 38, 'BAdPBiD6Ne', 10),
 (11, 27, 'dtd3d5', 11),
 (12, 26, 'e2EWt3',12),
 (13, 10, 'yY90ZxLSVxAn', 13),
 (14, 63, 'ryk1QQnP66Y', 14),
 (15, 45, 'PEnNG21Pms', 15),
 (16, 26, 'u36vJnI', 16),
 (17, 36, '4VUB4O3W8M', 17),
 (18, 43,'wVbt2c', 18),
 (19, 32, 'rIeTMhqpi5T4' , 19),
 (20, 42,'bhajb8O', 100);