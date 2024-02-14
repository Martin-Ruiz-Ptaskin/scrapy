# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 00:28:44 2024

@author: Usuario
"""
import requests
url = 'http://localhost:3000/'  # Exampleple URL
response = requests.get(url)

         # Check if the request was successful (status code 200)
if response.status_code == 200:
    print("succses request notificaciones")    
response = requests.get("http://localhost:3000/alive")
if response.status_code == 200:
 print("succses request alieve")    
