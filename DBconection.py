# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 18:47:59 2023

@author: Usuario
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

"""---------------------------------------------------"""

#connection = create_db_connection("localhost", "root", "", "scrapy")
connection = create_db_connection("50.87.144.185", "datodtal_scrapy", "%V]B]Rvvl}uo", "datodtal_scrapy")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        #print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
"""---------------------------------------------------"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="scrapy"
)
cursor = mydb.cursor()