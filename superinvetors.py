# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:57:49 2022

@author: mruizpta
"""
import urllib.request
import sys

# Agrega la ruta al directorio que contiene DBconection.py
sys.path.append(r'C:\Users\Usuario\scrapy')
import time
from bs4 import BeautifulSoup
from selenium import webdriver 
from datetime import date,datetime
import json
from selenium.webdriver.common.by import By
import DBconection as BD

class assetsFromFound:
    def __init__(self,name,portfolioPart,value,cantidad,movimiento):
        self.name=name
        self.portfolioPart = portfolioPart
        self.value = value
        self.cantidad=cantidad
        self.movimiento=movimiento
class hedgefound:
    def __init__(self,name,activity):
        self.name=name
        self.activity = activity
class urlName:
    def __init__(self,name,url):
        self.name=name
        self.url = url


"""---------------------------------------------------"""


def superInvestorsMain():
    mycursor = BD.mydb.cursor()

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
                       #print("se sompro " + str(diferencia) + activoEnWeb['name'])
                       dif ="+$" + str(diferencia*(-1))
                       query = "INSERT INTO `activosenoperaciones`(`activo`, `operador`,`cantidad`,`value`,`movimiento`,`tipo_investor`,`own`) VALUES ('" + \
                          activoEnWeb['name'] + "','"+name+ "','"+  activoEnWeb['cantidad']+ "','"+ str(dif)+"','compra','fund','"+ activoEnWeb['portfolioPart']+ "' )"
                       BD.execute_query(BD.connection, query)

                   if(diferencia >0):
                       dif ="-$" + str(diferencia)
                       #print("se vendio " + str(diferencia) + activoEnWeb['name'])

                       query = "INSERT INTO `activosenoperaciones`(`activo`, `operador`,`cantidad`,`value`,`movimiento` ,`tipo_investor`,own) VALUES ('" + \
                          activoEnWeb['name'] + "','"+name+ "','"+ activoEnWeb['cantidad']+ "','"+str(dif)+"','venta','fund','"+ activoEnWeb['portfolioPart']+ "' )"
                       BD.execute_query(BD.connection, query)
                   if(diferencia ==0):
                       """print("nada en " + str(diferencia) +activoEnWeb['name'])"""



    """------------------ fin generar notificaciones--------------"""

    driver = webdriver.Chrome(executable_path=r'C:\Users\Usuario\scrapy\chromedriver.exe')
    mycursor.execute("SELECT clave FROM `superinvestorkey`")
    contenido=[]
    myresultado = mycursor.fetchall()   
    for rest in myresultado:
        #print(rest[0])
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
            BD.execute_query(BD.connection, query)
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
               
                 hedge=assetsFromFound(asset,porcentaje,value,cantidad,activity)
                 assetlist.append(hedge)
             driver.close()  
             fondo.activity=json.dumps(assetlist, default=lambda o: o.__dict__ )

             data.append(fondo)

   
            
         
           

    #print(len(data))
    if len(data)>0:
        for found in data:
            print("entra1")
            existe = 0
            activityFromBD =""
            
             

            if(1 == 1):

                  for cache in cachelist:
                        if cache.name == found.name:
                              existe = 1
                              activityFromBD = cache.activity

            if (existe == 1):
               print("entra2")
               crearNotificaciones(activityFromBD,found.activity,found.name)
               #print(found.name)
               #print(found.activity)
               query = "UPDATE `founds` SET `assets`='" + \
                   found.activity +"' WHERE `name`='" + found.name + "'"
               BD.execute_query(BD.connection, query)
               query = "INSERT INTO `notificaciones`(`activo`, `data`,`tipoNotificacion`,`importancia`) VALUES ('" + \
                  found.name + "','"+str(found.activity)+"','fond',80)"
               print(query)
               BD.execute_query(BD.connection, query)

            else:
               print("entra en insert")
               query = "INSERT INTO `founds`(`name`, `assets`) VALUES ('" + \
                  found.name + "','"+str(found.activity)+"')"
               print(query)
               BD.execute_query(BD.connection, query)

               actividad=json.loads(found.activity)
               #print(actividad)
               for activoEnWeb in actividad:
                   print(activoEnWeb['cantidad'])
                 
                   query = "INSERT INTO `activosenoperaciones`(`activo`, `operador`,`cantidad`,`value`,`movimiento`,`tipo_investor`,`own`) VALUES ('" + \
                      activoEnWeb['name'] + "','"+ found.name+ "','"+ activoEnWeb['cantidad'] + "','+"+ activoEnWeb['value']+"','compra','fund','"+ activoEnWeb['portfolioPart']+ "')"
                   #print(query)
                   BD.execute_query(BD.connection, query)
               query = "INSERT INTO `notificaciones`(`activo`, `data`,`tipoNotificacion`,`importancia`) VALUES ('" + \
                  found.name + "','"+found.activity+"','fond',80)"
               BD.execute_query(BD.connection, query)
superInvestorsMain()



    
