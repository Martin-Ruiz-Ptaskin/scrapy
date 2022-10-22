# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:10:37 2022

@author: mruizpta
"""

import time
from selenium import webdriver 
from threading import Thread, Barrier

def func(threads,url):
 driver = webdriver.Chrome(executable_path=r'C:\\Users\\mruizpta\\chromedriver_win32\\chromedriver.exe')
 driver.get(url)

 autos = driver.find_elements_by_xpath('//app-card-car')
 print (url)
        
        # Recorro cada uno de los anuncios que he encontrado
 for auto in autos:
            # Por cada anuncio hallo el preico
  precio = auto.find_element_by_xpath('.//span[@class="payment-total payment-highlight"]').text
  print (precio)
 driver.close()
 
 
	

url =['https://www.kavak.com/ar/tipo-suv/autos-Q2/ano-2018/transmision-Automatica/autos-usados','https://www.kavak.com/ar/comprar-Bmw/autos-Q2/autos-usados',"https://www.kavak.com/ar/autos-Ds3/color-Gris/autos-usados",'https://www.kavak.com/ar/comprar-Smart/color-Gris/autos-usados']

numero_multitareas = 6

barrier = Barrier(numero_multitareas)

threads = []

for a in url:
 i = Thread(target=func, args=(barrier,a,))
 i.start()
 threads.append(i)

for i in threads:
 i.join()
 