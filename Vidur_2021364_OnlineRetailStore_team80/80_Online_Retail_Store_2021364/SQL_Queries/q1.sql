CREATE VIEW lit AS
SELECT customer.customer_id, customer.customer_name, customer.contact_number
FROM customer,cart_prod
WHERE cart_prod.quantity>=8 AND cart_prod.cart_id=customer.customer_id AND customer.admin_id<>1;