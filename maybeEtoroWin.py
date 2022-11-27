# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:28:46 2022

@author: Usuario
"""
import json
import requests
from selenium import webdriver 
driver = webdriver.Chrome(executable_path=r'C:\\Users\\mruizpta\\chromedriver_win32\\chromedriver.exe')
   
url =['RauchenwaldC']
""",'SiNeXo','JCA623','hambear','difaman','gauravk_in','HarpinderKang','jrotllant','BrunoBGomes','AntonioNobileC','JORDENBOER','Enslinjaco','ChineseMoney','yrm_capital','Saphirtal','Marinzgb','RauchenwaldC','Changweihsiao','hedge_fund','kingbravo10','creativemedia','CostelStoica','AmitKup','SwissWay','AlexKway','JeepsonTrading','acetoandrea','Alexebi','Nasdaki','bluewr','SalvadorMaV','LoicInv','Isiahjames','dhanpreet452','StanleyTaiwan','Annogo','adams302','OGFyahH','IngwarLattke','Flasky78','RiftenGuard','JDayTradesPro','jurajgazo','mrstocky','iliescu2605','SimoFo7','QualityHedge','Finanzzyklen','dipratom','ChaoyuanLee','smrinvestment','Tinak888','celesh','onlybacktesting','Praxantor','Charlotte2025','OliveTreeFund','Contraryfairy','raphaelpizzaia','GotfridsGirgens','Vibenpe','thomaspj','Matt1122','B3130jim','Ollipoud','olddriller','Walladoo','bryan01993','Josephpizza','FrancescoWeber','PraguermFx','Smahmood006','josephkfoury','xCorsarz_RCV','Steady-growth','Cipino90','ChartMatthew','Analisisciclico','felipehid','calintrading','jocjohnson','AndreaMarcon16','MaxDividend','ioatri','ingruc','HappyOwlz','Aukie2008','Stranden93','a11680','DmitriiIshutin','AnnGnep','PairsageGroup','RonaldTagsuan','conjepense','Floriana1']"""
gcid=[]
for u in url: 
    driver.get('https://www.etoro.com/api/logininfo/v1.1/users/'+ u.lower() +'?client_request_id=cfb768a2-8ff4-4166-8d60-0fb25f68c9e5')
    data = driver.find_elements_by_xpath('//pre')[0].text
    datajson=json.loads(data)
    gcid.append(datajson["realCID"])
    print(datajson)
for id in gcid:
    print (id)
    driver.get('https://www.etoro.com/sapi/trade-data-real/live/public/portfolios?cid='+ str(id) +'&client_request_id=2db01e24-a694-4da2-8d33-2607731e15eb')
    data = driver.find_elements_by_xpath('//pre')[0].text
    datajson=json.loads(data)
    print(datajson)

""" driver.get('https://www.etoro.com/sapi/trade-data-real/live/public/portfolios?cid='+u+'&client_request_id=2db01e24-a694-4da2-8d33-2607731e15eb')"""
