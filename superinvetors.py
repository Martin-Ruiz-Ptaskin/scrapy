# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:57:49 2022

@author: mruizpta
"""
import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver 
from datetime import date,datetime
import mysql.connector
import json
from mysql.connector import Error

class hedgefound:
    def __init__(self,name,portfolioPart,activity,value):
        self.name=name
        self.portfolioPart = portfolioPart
        self.activity = activity
        self.value = value

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

mycursor.execute("SELECT * FROM `founds`")
cachelist=[]
myresult = mycursor.fetchall()        
for rest in myresult:
    resultados= hedgefound(rest[0],rest[1])
    cachelist.append(resultados)
m = {
        'Jan': "01",
        'Feb': "02",
        'Mar': "03",
        'Apr': "04",
        'May': "05",
        'Jun': "06",
        'Jul': "07",
        'Aug': "08",
        'Sep': "09",
        'Oct': "10",
        'Nov': "11",
        'Dec': "12"
        }
driver = webdriver.Chrome(executable_path=r'C:\\Users\\mruizpta\\chromedriver_win32\\chromedriver.exe')
lista=""
contenido = open(r"C:\scrapy\founds.txt", "r")
previos=[]
    
for línea in contenido:
    lista=línea
    previos=lista.split("/")
     
            
contenido.close()
driver.get('https://www.dataroma.com/m/home.php')
hold= driver.find_element_by_id("port_body")
     
lock= hold.find_elements_by_xpath('.//a')
contenido = open(r"C:\scrapy\superinvestorkeylist.txt", "w")
toBeScraped=[]
for u in lock: 
       url= u.get_attribute('href')
       print(url)
       data = u.text.split('Updated')
       name=data[0]
       """fecha= datetime.strptime(data[1], '%d %b %Y')"""
       fecha = data[1].split(" ")
       out = str(m[fecha[2]])
       fecha=fecha[3]+"-"+out+"-"+fecha[1]
       today = date.today()
       key = fecha+name
       contenido.write(key+"/")

       if key in previos:
         print(key+"existe"+url)
       else:
        print(key+"no existe")
        toBeScraped.append(url)
contenido.close()

for url in toBeScraped:
         driver.get(url)
         hold= driver.find_element_by_id("grid")
        
         lock= hold.find_elements_by_xpath('.//tr')
         lock.pop(0)
         data=[]
         for l in lock:
             name =l.find_elements_by_xpath('.//td')
             value = name[6].text;
             asset= name[1].text
             index=asset.find("-")
             print (value +" esto es value")
             asset= asset[0:index-1]
             porcentaje=name[2].text
             activity=name[3].text
             hedge=hedgefound(asset,porcentaje,activity,value)
             data.append(hedge)
             
         for i in data:
          jsonstr1 = json.dumps(i.__dict__)
          print (jsonstr1) 
     
       
driver.close() 
for found in data:
    
        """try:
      if(1==2): 
    
          print("entra aca")
          query="INSERT INTO `founds`(`name`, `assets`) VALUES ('"+ found.name +"','"+found.value+"')"
          execute_query(connection, query)
          
          
        
      if(1==1):
    
          for cache in cachelist:
                    
                    
                    if cache.wallet==tag.wallet:
                        
                        previo=float(cache.amount)
                        neto=(previo-float(amount))
                        print(previo-float(amount))
                        query="UPDATE `founds` SET `amount`='"+amount+"' WHERE `wallet`='"+ tag.wallet +"'"
                        print(query)
                        execute_query(connection, query)
                        if neto ==0:
                            print( "nada que hacer")
                        if neto>=3:
                           print( "se debe accionar tiene menos")
                           query="INSERT INTO `hist_cripto_changes`(`wallet`, `amount`,`date`, `cripto`) VALUES ('"+ tag.wallet +"','"+amount+"',"+date.today().strftime("%m/%d/%Y")+",'BTC')"
        
                        elif neto <=-3 :
                            print("se debe aacionar tiene mas",cache.wallet)
                            query="INSERT INTO `hist_cripto_changes`(`wallet`, `amount`,`date`, `cripto`) VALUES ('"+ tag.wallet +"','"+amount+"',"+date.today().strftime("%m/%d/%Y")+",'BTC')"
     except:
      print ("error")   """




