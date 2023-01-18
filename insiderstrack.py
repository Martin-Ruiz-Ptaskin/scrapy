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
    def __init__(self,date,code,company,tradetype,cargo,value,insider):
        self.date=date
        self.code = code
        self.company = company
        self.tradetype = tradetype
        self.title = cargo

        self.value = value
        self.insider = insider
try:
  try:
   datos = urllib.request.urlopen("http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1").read().decode()
   soup =BeautifulSoup(datos)
   table = soup.find_all("tbody")
   

   line =table[1].find_all("tr")
   """filing=filing("hoy","TSLA","teska","BUY","CEO","1000","Elon")"""
   fillings=[]
   previos=[]
   lista=""
   contenido = open(r"C:\Users\mruizpta\scrapy\InsiderKeyList.txt", "r")
         
   for línea in contenido:
     lista=línea
     previos=lista.split("/")
     """print (previos)"""
            
   contenido.close()
            
     
   for fill in line:
       date=fill.find_all("td")[1].find_all("a")[0].getText();
       code= fill.find_all("td")[3].find_all("a")[0].getText()
       company =fill.find_all("td")[4].find_all("a")[0].getText()
       insider =fill.find_all("td")[5].find_all("a")[0].getText()
       cargo= fill.find_all("td")[6].getText()
       trade =fill.find_all("td")[7].getText()
       value =fill.find_all("td")[12].getText()
       fills =filing(date,code,company,trade,cargo,value,insider)
       fillings.append(fills)
  except:
    print("no se pudieron obtner los datos")
  contenido = open(r"C:\Users\mruizpta\scrapy\InsiderKeyList.txt", "w")
  for fill in fillings:
    key= fill.insider+fill.value+fill.date 

    contenido.write(key+"/")

    if key in previos:
     print(key+"existe")
    else:
       print(key+"no existe")
       query="INSERT INTO `insider`( `clave`, `name`, `company`, `amount`, `trade`, `date`) VALUES ('"+key+"','" +fill.insider+"','"+fill.code +"','"+fill.value+"','"+fill.tradetype+"','"+fill.date+"')"
       execute_query(connection, query)

  contenido.close()

except:
  print("error")

