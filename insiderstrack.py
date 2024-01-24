# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:06:30 2022

@author: mruizpta
"""
import sys

sys.path.append(r'C:\Users\Usuario\scrapy')

import requests
import json
import makeRequest
import urllib.request
import time
from bs4 import BeautifulSoup
import DBconection as BD



class filing:
    def __init__(self,date,code,company,tradetype,cargo,value,insider,QTY,own,operacion):
        self.date=date
        self.code = code
        self.company = company
        self.tradetype = tradetype
        self.title = cargo
        self.QTY = QTY
        self.own = own
        self.value = value
        self.insider = insider
        self.operacion= operacion

def mainInsider():
    
       mycursor = BD.mydb.cursor()

       mycursor.execute("SELECT clave FROM `insiderkey`")
       contenido=[]
       myresultado = []#mycursor.fetchall()    
       datos = urllib.request.urlopen("http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1").read().decode()
       soup =BeautifulSoup(datos,"html.parser")
       table = soup.find_all("tbody")
       

       line =table[1].find_all("tr")
       """filing=filing("hoy","TSLA","teska","BUY","CEO","1000","Elon")"""
       fillings=[]
       previos=[]
       lista=""
      
    
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
           operacion =""
           if trade=="P - Purchase":
               operacion="compra"
               
           if trade=="S - Sale" or trade =="S - Sale+OE": 
               fill.operacion="venta"
           fills =filing(date,code,company,trade,cargo,value,insider,qty,own,operacion)
           fillings.append(fills)
    
       for fill in fillings:
        key= str(fill.insider+fill.value+fill.date).replace("'", "")


        if key in contenido:
         print(key+"existe")
        else:
            
            
            
           print(key+"no existe")
          
       
           url1 = "http://localhost/generarActivo.php"

          
          
           insider_dict = fill.__dict__

# Convertir el diccionario a una cadena JSON
           insider_json = json.dumps(insider_dict, indent=2)
           makeRequest.makeRequest(url1, insider_json)

           #url2 = "https://econoba.martinruizptaskin.com.ar/php/insider.php"
           url2 = "http://localhost/generarActivo.php"
           makeRequest.makeRequest(url2, insider_json)


mainInsider()