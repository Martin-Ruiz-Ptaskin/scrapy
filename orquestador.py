# -*- coding: utf-8 -*-
"""
orquestador

This is a temporary script file.
"""
import time

import superinvetors
time.sleep(2)

import insiderstrack
time.sleep(2)

import maybeEtoroWin
time.sleep(2)
import GeneradorNotificaciones

import PriceStock
while 1==1:

 #superinvetors.superInvestorsMain()
 time.sleep(5)
 insiderstrack.mainInsider()
 time.sleep(5)

 #maybeEtoroWin.Etoromain()
 time.sleep(4)
 print("notificaciones")
 GeneradorNotificaciones.mainNoti()
 time.sleep(4)
 tiempo=0
 while tiempo <2:
     print(tiempo)
     tiempo=tiempo+1
     PriceStock.mainPrice()
     time.sleep(100)


