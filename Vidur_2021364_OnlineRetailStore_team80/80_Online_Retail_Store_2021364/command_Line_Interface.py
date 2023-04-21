import mysql.connector
from mysql.connector import Error

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
        if(ans==1):
            admin()
        elif(ans==2):
            customer()
        elif(ans==3):
            dealer()
        elif(ans==4):
            delivery_boy()
        elif(ans==5):
            quit()
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
            WHERE product.product_name = """+pr_name+";"
            mySql_sql_select_Query2="""
            SELECT prod_id,cart_id,quantity FROM Online_Retail_Store.cart_prod;
            """
            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()
            cursor.execute(mySql_sql_select_Query2)
            result2 = cursor.fetchall()
            if(len(result)==0):
                print("Sorry, no such product name exists, try again with correct product name..")
                customer_query(id)
                return
            cost_of_product=int(result[0][2])
            flag=0
            qty=0
            for ro in result2:
                if(int(result[0][0])==int(ro[0]) and id==int(ro[1])):
                    flag=1
                    qty=int(ro[2])
            if(flag==0):
                for row in result:
                    if(int(row[1])>=quantity):
                        my_query="""
                        insert into cart_prod (prod_id,cart_id,quantity) values 
                        ("""+row[0]+","+str(id)+","+str(quantity)+");"
                        cursor.execute(my_query)
                        print("Your cart has successfully been updated")
                    else:
                        print("Sorry, product you have requested is out of stock")
            else:
                for row in result:
                    if(int(row[1])>=quantity):
                        my_query2="""
                        SELECT total_cost FROM Online_Retail_Store.cart
                        WHERE cart_id="""+str(id)+";"
                        cursor.execute(my_query2)
                        answer=cursor.fetchall()
                        calcu=int(answer[0][0])-cost_of_product*qty+cost_of_product*quantity
                        my_query="""
                        UPDATE cart_prod
                        SET quantity="""+str(quantity)+"""
                        WHERE cart_id="""+str(id)+""" and prod_id="""+result[0][0]+""";"""
                        cursor.execute(my_query)
                        my_query="""
                        UPDATE cart
                        SET total_cost="""+str(calcu)+"""
                        WHERE cart_id="""+str(id)+""";"""
                        cursor.execute(my_query)
                        print("Your cart has successfully been updated")
                    else:
                        print("Sorry, product you have requested is out of stock")
            customer_query(id)
        elif(ans==5):
            mySql_sql_select_Query ="""
            DELETE FROM cart_prod
            WHERE cart_prod.cart_id="""+str(id)+""";"""
            cursor.execute(mySql_sql_select_Query)
            my_query="""
            UPDATE cart
            SET total_cost=0
            WHERE cart_id="""+str(id)+""";"""
            cursor.execute(my_query)
            print("Your cart has been emptied successfully")
        elif(ans==4):
            mySql_sql_select_Query ="""
            DELETE FROM cart_prod
            WHERE cart_prod.cart_id="""+str(id)+""";"""
            cursor.execute(mySql_sql_select_Query)
            my_query="""
            UPDATE cart
            SET total_cost=0
            WHERE cart_id="""+str(id)+""";"""
            cursor.execute(my_query)
            print("Your cart has been emptied successfully")
        elif(ans==7):
            customer()
        else:
            print("Sorry, wrong input has been given try again...")
            customer_query(id)
        return

    def admin():
        print("Enter the choice from given below: ")
        print("1. Login")
        print("2. Quit")
        num=int(input("Enter: "))
        if(num==1): 
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
                    print(row[0],row[1])
                    id=int(row[2])
                    admin_query(id)
                    admin()
            print("Sorry, Wrong Credentials,try again!!!")
            admin()
        else:
            start()
        return
    
    def dealer():
        print("Enter the choice from given below: ")
        print("1. Login")
        print("2. Go Back")
        num=int(input("Enter: "))
        if(num==1): 
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
                    print(row[0],row[1])
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
            SELECT customer.customer_name, orders.delivery_address
            FROM orders
            JOIN delivery_boy ON orders.delivery_boy_id = delivery_boy.delivery_boy_id
            JOIN customer ON customer.customer_id = orders.customer_id
            WHERE delivery_boy.delivery_boy_id = """+str(id)+";"
            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()
            print()
            print(f'There are currently {len(result)} orders to be delivered')
            print(f'Customer name   Delivery Address')
            for row in result:
                print(row[0],row[1])
            print()
            delivery_boy_query(id)
        elif(ans==2):
            delivery_boy()
        else:
            print("Sorry, wrong input has been given try again...")
            delivery_boy_query(id)
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
        print("2. Log out")
        ans=int(input("Enter the choice: "))
        if(ans==1):
            mySql_sql_select_Query ="""
            SELECT customer.customer_name, orders.delivery_address
            FROM orders
            JOIN delivery_boy ON orders.delivery_boy_id = delivery_boy.delivery_boy_id
            JOIN customer ON customer.customer_id = orders.customer_id
            WHERE delivery_boy.delivery_boy_id = """+str(id)+";"
            cursor.execute(mySql_sql_select_Query)
            result = cursor.fetchall()
            print()
            print(f'There are currently {len(result)} orders to be delivered')
            print(f'Customer name   Delivery Address')
            for row in result:
                print(row[0],row[1])
            print()
            delivery_boy_query(id)
        elif(ans==2):
            delivery_boy()
        else:
            print("Sorry, wrong input has been given try again...")
            delivery_boy_query(id)
        return
    

    def admin_query(id):
        print("1. Add Product")
        print("2. View products")
        print("3. Add Category")
        print("4. View Categories")
        print("5. Assign category to a product")
        print("6. Add Customer")
        print("7. Add Coupon")
        print("8. Assign a coupon to a customer")
        print("9. Add Dealer")
        print("10. Add Delivery Boy")
        print("11. Analyse Data")
        print("12. Log out.")
        ans=int(input("Enter the choice: "))
        if(ans==12):
            admin()
        elif(ans==11):
            admin_data_analysis()
        elif(ans==10):
            

    def admin_data_analysis():
        print("1. Displaying customer id,customer name,order id of the customers who have placed order having total cost>= the given cost")
        print("2. Displaying delivery boy id,date at which order placed,order status,delivery boy name,average rating of the delivery boy in all those orders in which toal cost>= the given cost")
        print("3. Displaying number of products sold by each brand for a given year.")
        print("4. Displaying product-wise order and sales count for a given month and year.")
        print("5. Displaying total Sales by the product category and month.")
        print("6. Top given number of customers by total order value.")


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
            print("Query_1_activated_successfully")
            
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
            print("Query_2_activated_successfully")

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
            print("Query_3_activated_successfully")

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
            print("Query_4_activated_successfully")

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
            print("Query_5_activated_successfully")

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
            print("Query_6_activated_successfully")
        ask=input("Do you want to run another sql query or logout? (YES/NO) ")
        if(ask=="YES"):
            start_query_admin()
        else:
            admin()

    start()

except mysql.connector.Error as error:
    print("Failed to connect or read with the sql: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
