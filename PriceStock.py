# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:46:50 2023

@author: MRP
"""

import urllib.request
import time
from threading import Thread, Barrier
import yfinance as yf
from bs4 import BeautifulSoup
from selenium import webdriver 
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
    

        for asset in Assets:
           
            
            print(asset.name)

            ticker_yahoo = yf.Ticker(asset.name)
            data = ticker_yahoo.history()
            last_quote = data['Close'].iloc[-1]
            print(" valor recinete")
            print( last_quote )
            print(" valor")
            print(float(asset.value) )
            
            diferencia=  (float(asset.value)-float(last_quote))/float(asset.value)
            print(diferencia)
            
            if diferencia>0.05:
               query2 = "UPDATE `position traker` SET `estado`='perdida'  WHERE  'activo' ='"+asset.name+"'"
               execute_query(connection, query2)
            elif diferencia<-0.05:
              
             query2 = "UPDATE `position traker` SET `estado`='Ganada'  WHERE  'activo' ='"+asset.name+"'" 
             execute_query(connection, query2)
            if asset.maximo< float(last_quote):
               print(asset.maximo)
               print("update")
               query2 = "UPDATE `position traker` SET `precioTop`='"+ str(float(last_quote))+"'  WHERE  `activo`= '"+asset.name+"'" 

               print(query2)
               execute_query(connection, query2) 
               
             
  
mainPrice()