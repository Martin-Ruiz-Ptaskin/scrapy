# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 17:27:12 2022

@author: mruizpta
"""
import mysql.connector
from mysql.connector import Error
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
pop_teacher = """
INSERT INTO `bitcoin`(`wallet`, `amount`) VALUES ('[value-1]','[value-2]')
"""
connection = connection = create_db_connection("localhost", "root", "", "scrapy")

execute_query(connection, pop_teacher)