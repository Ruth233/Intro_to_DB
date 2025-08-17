import mysql.connector

def create_database():
    """
    Creates the 'alx_book_store' database if it does not exist.
    Returns True if successful, False if an error occurs.
    """
    connection = None
    cursor = None

    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",       # Change if your host is different
            user="root",            # Replace with your MySQL username
            password="yourpassword" # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            return True

    except mysql.connector.Error as e:  # <-- FIXED HERE
        print(f"Error: {e}")
        return False

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    success = create_database()
    if success:
        print("✅ Operation completed successfully.")
    else:
        print("❌ Operation failed.")
