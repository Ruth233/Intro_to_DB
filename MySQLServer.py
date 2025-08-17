import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",       # change if needed
        user="root",            # your MySQL username
        password="yourpassword" # your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create the database safely
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    # Handle errors
    print(f"Error: {e}")

finally:
    # Ensure proper cleanup
    if connection.is_connected():
        cursor.close()
        connection.close()
