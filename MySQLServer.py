import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (adjust user & password to yours)
        connection = mysql.connector.connect(
            host="localhost",       # Change if using remote server
            user="root",            # Replace with your MySQL username
            password="your_password" # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
