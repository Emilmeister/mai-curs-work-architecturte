import mysql.connector
from mysql.connector import Error
import pandas as pd


def create_server_connection(host_name, port, database, user_name, user_password):
    connection_new = None
    try:
        connection_new = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            port=port,
            database=database,
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection_new


connection = create_server_connection("db", 3306, "delivery_service", "root", 'root')


def execute(query, args):
    cursor = connection.cursor(prepared=True)
    try:
        cursor.execute(query, args)
        if 'select' not in query.lower():
            connection.commit()
        else:
            return cursor.fetchall()
    except Error as err:
        print(f"Error: '{err}'")
