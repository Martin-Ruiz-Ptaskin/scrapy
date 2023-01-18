# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 21:35:11 2022

@author: mruizpta
"""

import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver 
    
driver = webdriver.Chrome(executable_path=r'C:\\Users\\mruizpta\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.dataroma.com/m/holdings.php?m=GA')
hold= driver.find_element_by_id("grid")

lock= hold.find_elements_by_xpath('.//tr')
for l in lock:
    name=l.find_elements_by_xpath('.//td')
    print (name[1].text)
