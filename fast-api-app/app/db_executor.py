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


def execute(query, args):
    connection = create_server_connection("proxysql", 6033, "delivery_service", "root", 'root')
    cursor = connection.cursor(prepared=True)
    cursor.execute(query, args)
    if 'insert into' in query.lower():
        uuid = cursor.fetchone()[0]
        connection.commit()
        connection.close()
        return uuid
    elif 'select' not in query.lower():
        connection.commit()
        connection.close()
    else:
        result = cursor.fetchall()
        connection.close()
        return result
