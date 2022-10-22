# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 03:29:02 2022

@author: mruizpta
"""

import time
import mysql.connector
from mysql.connector import Error
from selenium import webdriver 
from threading import Thread, Barrier
amount=[]
"""---------------------------------------------------"""
        
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

connection = create_db_connection("localhost", "root", "", "scrapy")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
"""---------------------------------------------------"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="scrapy"
)

mycursor = mydb.cursor()
"""mycursor.execute("SELECT * FROM bitcoin") cachelist=[]
myresult = mycursor.fetchall()


for rest in myresult:
    resultados= cartera(rest[0],rest[1])
    cachelist.append(resultados)"""
"""----------------------FIN CONECCION----------------------------"""

def func():
 

   driver = webdriver.Chrome(executable_path=r'C:\\Users\\mruizpta\\chromedriver_win32\\chromedriver.exe')

   driver.get('https://www.etoro.com/discover/people/results?copyblock=false&period=OneYearAgo&hasavatar=true&displayfullname=true&verified=true&popularinvestor=true&isfund=false&maxmonthlyriskscoremin=3&maxmonthlyriskscoremax=6&sort=-gain&page=6&pagesize=20&gainmax=180&gainmin=5&preset=preset_one')
   autoss = driver.find_elements_by_xpath('//et-table[@button-count-1 discover-button ng-star-inserted"]')
   autos = autoss.find_elements_by_xpath('//div[@class="et-table-row-main et-flex-align-center ng-star-inserted"]')
   
   for auto in autos:
            # Por cada anuncio hallo el preico
    name = auto.find_element_by_xpath('.//div[@class="user-nickname"]').text
    beneficios = auto.find_element_by_xpath('.//span[@class="positive"]').text
    copiadores = auto.find_element_by_xpath('.//span[@automation-id="discover-people-results-list-item-copiers-num""]').text
    print(name,beneficios,copiadores)

  
   driver.close()
func()