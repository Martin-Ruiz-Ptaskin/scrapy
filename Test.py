# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 21:35:11 2022

@author: mruizpta
"""

import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver 

class hedgefound:
    def __init__(self,name,portfolioPart,activity,value):
        self.name=name
        self.portfolioPart = portfolioPart
        self.activity = activity
        self.value = value
driver = webdriver.Chrome(executable_path=r'C:\\Users\\mruizpta\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.dataroma.com/m/holdings.php?m=GA')
hold= driver.find_element_by_id("grid")
data=[]
lock= hold.find_elements_by_xpath('.//tr')
lock.pop(0)
sample_dict = dict()
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
    print(i.name)
    print(i.portfolioPart)
    print(i.activity)
    print(i.value)
