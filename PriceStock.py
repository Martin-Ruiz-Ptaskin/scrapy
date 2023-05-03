# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:46:50 2023

@author: MRP
"""

import urllib.request
import time
from threading import Thread, Barrier

from bs4 import BeautifulSoup
from selenium import webdriver 
driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
from selenium.webdriver.common.by import By
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
class activoFromBd:
    def __init__(self,activo,cantidad,operador,value,interesados):
        self.activo=activo
        self.operador = operador+"[cantidad:"+str(cantidad)+",value:"+str(value)+"]"
        self.cantidad=cantidad
        self.value = value
        self.interesados = interesados

"""Clases"""
class activo:
    def __init__(self,name,value,maximo):
        self.name=name
        self.value = value
        self.maximo = maximo

"""-----------------------Get Assets-----------------------------"""
mycursor = mydb.cursor()
mycursor.execute("SELECT DISTINCT activo ,precioCompra,precioTop FROM `position traker`")
myresult = mycursor.fetchall() 
Assets=[]  
for rest in myresult:
    Assets.append(activo(rest[0],rest[1],rest[2]) )

"""----------------------- Fin Get Assets-----------------------------"""

        
        
activosConPrecio=[]
def mainPrice():
    def func(threads,Assets):
        driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

        for asset in Assets:
           
            
            print(asset.name)
            driver.get('https://www.google.com/search?q='+asset.name+'+stock&rlz=1C1CHBF_esAR1047AR1047&sxsrf=APwXEdde7_SzTvOQVk0YnM1lmenH53LvrA%3A1682299487637&ei=X9pFZPq6JsPS1sQP16GJ6A8&ved=0ahUKEwi65vb6rcH-AhVDqZUCHddQAv0Q4dUDCA8&uact=5&oq=APPL+stock&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCAAQigUQQzIHCAAQgAQQCjIHCAAQgAQQCjINCC4QrwEQxwEQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjINCC4QrwEQxwEQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjoKCAAQRxDWBBCwAzoKCAAQigUQsAMQQzoGCAAQBxAeOhAILhCKBRCxAxDHARDRAxBDOgoIIxCwAhAnEJ0COgcIABANEIAEOg0ILhANEK8BEMcBEIAEOgoIIxCxAhAnEJ0CSgQIQRgAUIgLWPEbYJAhaANwAXgAgAHAAYgB9gSSAQM1LjGYAQCgAQHIAQrAAQE&sclient=gws-wiz-serp')
            data = driver.find_elements(By.XPATH,"//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/g-card-section[1]/div[1]/g-card-section[1]/div[2]/div[1]/span[1]/span[1]/span[1]")[0].text
            diferencia=  (float(asset.value)-float(data))/float(asset.value)
            
            if diferencia>0.05:
               query2 = "UPDATE `position traker` SET `estado`='perdida'  WHERE  'activo' ='"+asset.name+"'"
               execute_query(connection, query2)
            elif diferencia<-0.05:
              
             query2 = "UPDATE `position traker` SET `estado`='Ganada'  WHERE  'activo' ='"+asset.name+"'" 
             execute_query(connection, query2)
            if asset.maximo< float(data):
               print(asset.maximo)
               print("update")
               query2 = "UPDATE `position traker` SET `precioTop`='"+ str(float(data))+"'  WHERE  `activo`= '"+asset.name+"'" 

               print(query2)
               execute_query(connection, query2) 
               
             
        driver.close()
    cantidad=round(len(Assets)/10)
    barrier = Barrier(cantidad)
    def get_sublists(original_list, number_of_sub_list_wanted):
         sublists = list()
         for sub_list_count in range(number_of_sub_list_wanted): 
          sublists.append(original_list[sub_list_count::number_of_sub_list_wanted])
         return sublists
    url=get_sublists(Assets, cantidad)
    threads = []

    for a in url:
         i = Thread(target=func, args=(barrier,a,))
         i.start()
         threads.append(i)

    for i in threads:
         i.join()
