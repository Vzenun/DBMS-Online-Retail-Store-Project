import mysql.connector
from mysql.connector import Error
import sys

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Online_Retail_Store',
                                         user='root',
                                         password='Vidurg@1102')
    cursor = connection.cursor()

    def start():
        print("Welcome to the Vidur Online Retail Store")
        print("Choose the option from the given below menu: ")
        print("1. Enter as Admin")
        print("2. Enter as Customer")
        print("3. Enter as Dealer")
        print("4. Enter as Delivery Boy")
        print("5. Exit the Application")

        ans=int(input("Enter the choice: "))
        print()
        if(ans==1):
            admin()
        elif(ans==2):
            customer()
        elif(ans==3):
            dealer()
        elif(ans==4):
            delivery_boy()
        elif(ans==5):
            sys.exit(0)
        else:
            print("Sorry, wrong input has been given try again...")
            start()
        return
    
    def customer():
        print("Enter the choice from given below: ")
        print("1. Login")
        print("2. Go Back")
        num=int(input("Enter: "))
        if(num==1): 
            print()
            print("Enter the credentials: ")
            usrname=input("Enter your username: ")
            pwd=input("Enter your password: ")
            mySql_sql_select_Query ="""
            SELECT customer_username, customer_password,customer_id,customer_name FROM Online_Retail_Store.customer
            """
            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()
            for row in result:
                if(row[0]==usrname and row[1]==pwd):
                    # print(row[0],row[1])
                    print(f'Welcome {row[3]}')
                    id=int(row[2])
                    customer_query(id)
                    customer()
                    return
            print("Sorry, Wrong Credentials,try again!!!")
            customer()
        elif(num==2):
            start()
        else:
            print("Sorry, wrong input has been given try again...")
            customer()
        return
    
    def customer_query(id):
        print("1. View Cart")
        print("2. Browse Products")
        print("3. Add/Edit quantity of product to cart")
        print("4. View Coupons")
        print("5. Empty Cart")
        print("6. Checkout Cart")
        print("7. Log out")

        ans=int(input("Enter the choice: "))
        if(ans==1):
            mySql_sql_select_Query ="""
            SELECT product.product_name, product.product_cost, cart_prod.quantity,product.product_cost*cart_prod.quantity as Total_cost
            FROM product
            JOIN cart_prod ON product.product_id = cart_prod.prod_id
            WHERE cart_prod.cart_id = """+str(id)+";"
            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()
            print()
            print(f'There are currently {len(result)} products in the cart')
            print(f'Product name   Product Cost   Quantity   Total_cost')
            grand_total=0
            for row in result:
                print(f'{row[0]}        {row[1]}        {row[2]}         {row[3]}')
                grand_total+=int(row[3])
            print()
            print(f'Grand Total : {grand_total}')
            print()
            customer_query(id)
        elif(ans==2):
            mySql_sql_select_Query ="""
            SELECT product.product_name,product.Brand_name,product.product_cost FROM Online_Retail_Store.product;"""
            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()
            print()
            print(f'Product name   Brand Name   Product Cost')
            for row in result:
                print(f'{row[0]}        {row[1]}        {row[2]}')
            print()
            customer_query(id)
        elif(ans==3):
            pr_name=input("Enter the product name: ")
            quantity=int(input("Enter the quantity of product: "))
            mySql_sql_select_Query ="""
            SELECT product.product_id,Quantity,product.product_cost
            FROM product
            WHERE product.product_name = '"""+pr_name+"';"
            #print(mySql_sql_select_Query)
            mySql_sql_select_Query2="""
            SELECT prod_id,cart_id,quantity FROM Online_Retail_Store.cart_prod;
            """
            #print(mySql_sql_select_Query2)
            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()
            #print(1)
            cursor.execute(mySql_sql_select_Query2)
            result2 = cursor.fetchall()
            #print(2)
            #print(len(result))
            if(len(result)==0):
                print("Sorry, no such product name exists, try again with correct product name..")
                customer_query(id)
                return
            cost_of_product=int(result[0][2])
            #print(cost_of_product)
            flag=0
            qty=0
            #print(len(result2))
            for ro in result2:
                #print(ro)
                if(int(result[0][0])==int(ro[0]) and id==int(ro[1])):
                    print(result[0][0],ro[0])
                    print(id,ro[1])
                    flag=1
                    qty=int(ro[2])
                    break
            #print(3)
            if(flag==0):
                #print(4)
                if(int(result[0][1])>=quantity):
                    my_query="""
                    insert into cart_prod (prod_id,cart_id,quantity) values 
                    ('"""
                    #print(my_query)
                    my_query=my_query+str(result[0][0])
                    #print(my_query)
                    my_query=my_query+"',"+str(id)+",'"+str(quantity)+"');"
                    #print(my_query)
                    try:
                        cursor.execute(my_query)
                        connection.commit()
                        print()
                        print(f'Your cart has been updated succesfully.')
                        print()
                    except:
                        connection.rollback()
                        print()
                        print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                        print()
                else:
                    print("Sorry, product you have requested is out of stock")
            else:
                #print(5)
                if(int(result[0][1])>=quantity):
                    my_query2="""
                    SELECT total_cost FROM Online_Retail_Store.cart
                    WHERE cart_id="""+str(id)+";"
                    
                    cursor.execute(my_query2)
                    answer=cursor.fetchall()

                    calcu=int(answer[0][0])-cost_of_product*qty+cost_of_product*quantity

                    my_query="""
                    UPDATE cart_prod
                    SET quantity="""+str(quantity)+"""
                    WHERE cart_id="""+str(id)+""" and prod_id="""+str(result[0][0])+""";"""

                    try:
                        cursor.execute(my_query)
                        connection.commit()
                        print()
                        print(f'Your quantity of product has been updated succesfully.')
                        print()
                    except:
                        connection.rollback()
                        print()
                        print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                        print()
                    
                    my_query="""
                    UPDATE cart
                    SET total_cost="""+str(calcu)+"""
                    WHERE cart_id="""+str(id)+""";"""
                    try:
                        cursor.execute(my_query)
                        connection.commit()
                        print()
                        print(f'Your cart has been updated succesfully.')
                        print()
                    except:
                        connection.rollback()
                        print()
                        print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                        print()

                else:
                    print("Sorry, product you have requested is out of stock")

            customer_query(id)

        elif(ans==5):
            empty_cart(id)
            customer_query(id)

        elif(ans==4):
            mySql_sql_select_Query ="""
            SELECT coupon.coupon_code,coupon.percentage_discount
            FROM coupon
            INNER JOIN customer_coupon ON coupon.coupon_id = customer_coupon.coupon_id
            WHERE customer_coupon.customer_id = """+str(id)+""";"""
            cursor.execute(mySql_sql_select_Query)
            result=cursor.fetchall()
            print(f'There are currently {len(result)} coupons allocated to you.')
            print("Coupon_Code     Percentage_discount")
            for row in result:
                print(f'{row[0]}   {row[1]}')
            customer_query(id)

        elif(ans==6):
            my_query2="""
            SELECT total_cost FROM Online_Retail_Store.cart
            WHERE cart_id="""+str(id)+";"
            cursor.execute(my_query2)
            answer=cursor.fetchall()
            if(int(answer[0][0])==0):
                print("Sorry nothing to checkout your cart is alreaady empty.")
            else:
                cost=int(answer[0][0])
                percent=0
                asku=input("Do you want to apply the coupon code on the order(YES/NO):")
                if(asku=='NO'):
                    percent=0
                else:
                    coupon_code=input("Enter the coupon code:")
                    mySql_sql_select_Query ="""
                    SELECT coupon.percentage_discount,coupon.coupon_id
                    FROM coupon
                    INNER JOIN customer_coupon ON coupon.coupon_id = customer_coupon.coupon_id
                    WHERE coupon.coupon_code= '"""+coupon_code+"""' and customer_coupon.customer_id = """+str(id)+""";"""
                    cursor.execute(mySql_sql_select_Query)
                    res=cursor.fetchall()
                    if(len(res)==0):
                        print("No such coupon code is available.")
                    else:
                        percent=int(res[0][0])
                        cost=cost-cost*(percent)/100
                        print("Coupon Applied Successfully")
                        coupon_id=res[0][1]
                        mySql_sql_select_Query="""
                        DELETE FROM customer_coupon
                        WHERE customer_coupon.customer_id="""+str(id)+""" and customer_coupon.coupon_id= """+str(coupon_id)+""";
                        """
                        try:
                            cursor.execute(mySql_sql_select_Query)
                            connection.commit()
                            print()
                            print("Coupon Applied Successfully")
                            print()
                        except:
                            connection.rollback()
                            print()
                            print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                            print()
                            customer_query(id)
                date=input("Enter the date: ")
                expected_date=input("Enter the date upto which you can expect delivery(make it atleast 7 days later than the date at which you placed the order): ")
                address=input("Enter the delivery address: ")
                order_status='Not delivered'
                empty_cart_with_checkout(id)
                my_query="""
                insert into orders (delivery_boy_id, total_cost, delivery_address, order_status, order_placed_date, expected_delivery_time, customer_id) values 
                (6, '"""+str(cost)+"""', '"""+str(address)+"""', '"""+str(order_status)+"""', '"""+str(date)+"""', '"""+str(expected_date)+"""', '"""+str(id)+"""');
                """
                print(2)
                try:
                    cursor.execute(my_query)
                    connection.commit()
                    print()
                    print(f'Your order has been placed succesfully.')
                    print()
                except:
                    connection.rollback()
                    print()
                    print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                    print()
            customer_query(id)
        elif(ans==7):
            customer()
        else:
            print("Sorry, wrong input has been given try again...")
            customer_query(id)
        return
    
    def empty_cart(id):
        if(True):
            mySql_sql_select_Query ="""
            DELETE FROM cart_prod
            WHERE cart_prod.cart_id= """+str(id)+""";"""
            try:
                cursor.execute(mySql_sql_select_Query)
                connection.commit()
                print()
                print(f'Your cart has been emptied succesfully.')
                print()
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                print()

            my_query="""
            UPDATE cart
            SET total_cost=0
            WHERE cart_id="""+str(id)+""";"""
            try:
                cursor.execute(my_query)
                connection.commit()
                print()
                print(f'Your cart has been updated succesfully.')
                print()
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                print()
    def empty_cart_with_checkout(id):
        if(True):
            mySql_sql_select_Query ="""
            SELECT cart_prod.prod_id,cart_prod.quantity
            FROM cart_prod
            WHERE cart_prod.cart_id="""+str(id)+""";"""
            cursor.execute(mySql_sql_select_Query)
            result=cursor.fetchall()
            flag=0
            for row in result:
                my_query="""
                SELECT product.Quantity
                FROM product
                WHERE product.product_id= """+str(row[0])+""";"""
                cursor.execute(my_query)
                armer=cursor.fetchall()
                if(int(row[1])>int(armer[0][0])):
                    flag=1
            if(flag==1):
                print("Sorry unable to checkout due to insufficient amount of product in inventory.")
                customer_query(id)
            mySql_sql_select_Query ="""
            SELECT cart_prod.prod_id,cart_prod.quantity
            FROM cart_prod
            WHERE cart_prod.cart_id="""+str(id)+""";"""
            cursor.execute(mySql_sql_select_Query)
            result=cursor.fetchall()
            for row in result:
                my_query=="""
                SELECT product.Quantity
                FROM cart_prod
                WHERE product.product_id= """+str(row[0])+""";"""
                cursor.execute(my_query)
                armer=cursor.fetchall()
                my_query="""
                UPDATE product
                SET Quantity="""+str(int(armer[0][0])-int(row[1]))+"""
                WHERE product_id="""+str(row[0])+""";"""
                try:
                    cursor.execute(my_query)
                    connection.commit()
                    print()
                    print(f'Your cart has been updated succesfully.')
                    print()
                except:
                    connection.rollback()
                    print()
                    print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                    print()
            mySql_sql_select_Query ="""
            DELETE FROM cart_prod
            WHERE cart_prod.cart_id= """+str(id)+""";"""
            try:
                cursor.execute(mySql_sql_select_Query)
                connection.commit()
                print()
                print(f'Your cart has been emptied succesfully.')
                print()
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                print()
            my_query="""
            UPDATE cart
            SET total_cost=0
            WHERE cart_id="""+str(id)+""";"""
            try:
                cursor.execute(my_query)
                connection.commit()
                print()
                print(f'Your cart has been updated succesfully.')
                print()
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
    def dealer():
        print("Enter the choice from given below: ")
        print("1. Login")
        print("2. Go Back")
        num=int(input("Enter: "))
        if(num==1): 
            print()
            print("Enter the credentials: ")
            usrname=input("Enter your username: ")
            pwd=input("Enter your password: ")
            mySql_sql_select_Query ="""
            SELECT dealer_username, dealer_password,dealer_id FROM Online_Retail_Store.dealer
            """
            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()
            for row in result:
                if(row[0]==usrname and row[1]==pwd):
                    print(f'Welcome {row[0]}')
                    id=int(row[2])
                    dealer_query(id)
                    dealer()
            print("Sorry, Wrong Credentials,try again!!!")
            dealer()
        elif(num==2):
            start()
        else:
            print("Sorry, wrong input has been given try again...")
            dealer()
        return
    
    def dealer_query(id):
        print("1. View Products currently being sold")
        print("2. Log out")
        ans=int(input("Enter the choice: "))
        if(ans==1):
            mySql_sql_select_Query ="""
            SELECT product.product_id,product.product_name
            FROM product
            JOIN deal_prod ON product.product_id = deal_prod.prod_id
            WHERE deal_prod.deal_id = """+str(id)+";"
            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()
            print()
            print(f'There are currently {len(result)} products sold by you')
            print(f'Product_id    Product_name')
            for row in result:
                print(row[0],row[1])
            print()
            dealer_query(id)
        elif(ans==2):
            dealer()
        else:
            print("Sorry, wrong input has been given try again...")
            dealer_query(id)
        return
    
    def delivery_boy():
        print("Enter the choice from given below: ")
        print("1. Login")
        print("2. Go Back")
        num=int(input("Enter: "))
        if(num==1): 
            print("Enter the credentials: ")
            usrname=input("Enter your username: ")
            pwd=input("Enter your password: ")
            mySql_sql_select_Query ="""
            SELECT delivery_boy_username, delivery_boy_password ,delivery_boy_id  FROM Online_Retail_Store.delivery_boy
            """
            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()
            for row in result:
                if(row[0]==usrname and row[1]==pwd):
                    print(row[0],row[1])
                    id=int(row[2])
                    delivery_boy_query(id)
                    delivery_boy()
            print("Sorry, Wrong Credentials,try again!!!")
            delivery_boy()
        elif(num==2):
            start()
        else:
            print("Sorry, wrong input has been given try again...")
            delivery_boy()
        return
    
    def delivery_boy_query(id):
        print("1. View Orders")
        print("2. Mark Order Delivered")
        print("3. Log out")
        ans=int(input("Enter the choice: "))
        if(ans==1):
            mySql_sql_select_Query ="""
            SELECT customer.customer_username,orders.order_id, orders.delivery_address
            FROM orders
            JOIN delivery_boy ON orders.delivery_boy_id = delivery_boy.delivery_boy_id
            JOIN customer ON customer.customer_id = orders.customer_id
            WHERE orders.order_status='Not delivered' and delivery_boy.delivery_boy_id = """+str(id)+";"
            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()
            print()
            print(f'There are currently {len(result)} orders to be delivered')
            print(f'Customer name   Order_id   Delivery Address')
            for row in result:
                print(row[0],row[1],row[2])
            print()
            delivery_boy_query(id)

        elif(ans==2):
            ord_id=input("Enter the order id: ")
            my_query="""
            UPDATE orders
            SET orders.order_status='Delivered'
            WHERE orders.order_status='Not delivered' and orders.delivery_boy_id= """+str(id)+""" and orders.order_id= """+str(ord_id)+""";
            """
            try:
                cursor.execute(my_query)
                connection.commit()
                print()
                print(f'Order status has been updated succesfully.')
                print()
                delivery_boy_query(id)
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                print()
                delivery_boy_query(id)
        elif(ans==3):
            delivery_boy()
        else:
            print("Sorry, wrong input has been given try again...")
            delivery_boy_query(id)
        return
    
    def admin():
        print("Enter the choice from given below: ")
        print("1. Login")
        print("2. Quit")
        num=int(input("Enter: "))
        if(num==1): 
            print()
            print("Enter the credentials: ")
            usrname=input("Enter your username: ")
            pwd=input("Enter your password: ")
            mySql_sql_select_Query ="""
            SELECT admin_username,admin_password,admin_id FROM Online_Retail_Store.admins
            """
            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()
            for row in result:
                if(row[0]==usrname and row[1]==pwd):
                    print()
                    print(f'Welcome, {usrname}')
                    print()
                    id=int(row[2])
                    admin_query(id)
                    admin()
            print("Sorry, Wrong Credentials,try again!!!")
            admin()
        else:
            start()
        return

    def admin_query(id):
        print("1. Add Product")
        print("2. View products")
        print("3. Add Category")
        print("4. View Categories")
        print("5. Assign category to a product")
        print("6. Add Customer")
        print("7. View Customers")
        print("8. Add Coupon")
        print("9. View Coupons")
        print("10. Assign a coupon to a customer")
        print("11. Add Dealer")
        print("12. Add Delivery Boy")
        print("13. Analyse Data")
        print("14. Delete Product")
        print("15. Log out.")
        ans=int(input("Enter the choice: "))
        print()
        if(ans==15):
            admin()

        elif(ans==14):
            name=input("Enter product_id: ")
            my_query="""
            DELETE FROM product
            WHERE product.product_id= """+str(name)+""";
            """
            # print(my_query)
            try:
                cursor.execute(my_query)
                connection.commit()
                print()
                print(f'Product has been deleted succesfully.')
                print()
                admin_query(id)
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                print()
                admin_query(id)

        elif(ans==13):
            admin_data_analysis(id)

        elif(ans==12):
            name=input("Enter name: ")
            usrname=input("Enter username: ")
            pwd=input("Enter password: ")
            contact_number=input("Enter phone number: ")
            emid=input("Enter email-id: ")
            my_query="""
            insert into delivery_boy (delivery_boy_name, delivery_boy_username, delivery_boy_password, delivery_boy_average_rating, contact_number, email_id, admin_id) values 
            ('"""+name+"""','"""+usrname+"""','"""+pwd+"""', 0,'"""+contact_number+"""','"""+emid+"""','"""+str(id)+"""');
            """
            # print(my_query)
            try:
                cursor.execute(my_query)
                connection.commit()
                print()
                print(f'{name} has been added succesfully.')
                print()
                admin_query(id)
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                print()
                admin_query(id)

        elif(ans==11):
            name=input("Enter name: ")
            usrname=input("Enter username: ")
            pwd=input("Enter password: ")
            address=input("Enter address_of_operations: ")
            contact_number=input("Enter phone number: ")
            emid=input("Enter email-id: ")
            my_query="""
            insert into dealer (dealer_name, dealer_username, dealer_password, address_of_operations, contact_number, email_id, admin_id) values 
            ('"""+name+"""','"""+usrname+"""','"""+pwd+"""','"""+address+"""','"""+contact_number+"""','"""+emid+"""','"""+str(id)+"""');
            """
            try:
                cursor.execute(my_query)
                connection.commit()
                print()
                print(f'{name} has been added succesfully.')
                print()
                admin_query(id)
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                print()
                admin_query(id)

        elif(ans==10):
            name=input("Enter coupon_id: ")
            usrname=input("Enter customer_id: ")
            my_query="""
            insert into customer_coupon (coupon_id, customer_id) values
            ("""+name+""","""+usrname+""");
            """
            try:
                cursor.execute(my_query)
                connection.commit()
                print()
                print(f'Coupon has been assigned to the customer succesfully.')
                print()
                admin_query(id)
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                print()
                admin_query(id)

        elif(ans==9):
            my_query="""
            SELECT * FROM Online_Retail_Store.coupon;
            """
            cursor.execute(my_query)
            result=cursor.fetchall()
            print(f'There are currently {len(result)} coupons present in the database.')
            print("Coupon_id    Coupon_Code     Percentage_discount")
            for row in result:
                print(f'{row[0]}   {row[2]}   {row[1]}')
            admin_query(id)

        elif(ans==8):
            name=input("Enter coupon_code: ")
            usrname=input("Enter percentage_discount: ")
            my_query="""
            insert into coupon (percentage_discount, coupon_code, admin_id) values 
            ('"""+usrname+"""','"""+name+"""','"""+str(id)+"""');
            """
            try:
                cursor.execute(my_query)
                connection.commit()
                print()
                print(f'Coupon has been added succesfully.')
                print()
                admin_query(id)
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                print()
                admin_query(id)
        
        elif(ans==7):
            my_query="""
            SELECT * FROM Online_Retail_Store.customer;
            """
            cursor.execute(my_query)
            result=cursor.fetchall()
            print(f'There are currently {len(result)} customers present in the database.')
            print("Customer_id    Customer_name     Contact_number    Customer_username   Email_id   Customer_address")
            for row in result:
                print(f'{row[0]}   {row[1]}   {row[2]}   {row[3]}   {row[5]}   {row[6]}')
            admin_query(id)

        elif(ans==6):
            name=input("Enter name: ")
            usrname=input("Enter username: ")
            pwd=input("Enter password: ")
            address=input("Enter address: ")
            contact_number=input("Enter phone number: ")
            emid=input("Enter email-id: ")

            my_query="""
            insert into customer(customer_name, customer_username, customer_password,customer_address, contact_number, email_id, admin_id) values 
            ('"""+name+"""','"""+usrname+"""','"""+pwd+"""','"""+address+"""','"""+contact_number+"""','"""+emid+"""','"""+str(id)+"""');
            """
            try:
                cursor.execute(my_query)
                connection.commit()

                print()
                print(f'Customer has been added succesfully.')

                helper="""
                SELECT customer_id FROM Online_Retail_Store.customer
                WHERE customer_username= '"""+usrname+"""';"""
                cursor.execute(helper)
                rey=cursor.fetchall()
                cart_id=rey[0][0]
                my_quer="""
                insert into cart (cart_id,total_cost, description_info) values  
                ('"""
                my_quer=my_quer+str(cart_id)
                my_quer=my_quer+"""',0,'jvrenvjnvjnrvnkj vrnwvjn wrvjw vbntv tjb vjthjkv krj vj vfrv');"""

                try:
                    cursor.execute(my_quer)
                    connection.commit()
                    print()
                    print(f'Cart of customer has also been added succesfully.')
                    print()
                    admin_query(id)
                except:
                    connection.rollback()
                    print()
                    print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                    query="""DELETE FROM customer 
                    WHERE customer_id="""+str(cart_id)+""";"""
                    cursor.execute(query)
                    connection.commit()
                    print()
                    admin_query(id)
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                print()
                admin_query(id)
        
        elif(ans==5):
            name=input("Enter category_id: ")
            usrname=input("Enter product_id: ")
            my_query="""
            insert into categ_prod (prod_id,categ_id) values 
            ("""+usrname+""","""+name+""");
            """
            try:
                cursor.execute(my_query)
                connection.commit()
                print()
                print(f'Category has been assigned to the given product succesfully.')
                print()
                admin_query(id)
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                print()
                admin_query(id)
        
        elif(ans==4):
            my_query="""
            SELECT * FROM Online_Retail_Store.category;
            """
            cursor.execute(my_query)
            result=cursor.fetchall()
            print(f'There are currently {len(result)} categories present in the database.')
            print("Category_id    Category_name     Category_info")
            for row in result:
                print(f'{row[0]}   {row[1]}   {row[2]}')
            admin_query(id)

        elif(ans==3):
            name=input("Enter category_name: ")
            usrname=input("Enter category_info: ")
            my_query="""
            insert into category (category_name, category_info, admin_id) values 
            ('"""+name+"""','"""+usrname+"""','"""+str(id)+"""');
            """
            try:
                cursor.execute(my_query)
                connection.commit()
                print()
                print(f'Category has been added succesfully.')
                print()
                admin_query(id)
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                print()
                admin_query(id)

        elif(ans==2):
            my_query="""
            SELECT * FROM Online_Retail_Store.product;
            """
            cursor.execute(my_query)
            result=cursor.fetchall()
            print(f'There are currently {len(result)} products present in the database.')
            print("Product_id    Product_name    Product_cost   Brand_Name   Quantity")
            for row in result:
                print(f'{row[0]}   {row[1]}   {row[2]}   {row[3]}   {row[4]}')
            admin_query(id)

        elif(ans==1):
            name=input("Enter product_name: ")
            cost=input("Enter product_cost: ")
            brand=input("Enter brand_name: ")
            quantity=input("Enter quantity: ")
            my_query="""
            insert into product (product_name, product_cost, Brand_name, Quantity, admin_id) values 
            ('"""+name+"""','"""+cost+"""','"""+brand+"""','"""+quantity+"""','"""+str(id)+"""');
            """
            try:
                cursor.execute(my_query)
                connection.commit()
                print()
                print(f'Product has been added succesfully.')
                print()
                admin_query(id)
            except:
                connection.rollback()
                print()
                print(f'Sorry due to some error/wrong input information is not been able to be saved try again.')
                print()
                admin_query(id)

        else:
            print("Sorry, wrong input has been given try again...")
            admin_query(id)

        return

    def admin_data_analysis(id):

        print("1. Displaying customer id,customer name,order id of the customers who have placed order having total cost>= the given cost")
        print("2. Displaying delivery boy id,date at which order placed,order status,delivery boy name,average rating of the delivery boy in all those orders in which toal cost>= the given cost")
        print("3. Displaying number of products sold by each brand for a given year.")
        print("4. Displaying product-wise order and sales count for a given month and year.")
        print("5. Displaying total Sales by the product category and month.")
        print("6. Top given number of customers by total order value.")
        print("7. Go Back")

        num=int(input("Now choose which query do you want to see: "))
        if(num==1):
            cost=input("Enter the cost:")
            mySql_sql_select_Query ="""
            SELECT c.customer_id, c.customer_name,o.order_id
            FROM Online_Retail_Store.customer as c
            LEFT JOIN Online_Retail_Store.orders as o ON c.customer_id = o.customer_id
            WHERE o.total_cost>="""
            mySql_sql_select_Query=mySql_sql_select_Query+cost
            mySql_sql_select_Query=mySql_sql_select_Query+""" ORDER BY c.customer_id """


            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()

            print(f'Total number of tuples fetched for the above query: {cursor.rowcount}')
            print()

            for row in result:
                print(f'customer_id: {row[0]}', end ="    ")
                print(f'customer_name: {row[1]}', end ="    ")
                print(f'order_id: {row[2]}')
            
            print()
            admin_data_analysis(id)
            
        elif(num==2):
            cost=input("Enter the cost:")
            mySql_sql_select_Query ="""
            select Online_Retail_Store.orders.delivery_boy_id,Online_Retail_Store.orders.order_placed_date,Online_Retail_Store.orders.order_status,Online_Retail_Store.delivery_boy.delivery_boy_name,Online_Retail_Store.delivery_boy.delivery_boy_average_rating
            from Online_Retail_Store.orders
            left join Online_Retail_Store.delivery_boy
            on Online_Retail_Store.orders.delivery_boy_id = Online_Retail_Store.delivery_boy.delivery_boy_id
            where Online_Retail_Store.orders.total_cost>="""
            mySql_sql_select_Query=mySql_sql_select_Query+cost
            mySql_sql_select_Query=mySql_sql_select_Query+""" ORDER BY Online_Retail_Store.delivery_boy.delivery_boy_id"""


            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()

            print(f'Total number of tuples fetched for the query: {cursor.rowcount}')
            print()

            for row in result:
                print(f'->  ', end="  ")
                print(f'Delivery Boy Id: {row[0]}', end ="    ")
                print(f'Order placed Date: {row[1]}', end ="    ")
                print(f'Status of Order: {row[2]}', end ="    ")
                print(f'Delivery Boy Name: {row[3]}', end ="    ")
                print(f'Average rating: {row[4]}')

            print()
            admin_data_analysis(id)

        elif(num==3):
            year=input("Enter the year:")
            mySql_sql_select_Query ="""
            SELECT p.Brand_name, COUNT(cp.prod_id) as total_products_sold
            FROM orders o
            JOIN cart c ON o.customer_id = c.cart_id
            JOIN cart_prod cp ON c.cart_id = cp.cart_id
            JOIN product p ON cp.prod_id = p.product_id
            WHERE YEAR(order_placed_date) = """
            mySql_sql_select_Query=mySql_sql_select_Query+year
            mySql_sql_select_Query=mySql_sql_select_Query+""" GROUP BY p.Brand_name WITH ROLLUP"""

            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()

            print(f'Total number of tuples fetched for the query: {cursor.rowcount}')
            print()

            for row in result:
                print(f'->  ', end="  ")
                print(f'Brand name: {row[0]}', end ="    ")
                print(f'Total Products sold: {row[1]}')

            print()
            admin_data_analysis(id)

        elif(num==4):
            year=input("Enter the year:")
            month=input("Enter the month number:")

            mySql_sql_select_Query ="""
            SELECT p.product_name, COUNT(o.order_id) as total_orders, SUM(o.total_cost) as total_sales
            FROM orders o
            JOIN cart c ON o.customer_id = c.cart_id
            JOIN cart_prod cp ON c.cart_id = cp.cart_id
            JOIN product p ON cp.prod_id = p.product_id
            WHERE MONTH(order_placed_date) = """
            mySql_sql_select_Query=mySql_sql_select_Query+month
            mySql_sql_select_Query=mySql_sql_select_Query+""" AND YEAR(order_placed_date) = """
            mySql_sql_select_Query=mySql_sql_select_Query+year
            mySql_sql_select_Query=mySql_sql_select_Query+""" GROUP BY p.product_name WITH ROLLUP
            ORDER BY total_orders DESC"""

            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()

            print(f'Total number of tuples fetched for the query: {cursor.rowcount}')
            print()

            np=0
            for row in result:
                if(np==0):
                    print(f'->  ', end="  ")
                    print(f'Total orders in all total: {row[1]}', end ="    ")
                    print(f'Total sales of all orders: {row[2]}')
                    print()
                    np+=1
                else:
                    print(f'->  ', end="  ")
                    print(f'Product name: {row[0]}', end ="    ")
                    print(f'Total orders: {row[1]}',end="    ")
                    print(f'Total sales: {row[2]}')

            print()
            admin_data_analysis(id)

        elif(num==5):
            mySql_sql_select_Query ="""
            SELECT category_name, YEAR(order_placed_date) as year, MONTH(order_placed_date) as month, SUM(o.total_cost) as total_sales
            FROM orders o
            JOIN cart c ON o.customer_id = c.cart_id
            JOIN cart_prod cp ON c.cart_id = cp.cart_id
            JOIN product p ON cp.prod_id = p.product_id
            JOIN categ_prod cg ON p.product_id = cg.prod_id
            JOIN category ct ON cg.categ_id = ct.category_id
            GROUP BY category_name, YEAR(order_placed_date), MONTH(order_placed_date) WITH ROLLUP
            ORDER BY category_name, year, month"""

            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()

            print(f'Total number of tuples fetched for the query: {cursor.rowcount}')
            print()

            for row in result:
                print(f'->  ', end="  ")
                print(f'Category name: {row[0]}', end ="    ")
                print(f'Year: {row[1]}',end="    ")
                print(f'Month: {row[2]}',end="    ")
                print(f'Total sales: {row[3]}')

            print()
            admin_data_analysis(id)

        elif(num==6):
            number=input("Enter the number: ")

            mySql_sql_select_Query ="""
            SELECT c.customer_name, c.email_id, SUM(total_cost) as total_order_value
            FROM orders o
            JOIN customer c ON o.customer_id = c.customer_id
            GROUP BY c.customer_name, c.email_id
            ORDER BY total_order_value DESC
            LIMIT """
            mySql_sql_select_Query =mySql_sql_select_Query + number

            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()

            print(f'Total number of tuples fetched for the query: {cursor.rowcount}')
            print()

            for row in result:
                print(f'->  ', end="  ")
                print(f'Customer name: {row[0]}', end ="    ")
                print(f'Email Id: {row[1]}',end="    ")
                print(f'Total Order Value: {row[2]}')

            print()
            admin_data_analysis(id)

        elif(num==7):
            admin_query(id)

        else:
            print("Sorry, wrong input has been given try again...")
            admin_data_analysis(id)

    start()

except mysql.connector.Error as error:
    print("Failed to connect or read with the sql: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")