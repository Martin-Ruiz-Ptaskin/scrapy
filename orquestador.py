# -*- coding: utf-8 -*-
"""
orquestador

This is a temporary script file.
"""
import time
import os


while 1==1:

 vueltas=0
 tiempo=0
 os.system('python scrapy/insiderstrack.py')
 os.system('python scrapy/maybeEtoroWin.py')
 os.system('python scrapy/superinvetors.py')
 while tiempo <1:
     print(tiempo)
     tiempo=tiempo+1
     
     os.system('python scrapy/PriceStock.py')
  
     time.sleep(800)
 vueltas= vueltas+1
 print("vueltas ------------------- " + str(vueltas)+ "------------------------")

