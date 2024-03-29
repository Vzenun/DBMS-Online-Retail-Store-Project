create table product_feedback (
	feedback_id INT NOT NULL UNIQUE AUTO_INCREMENT,
	rating_given DECIMAL(3,2) NOT NULL,
	review TEXT NOT NULL,
	likes INT,
	date_published DATE NOT NULL,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES product (product_id)
    ON DELETE CASCADE,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
    ON DELETE CASCADE
);

insert into product_feedback (feedback_id, rating_given, review, likes, date_published, product_id, customer_id) values 
 (1, 0.94, 'arcu libero rutrum ac lobortis vel dapibus at diam nam tristique tortor', 5974, '2022-05-16', 100, 1),
 (2, 0.18, 'penatibus et magnis dis parturient montes nascetur ridiculus mus vivamus vestibulum sagittis sapien cum sociis natoque', 8979, '2023-01-22', 2, 2),
 (3, 1.84, 'nisl nunc nisl duis bibendum felis sed interdum venenatis turpis enim blandit mi in porttitor pede justo eu', 7501, '2022-07-28', 3, 3),
 (4, 2.09, 'ante vel ipsum praesent blandit lacinia erat vestibulum sed magna at nunc commodo placerat praesent blandit nam', 5366, '2022-11-25', 64, 14),
 (5, 4.28, 'massa donec dapibus duis at velit eu est congue elementum in hac habitasse', 2606, '2022-06-24', 5, 5),
 (6, 2.35, 'quam fringilla rhoncus mauris enim leo rhoncus sed vestibulum sit amet', 3072, '2022-02-25', 6, 6),
 (7, 4.41, 'vel augue vestibulum rutrum rutrum neque aenean auctor gravida sem praesent id massa', 7198, '2022-11-17', 7, 7),
 (8, 0.9, 'facilisi cras non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel', 0, '2023-01-18', 9, 8),
 (9, 2.38, 'condimentum curabitur in libero ut massa volutpat convallis morbi odio odio elementum eu interdum eu tincidunt in leo maecenas pulvinar', 8256, '2022-03-16', 9, 9),
 (10, 3.04, 'non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel nulla eget eros elementum pellentesque', 8707, '2022-09-22', 10, 10),
 (11, 2.44, 'nec nisi volutpat eleifend donec ut dolor morbi vel lectus', 2252, '2022-12-11', 11, 11),
 (12, 2.13, 'sapien a libero nam dui proin leo odio porttitor id', 338, '2022-10-13', 12, 12),
 (13, 0.07, 'at turpis a pede posuere nonummy integer non velit donec diam neque vestibulum eget', 5153, '2022-12-17', 13, 13),
 (14, 0.62, 'quis odio consequat varius integer ac leo pellentesque ultrices mattis odio donec', 7608, '2022-11-12', 14, 14),
 (15, 0.11, 'in lacus curabitur at ipsum ac tellus semper interdum mauris ullamcorper purus sit amet nulla quisque arcu', 9256, '2022-12-09', 15, 15),
 (16, 4.08, 'dui nec nisi volutpat eleifend donec ut dolor morbi vel lectus in quam fringilla rhoncus', 4478, '2022-09-28', 16, 16),
 (17, 4.61, 'interdum in ante vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae duis faucibus accumsan', 1228, '2023-02-05', 17, 17),
 (18, 0.01, 'vitae nisl aenean lectus pellentesque eget nunc donec quis orci eget orci vehicula condimentum curabitur in libero ut', 7020, '2022-03-10', 18, 18),
 (19, 1.36, 'varius nulla facilisi cras non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus', 1386, '2022-04-30', 19, 19),
 (20, 4.84, 'augue vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere', 38, '2022-09-05', 20, 20),
 (21, 4.73, 'nunc vestibulum ante ipsum primis in faucibus orci luctus et', 5659, '2022-05-20', 21, 21),
 (22, 1.8, 'sit amet lobortis sapien sapien non mi integer ac neque duis bibendum morbi non quam nec dui luctus rutrum', 1959, '2022-09-08', 22, 22),
 (23, 2.45, 'tincidunt in leo maecenas pulvinar lobortis est phasellus sit amet', 8296, '2022-12-01', 23, 23),
 (24, 1.68, 'lacus curabitur at ipsum ac tellus semper interdum mauris ullamcorper purus sit amet nulla', 9674, '2022-08-10', 24, 4),
 (25, 0.48, 'proin eu mi nulla ac enim in tempor turpis nec euismod', 7612, '2022-12-25', 25, 25),
 (26, 0.22, 'dui proin leo odio porttitor id consequat in consequat ut nulla sed accumsan felis ut at dolor', 5653, '2022-07-30', 26, 6),
 (27, 0.08, 'mi sit amet lobortis sapien sapien non mi integer ac neque duis bibendum morbi non quam nec dui luctus rutrum', 3736, '2023-02-05', 7, 27),
 (28, 0.14, 'at dolor quis odio consequat varius integer ac leo pellentesque ultrices mattis odio donec vitae', 1437, '2022-05-17', 2, 28),
 (29, 3.0, 'luctus nec molestie sed justo pellentesque viverra pede ac diam cras', 7366, '2022-07-08', 29, 29),
 (30, 0.32, 'odio curabitur convallis duis consequat dui nec nisi volutpat eleifend donec ut dolor morbi vel lectus in', 9723, '2022-04-17', 30, 30),
 (31, 1.56, 'non ligula pellentesque ultrices phasellus id sapien in sapien iaculis congue vivamus metus arcu adipiscing molestie hendrerit', 6238, '2022-05-03', 31, 31),
 (32, 3.23, 'amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus id sapien', 926, '2022-07-31', 32, 32),
 (33, 2.74, 'vel sem sed sagittis nam congue risus semper porta volutpat quam pede lobortis ligula sit amet eleifend pede', 2217, '2023-01-29', 33, 33),
 (34, 4.53, 'sem duis aliquam convallis nunc proin at turpis a pede posuere nonummy integer non', 2473, '2022-07-13', 34, 34),
 (35, 0.21, 'massa tempor convallis nulla neque libero convallis eget eleifend luctus ultricies eu nibh quisque id justo sit amet', 7808, '2022-09-01', 35, 35),
 (36, 3.95, 'ac nibh fusce lacus purus aliquet at feugiat non pretium quis lectus suspendisse potenti in', 8844, '2022-06-24', 36, 36),
 (37, 4.93, 'nulla eget eros elementum pellentesque quisque porta volutpat erat quisque erat eros viverra eget congue eget semper', 5761, '2022-06-02', 37, 37),
 (38, 3.63, 'non ligula pellentesque ultrices phasellus id sapien in sapien iaculis congue vivamus metus arcu adipiscing', 6760, '2022-07-05', 38, 38),
 (39, 1.36, 'luctus tincidunt nulla mollis molestie lorem quisque ut erat curabitur gravida nisi at nibh in', 6842, '2022-03-28', 39, 39),
 (40, 0.86, 'quis orci nullam molestie nibh in lectus pellentesque at nulla suspendisse potenti cras in purus eu magna vulputate', 9396, '2023-01-08', 40, 40),
 (41, 4.78, 'ligula in lacus curabitur at ipsum ac tellus semper interdum', 8751, '2022-09-03', 41, 41),
 (42, 4.45, 'lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat vestibulum sed magna at nunc commodo placerat', 3439, '2022-04-19', 42, 42),
 (43, 1.23, 'in felis donec semper sapien a libero nam dui proin leo odio porttitor', 681, '2022-05-21', 43, 43),
 (44, 2.69, 'eget eleifend luctus ultricies eu nibh quisque id justo sit amet sapien dignissim vestibulum vestibulum ante ipsum', 2783, '2022-10-15', 44, 44),
 (45, 0.88, 'in lectus pellentesque at nulla suspendisse potenti cras in purus', 7375, '2022-11-21', 45, 45),
 (46, 4.21, 'mi nulla ac enim in tempor turpis nec euismod scelerisque quam turpis adipiscing lorem', 9481, '2022-12-29', 46, 46),
 (47, 4.44, 'cubilia curae mauris viverra diam vitae quam suspendisse potenti nullam porttitor lacus at', 6558, '2023-01-08', 47, 47),
 (48, 2.9, 'risus auctor sed tristique in tempus sit amet sem fusce consequat', 9844, '2022-12-16', 48, 48),
 (49, 1.44, 'erat fermentum justo nec condimentum neque sapien placerat ante nulla justo', 4405, '2022-04-18', 49, 49),
 (50, 0.13, 'leo rhoncus sed vestibulum sit amet cursus id turpis integer aliquet massa id lobortis', 9214, '2022-08-23', 50, 50),
 (51, 4.85, 'dapibus dolor vel est donec odio justo sollicitudin ut suscipit a feugiat', 3129, '2022-12-11', 51, 51),
 (52, 1.44, 'ornare imperdiet sapien urna pretium nisl ut volutpat sapien arcu sed augue aliquam', 7151, '2022-03-18', 52, 52),
 (53, 3.87, 'mus etiam vel augue vestibulum rutrum rutrum neque aenean auctor gravida sem praesent id massa id nisl venenatis', 3544, '2022-12-03', 53, 53),
 (54, 3.67, 'condimentum neque sapien placerat ante nulla justo aliquam quis turpis eget elit sodales scelerisque mauris sit amet eros suspendisse accumsan', 5926, '2023-02-01', 54, 54),
 (55, 3.73, 'congue eget semper rutrum nulla nunc purus phasellus in felis donec semper sapien a libero', 1738, '2022-11-28', 55, 55),
 (56, 3.65, 'diam cras pellentesque volutpat dui maecenas tristique est et tempus semper est quam', 5392, '2022-12-13', 56, 56),
 (57, 0.9, 'libero non mattis pulvinar nulla pede ullamcorper augue a suscipit nulla elit ac nulla sed vel enim sit amet', 9454, '2022-07-03', 57, 57),
 (58, 3.88, 'donec posuere metus vitae ipsum aliquam non mauris morbi non lectus aliquam sit amet diam in magna bibendum imperdiet nullam', 6222, '2022-07-28', 58, 58),
 (59, 4.25, 'varius nulla facilisi cras non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel', 1928, '2022-02-27', 59, 59),
 (60, 2.95, 'eget rutrum at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat vestibulum', 7342, '2022-10-04', 60, 60),
 (61, 3.83, 'nam dui proin leo odio porttitor id consequat in consequat ut nulla sed accumsan felis ut', 4916, '2022-10-30', 61, 61),
 (62, 3.85, 'luctus ultricies eu nibh quisque id justo sit amet sapien dignissim vestibulum vestibulum', 7580, '2022-09-23', 62, 62),
 (63, 2.61, 'ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae nulla dapibus dolor vel', 902, '2022-12-02', 63, 63),
 (64, 1.37, 'vestibulum sit amet cursus id turpis integer aliquet massa id lobortis convallis tortor risus dapibus augue vel', 8003, '2022-05-29', 64, 64),
 (65, 0.52, 'nibh ligula nec sem duis aliquam convallis nunc proin at turpis a pede posuere nonummy integer non velit', 5186, '2022-06-04', 65, 65),
 (66, 1.35, 'lectus pellentesque at nulla suspendisse potenti cras in purus eu magna vulputate luctus cum sociis natoque penatibus et magnis', 6737, '2023-01-03', 66, 66),
 (67, 1.59, 'maecenas leo odio condimentum id luctus nec molestie sed justo pellentesque viverra pede ac diam cras', 9407, '2022-08-11', 67, 67),
 (68, 4.82, 'pede malesuada in imperdiet et commodo vulputate justo in blandit ultrices enim', 133, '2022-10-12', 68, 68),
 (69, 0.88, 'posuere nonummy integer non velit donec diam neque vestibulum eget vulputate ut ultrices vel augue vestibulum', 3776, '2022-09-04', 69, 69),
 (70, 1.9, 'lectus pellentesque at nulla suspendisse potenti cras in purus eu magna vulputate luctus cum sociis natoque penatibus et magnis dis', 4619, '2022-11-09', 70, 70),
 (71, 1.47, 'vel augue vestibulum ante ipsum primis in faucibus orci luctus et', 6670, '2023-01-25', 71, 71),
 (72, 3.06, 'integer ac neque duis bibendum morbi non quam nec dui', 7785, '2022-11-13', 72, 72),
 (73, 1.72, 'dui nec nisi volutpat eleifend donec ut dolor morbi vel lectus in quam fringilla rhoncus mauris enim leo rhoncus sed', 1713, '2022-05-26', 73, 73),
 (74, 3.27, 'a feugiat et eros vestibulum ac est lacinia nisi venenatis tristique fusce', 2027, '2022-04-23', 74, 74),
 (75, 1.82, 'quam nec dui luctus rutrum nulla tellus in sagittis dui', 2909, '2022-04-08', 75, 75),
 (76, 2.94, 'posuere cubilia curae donec pharetra magna vestibulum aliquet ultrices erat tortor sollicitudin mi sit', 1207, '2022-07-17', 76, 76),
 (77, 4.0, 'augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt', 774, '2022-08-23', 77, 77),
 (78, 1.55, 'luctus et ultrices posuere cubilia curae mauris viverra diam vitae quam suspendisse potenti nullam porttitor lacus', 5750, '2022-12-24', 78, 78),
 (79, 3.66, 'ridiculus mus vivamus vestibulum sagittis sapien cum sociis natoque penatibus et magnis dis parturient montes nascetur', 5771, '2022-10-26', 79, 79),
 (80, 2.83, 'nisl nunc nisl duis bibendum felis sed interdum venenatis turpis enim blandit mi in porttitor pede justo', 1922, '2022-10-10', 80, 80),
 (81, 0.23, 'lacus curabitur at ipsum ac tellus semper interdum mauris ullamcorper purus sit amet nulla quisque arcu', 883, '2022-08-27', 81, 81),
 (82, 4.94, 'fusce congue diam id ornare imperdiet sapien urna pretium nisl ut volutpat sapien arcu sed augue aliquam erat', 8806, '2022-12-31', 82, 82),
 (83, 0.67, 'porttitor pede justo eu massa donec dapibus duis at velit eu est congue elementum', 7858, '2022-11-15', 83, 83),
 (84, 3.66, 'sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus mus', 3144, '2022-12-09', 84, 84),
 (85, 4.86, 'posuere cubilia curae duis faucibus accumsan odio curabitur convallis duis consequat', 7455, '2022-11-13', 85, 85),
 (86, 0.85, 'in magna bibendum imperdiet nullam orci pede venenatis non sodales sed tincidunt eu felis fusce posuere felis sed', 1999, '2022-07-21', 86, 86),
 (87, 1.39, 'nec euismod scelerisque quam turpis adipiscing lorem vitae mattis nibh ligula nec sem', 370, '2022-05-20', 87, 87),
 (88, 4.48, 'luctus et ultrices posuere cubilia curae nulla dapibus dolor vel est donec', 9255, '2022-03-28', 88, 88),
 (89, 0.78, 'nam ultrices libero non mattis pulvinar nulla pede ullamcorper augue a suscipit nulla elit ac nulla sed', 8619, '2022-11-19', 89, 89),
 (90, 4.78, 'suspendisse potenti in eleifend quam a odio in hac habitasse platea dictumst maecenas ut massa quis augue luctus tincidunt nulla', 7140, '2022-08-09', 90, 90),
 (91, 3.21, 'massa quis augue luctus tincidunt nulla mollis molestie lorem quisque ut', 1249, '2022-07-08', 91, 91),
 (92, 4.04, 'nulla mollis molestie lorem quisque ut erat curabitur gravida nisi', 3672, '2022-04-19', 92, 92),
 (93, 4.36, 'ipsum ac tellus semper interdum mauris ullamcorper purus sit amet', 9217, '2022-05-26', 93, 93),
 (94, 1.4, 'id nulla ultrices aliquet maecenas leo odio condimentum id luctus nec molestie sed justo pellentesque viverra pede ac diam', 9982, '2022-03-06', 94, 94),
 (95, 4.38, 'sagittis sapien cum sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus mus etiam', 1003, '2022-02-19', 95, 95),
 (96, 4.97, 'odio in hac habitasse platea dictumst maecenas ut massa quis augue luctus tincidunt nulla mollis', 62, '2022-04-10', 96, 96),
 (97, 0.98, 'libero ut massa volutpat convallis morbi odio odio elementum eu interdum eu', 7646, '2022-05-27', 97, 97),
 (98, 3.43, 'nunc commodo placerat praesent blandit nam nulla integer pede justo lacinia eget tincidunt eget tempus', 3623, '2022-09-10', 98, 98),
 (99, 0.77, 'fermentum donec ut mauris eget massa tempor convallis nulla neque libero convallis', 104, '2022-04-14', 99, 99),
 (100, 1.55, 'cras non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel nulla', 2672, '2022-12-29', 100, 100);
 