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
from mysql.connector import Error

class suoerinvestor:
    def __init__(self,date,code,company,tradetype,cargo,value,insider):
        self.date=date
        self.code = code
        self.company = company
        self.tradetype = tradetype
        self.title = cargo

        self.value = value
        self.insider = insider
def func():
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
     contenido = open(r"C:\Users\mruizpta\scrapy\superinvestorkeylist.txt", "r")
     previos=[]
    
     for línea in contenido:
      lista=línea
      previos=lista.split("/")
      """print (previos)"""
            
     contenido.close()
     driver.get('https://www.dataroma.com/m/home.php')
     hold= driver.find_element_by_id("port_body")
     
     lock= hold.find_elements_by_xpath('.//a')
     contenido = open(r"C:\Users\mruizpta\scrapy\superinvestorkeylist.txt", "w")
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

       
       
     driver.close() 
 

func()


