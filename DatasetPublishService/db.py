import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error


def get_db_credentials():
    """Reads database credentials from environment variables"""
    load_dotenv()
    return {
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD')
    }


def connect_to_database():
    """Establishes a connection to the MySQL database"""
    try:
        credentials = get_db_credentials()
        connection = mysql.connector.connect(**credentials)
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
    return None

if __name__ == "__main__":
    connect_to_database()