# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:46:50 2023

@author: Usuario
"""

import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver 
driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
from selenium.webdriver.common.by import By

span="span[@jsname = 'vWLAgc']"
driver.get('https://www.google.com/search?q=TSLA+stock&rlz=1C1CHBF_esAR1047AR1047&sxsrf=APwXEdde7_SzTvOQVk0YnM1lmenH53LvrA%3A1682299487637&ei=X9pFZPq6JsPS1sQP16GJ6A8&ved=0ahUKEwi65vb6rcH-AhVDqZUCHddQAv0Q4dUDCA8&uact=5&oq=APPL+stock&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCAAQigUQQzIHCAAQgAQQCjIHCAAQgAQQCjINCC4QrwEQxwEQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjINCC4QrwEQxwEQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjoKCAAQRxDWBBCwAzoKCAAQigUQsAMQQzoGCAAQBxAeOhAILhCKBRCxAxDHARDRAxBDOgoIIxCwAhAnEJ0COgcIABANEIAEOg0ILhANEK8BEMcBEIAEOgoIIxCxAhAnEJ0CSgQIQRgAUIgLWPEbYJAhaANwAXgAgAHAAYgB9gSSAQM1LjGYAQCgAQHIAQrAAQE&sclient=gws-wiz-serp')
data = driver.find_elements(By.XPATH,"//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/g-card-section[1]/div[1]/g-card-section[1]/div[2]/div[1]/span[1]/span[1]/span[1]")[0].text