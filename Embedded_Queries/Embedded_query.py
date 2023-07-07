import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Online_Retail_Store',
                                         user='root',
                                         password='Vidurg@1102')
    cursor = connection.cursor()
    def start_query():

        print("There are currently given queries runnable in the system :")
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
            WHERE o.total_cost>= """
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
        start_query()
    start_query()

except mysql.connector.Error as error:
    print("Failed to read: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")