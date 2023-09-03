# -*- coding: utf-8 -*-
"""
orquestador

This is a temporary script file.
"""
import time
import os
import requests
url = 'http://localhost:3000/'  # Example URL

vueltas=0
while 1==1:

 response = requests.get(url)

 # Check if the request was successful (status code 200)
 if response.status_code == 200:
     # Print the response content (usually JSON or HTML)
     print("info envida")
 else:
     print(f"Request failed with status code {response.status_code}")
 tiempo=0
 os.system('python scrapy/insiderstrack.py')
 #os.system('python scrapy/maybeEtoroWin.py')
 os.system('python scrapy/superinvetors.py')
 while tiempo< 1:
     print(tiempo)
     tiempo=tiempo+1
     
     #os.system('python scrapy/PriceStock.py')
  
     time.sleep(5)
 vueltas= vueltas+ 1
 print("vueltas ------------------- " + str(vueltas)+ "------------------------")

