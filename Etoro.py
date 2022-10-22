# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:54:05 2022

@author: mruizpta
"""

import time
import mysql.connector
from mysql.connector import Error
from selenium import webdriver 
from threading import Thread, Barrier
amount=[]
class innversor:
    def __init__(self,investor,stock):
        self.investor=investor
        self.stock = stock
        
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
acciones=[]
def func(threads,url):
 
 for u in url: 
   driver = webdriver.Chrome(executable_path=r'C:\\Users\\mruizpta\\chromedriver_win32\\chromedriver.exe')

   driver.get('https://www.etoro.com/people/'+u+'/portfolio')
   autoss = driver.find_elements_by_xpath('//ui-table-body[@class="ng-scope"]')
   autos = driver.find_elements_by_xpath('//div[@class="i-portfolio-table-instrument"]')
   
   for auto in autos:
            # Por cada anuncio hallo el preico
    stock = auto.find_element_by_xpath('.//div[@class="i-portfolio-table-name"]').text
    print(stock)

    acciones.append(stock)
  
   driver.close()
 
 
	

url =['garudolf']



cantidad=round(len(url)/1)
barrier = Barrier(cantidad)
def get_sublists(original_list, number_of_sub_list_wanted):
 sublists = list()
 for sub_list_count in range(number_of_sub_list_wanted): 
  sublists.append(original_list[sub_list_count::number_of_sub_list_wanted])
 return sublists
url=get_sublists(url, cantidad)
threads = []

for a in url:
 i = Thread(target=func, args=(barrier,a,))
 i.start()
 threads.append(i)

for i in threads:
 i.join()



        

print(len(amount))
for tag in amount:
    

 amount= tag.amount.replace(',','')
   
 amount= amount.replace(',','.')
 """ con este cargo nuevos con borrado previo """
 if(1==2): 

  print("entra aca")
  query="INSERT INTO `bitcoin`(`wallet`, `amount`) VALUES ('"+ tag.wallet +"','"+amount+"')"
  execute_query(connection, query)
  
  
  """ con este actualizo """
 
   