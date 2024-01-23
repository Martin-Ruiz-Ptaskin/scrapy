# -*- coding: utf-8 -*-
"""
orquestador

This is a temporary script file.
"""
import time
import os
import requests
url = 'http://localhost:3000/'  # Exampleple URL

vueltas=0
while 1==1:


 tiempo=0
 try:
     print("entra insiderstrack")
     #os.system('python scrapy/insiderstrack.py')
     #os.system('python scrapy/maybeEtoroWin.py')
     print("entra superinvetors")
     os.system('python scrapy/superinvetors.py')
     print("entra GeneradorNotificaciones")
     os.system('python scrapy/GeneradorNotificaciones.py')
     print("vuelta fuera")
 except Exception as e:
    print(f"Se ha producido un error: {e}")
    
 while tiempo<3:
     tiempo+=1
     print(tiempo)
     print("vuelta dentro")
     if tiempo==1:
         response = requests.get(url)

         # Check if the request was successful (status code 200)
         if response.status_code == 200:
             # Print the response content (usually JSON or HTML)
             print("info envida")
         else:
             print(f"Request failed with status code {response.status_code}")
     if tiempo==2:
         #response = requests.get("http://localhost:3000/alive")
         if response.status_code == 200:
             # Print the response content (usually JSON or HTML)
             print("vive")
         else:
             print(f"Request failed with status code {response.status_code}")
         os.system('python scrapy/PriceStock.py')
         print("vivew")
     time.sleep(600)
 vueltas= vueltas+ 1
 print("vueltas ------------------- " + str(vueltas)+ "------------------------")

