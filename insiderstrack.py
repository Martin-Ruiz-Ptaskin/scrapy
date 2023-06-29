# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:06:30 2022

@author: mruizpta
"""

import urllib.request
import time
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error
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


class filing:
    def __init__(self,date,code,company,tradetype,cargo,value,insider,QTY):
        self.date=date
        self.code = code
        self.company = company
        self.tradetype = tradetype
        self.title = cargo
        self.QTY = QTY

        self.value = value
        self.insider = insider

def mainInsider():
    
    
    try:
      try:
       datos = urllib.request.urlopen("http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1").read().decode()
       soup =BeautifulSoup(datos,"html.parser")
       table = soup.find_all("tbody")
       

       line =table[1].find_all("tr")
       """filing=filing("hoy","TSLA","teska","BUY","CEO","1000","Elon")"""
       fillings=[]
       previos=[]
       lista=""
      

       mycursor.execute("SELECT clave FROM `insiderkey`")
       contenido=[]
       myresultado = mycursor.fetchall()        
       for rest in myresultado:
            print(rest[0])
            contenido.append(rest[0])
                
         
       for fill in line:
           date=fill.find_all("td")[1].find_all("a")[0].getText();
           code= fill.find_all("td")[3].find_all("a")[0].getText()
           company =fill.find_all("td")[4].find_all("a")[0].getText()
           insider =fill.find_all("td")[5].find_all("a")[0].getText()
           cargo= fill.find_all("td")[6].getText()
           trade =fill.find_all("td")[7].getText()
           value =fill.find_all("td")[12].getText()
           qty=fill.find_all("td")[10].getText()
           print(qty)
           fills =filing(date,code,company,trade,cargo,value,insider,qty)
           fillings.append(fills)
      except Error as err:
        print(err)
      for fill in fillings:
        key= fill.insider+fill.value+fill.date 


        if key in contenido:
         print(key+"existe")
        else:
           print(key+"no existe")
           query="INSERT INTO `insider`( `clave`, `name`, `company`, `amount`, `trade`, `date`) VALUES ('"+fill.company+"','" +fill.insider+"','"+fill.code +"','"+fill.value+"','"+fill.tradetype+"','"+fill.date+"')"
           execute_query(connection, query)
           print(fill.tradetype)
           query = "INSERT INTO `insiderkey`(`clave`) VALUES ('" +key+"' )"
           execute_query(connection, query)
           operacion =""
           if fill.tradetype=="P - Purchase":
               operacion="compra"
               
           if fill.tradetype=="S - Sale": 
               operacion="venta"
           print(operacion)
           query2 = "INSERT INTO `activosenoperaciones`(`activo`, `operador`,`cantidad`,`value`,`movimiento`) VALUES ('" + \
              fill.code+ "','"+fill.insider+ "','"+fill.QTY+ "','"+fill.value+"','"+ operacion + "')"
           print(query2)
           execute_query(connection, query2)

      contenido.close()

    except:
      print(Error)

