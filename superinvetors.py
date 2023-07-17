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
from selenium.webdriver.common.by import By

class assetsFromFound:
    def __init__(self,name,portfolioPart,value,cantidad):
        self.name=name
        self.portfolioPart = portfolioPart
        self.value = value
        self.cantidad=cantidad
class hedgefound:
    def __init__(self,name,activity):
        self.name=name
        self.activity = activity
class urlName:
    def __init__(self,name,url):
        self.name=name
        self.url = url

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
def superInvestorsMain():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `founds`")
    cachelist=[]
    myresult = mycursor.fetchall()        
    for rest in myresult:
        resultados= hedgefound(rest[1],rest[2])
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
    """------------------generar notificaciones--------------"""
    def crearNotificaciones(ActyvityFromBD,activity,name):
        frombd=json.loads(ActyvityFromBD)
        actividad=json.loads(activity)
        for activo in frombd:
            """  print(activo)
            print(activo['name'])"""
            for activoEnWeb in actividad:
                if(activo['name']==activoEnWeb['name']):
                   activoValue=activo['value'].replace(',', '').replace('$', '')
                   activoWebValue=activoEnWeb['value'].replace(',', '').replace('$', '')
                   monto= ((-1)*(int(activoValue)-int(activoWebValue)))
                   #print("-----------------------")

                   #print(monto , " esto es monto")
                   diferencia= int(activo['cantidad'].replace(',', ''))-int(activoEnWeb['cantidad'].replace(',', ''))
                  # print(diferencia,activo['value'] ,activoEnWeb['value'])
                   if(diferencia <0):
                       print("se sompro " + str(diferencia) + activoEnWeb['name'])
                       dif ="+$" + str(diferencia*(-1))
                       query = "INSERT INTO `activosenoperaciones`(`activo`, `operador`,`cantidad`,`value`,`movimiento`,`tipo_investor`) VALUES ('" + \
                          activoEnWeb['name'] + "','"+name+ "','"+ activoEnWeb['portfolioPart'] + "','"+ str(dif)+"','compra','fund')"
                       execute_query(connection, query)

                   if(diferencia >0):
                       dif ="-$" + str(diferencia)
                       print("se vendio " + str(diferencia) + activoEnWeb['name'])

                       query = "INSERT INTO `activosenoperaciones`(`activo`, `operador`,`cantidad`,`value`,`movimiento` ,`tipo_investor`) VALUES ('" + \
                          activoEnWeb['name'] + "','"+name+ "','"+ activoEnWeb['portfolioPart']+ "','"+str(dif)+"','venta','fund' )"
                       execute_query(connection, query)
                   if(diferencia ==0):
                       print("nada en " + str(diferencia) +activoEnWeb['name'])



    """------------------ fin generar notificaciones--------------"""

    driver = webdriver.Chrome(executable_path=r'C:\Users\Usuario\scrapy\chromedriver.exe')
    mycursor.execute("SELECT clave FROM `superinvestorkey`")
    contenido=[]
    myresultado = mycursor.fetchall()   
    for rest in myresultado:
        print(rest[0])
        contenido.append(rest[0])
    
  
         
                
    driver.get('https://www.dataroma.com/m/home.php')
    hold= driver.find_element(By.ID,"port_body")
         
    lock= hold.find_elements(By.XPATH,'.//a')
    toBeScraped=[]
    for u in lock: 
           url= u.get_attribute('href')
          # print(url)
           data = u.text.split('Updated')
           name=data[0]
           """fecha= datetime.strptime(data[1], '%d %b %Y')"""
           fecha = data[1].split(" ")
           out = str(m[fecha[2]])
           fecha=fecha[3]+"-"+out+"-"+fecha[1]
           today = date.today()
           key = fecha+name
           
           
           if key in contenido:
            #print(key+"existe"+url)
            """"""
           else:
            #print(key+"no existe")
            query = "INSERT INTO `superinvestorkey`(`clave`) VALUES ('" +key+"' )"
            execute_query(connection, query)
            toBeScraped.append(urlName(name,url))
    driver.close()
    data=[]
    for url in toBeScraped:
             driver = webdriver.Chrome(executable_path=r'C:\Users\Usuario\scrapy\chromedriver.exe')
             driver.get(url.url)
             hold= driver.find_element(By.ID,"grid")
            
             lock= hold.find_elements(By.XPATH,'.//tr')
             lock.pop(0)
             
             #print(url.name)
             assetlist=[]
             fondo=hedgefound(url.name, assetlist)
             for l in lock:
                 name =l.find_elements(By.XPATH,'.//td')
                 value = name[6].text;
                 asset= name[1].text
                 index=asset.find("-")
                 asset= asset[0:index-1]
                 porcentaje=name[2].text
                 activity=name[3].text
                 cantidad=name[4].text
               
                 hedge=assetsFromFound(asset,porcentaje,value,cantidad)
                 assetlist.append(hedge)
             driver.close()  
             fondo.activity=json.dumps(assetlist, default=lambda o: o.__dict__ )

             data.append(fondo)

   
            
         
           

    #print(len(data))
    if len(data)>0:
        for found in data:
            
            existe = 0
            activityFromBD =""
            
             

            if(1 == 1):

                  for cache in cachelist:
                        if cache.name == found.name:
                              existe = 1
                              activityFromBD = cache.activity

            if (existe == 1):
               crearNotificaciones(activityFromBD,found.activity,found.name)
               #print(found.name)
               #print(found.activity)
               query = "UPDATE `founds` SET `assets`='" + \
                   found.activity +"' WHERE `name`='" + found.name + "'"
               execute_query(connection, query)

            else:
               #print("entra en insert")
            
               actividad=json.loads(found.activity)
               #print(actividad)
               for activoEnWeb in actividad:
                   #print("se añade ")
                 
                   query = "INSERT INTO `activosenoperaciones`(`activo`, `operador`,`cantidad`,`value`,`movimiento`,`tipo_investor`) VALUES ('" + \
                      activoEnWeb['name'] + "','"+ found.name+ "','"+ activoEnWeb['portfolioPart'] + "','+"+ activoEnWeb['value']+"','compra','fund')"
                   #print(query)
                   execute_query(connection, query)
               query = "INSERT INTO `founds`(`name`, `assets`) VALUES ('" + \
                  found.name + "','"+found.activity+"')"
               execute_query(connection, query)

superInvestorsMain()



    
