# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:06:30 2022

@author: mruizpta
"""

import urllib.request
import time
from bs4 import BeautifulSoup
import DBconection as BD
mycursor = BD.mydb.cursor()


class filing:
    def __init__(self,date,code,company,tradetype,cargo,value,insider,QTY,own):
        self.date=date
        self.code = code
        self.company = company
        self.tradetype = tradetype
        self.title = cargo
        self.QTY = QTY
        self.own = own
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
            #print(rest[0])
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
           own=fill.find_all("td")[11].getText()
           fills =filing(date,code,company,trade,cargo,value,insider,qty,own)
           fillings.append(fills)
      except BD.Error as err:
        print(err)
      for fill in fillings:
        key= str(fill.insider+fill.value+fill.date).replace("'", "")


        if key in contenido:
         print(key+"existe")
        else:
           #print(key+"no existe")
           query="INSERT INTO `insider`( `clave`, `name`, `company`, `amount`, `trade`, `date`, `cantidad`, `own`,`position`) VALUES ('"+fill.company+"','" +str(fill.insider).replace("'", "")+"','"+fill.code +"','"+fill.value+"','"+fill.tradetype+"','"+fill.date+"','"+fill.QTY+"','"+fill.own+"','"+ fill.title + "')"
           BD.execute_query(BD.connection, query)
           #print(fill.tradetype)
           query = "INSERT INTO `insiderkey`(`clave`) VALUES ('" +str(key).replace("'", "")+"' )"
           BD.execute_query(BD.connection, query)
           operacion =""
           if fill.tradetype=="P - Purchase":
               operacion="compra"
               
           if fill.tradetype=="S - Sale" or fill.tradetype =="S - Sale+OE": 
               operacion="venta"
           #print(operacion)
           query2 = "INSERT INTO `activosenoperaciones`(`activo`, `operador`,`cantidad`,`value`,`movimiento`,`tipo_investor`,`own`,`position`) VALUES ('" + \
              fill.code+ "','"+str(fill.insider).replace("'", "")+ "','"+fill.QTY+ "','"+fill.value+"','"+ operacion + "','insider','"+ fill.own + "','"+ fill.title + "' )"
           #print(query2)
           BD.execute_query(BD.connection, query2)

      

    except:
      print(BD.Error)
mainInsider()