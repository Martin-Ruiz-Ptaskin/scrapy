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


class suoerinvestor:
    def __init__(self,date,code,company,tradetype,cargo,value,insider):
        self.date=date
        self.code = code
        self.company = company
        self.tradetype = tradetype
        self.title = cargo

        self.value = value
        self.insider = insider
datos = urllib.request.urlopen("http://feeds.feedburner.com/dataroma").read().decode()
def func():

 driver = webdriver.Chrome(executable_path=r'C:\\Users\\mruizpta\\chromedriver_win32\\chromedriver.exe')

 driver.get('https://www.dataroma.com/m/home.php')
 hold= driver.find_element_by_id("port_body")
 
 lock= hold.find_elements_by_xpath('.//a')
 for u in lock: 
   url= u.get_attribute('href')
   data = u.text.split('Updated')
   name=data[0]
   fecha= split(datetime.strptime(data[1][1:], '%d %b %Y')," ")
   

   today = date.today()
   print(fecha[0]<today)
   print(name,fecha,today)
   
   """ autoss = driver.find_elements_by_xpath('//ui-table-body[@class="ng-scope"]')
   autos = driver.find_elements_by_xpath('//div[@class="i-portfolio-table-instrument"]')"""
   

 driver.close() 
   

func()