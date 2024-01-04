# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:28:46 2023

@author: Usuario
VER ESTO PARA PRECIO DE ACTIVOS
https://api.etorostatic.com/sapi/instrumentsmetadata/V1.1/instruments/bulk?bulkNumber=1&cv=3d7fb2671fb8b4a97f3b7ad1ce5b0dc6_56427fb9fa56ff5eb047b7a38803ffec&totalBulks=1
"""
import json
import requests
import json
from selenium import webdriver 
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import DBconection as BD
"""-------------------------------------------------"""
mycursor =  BD.mydb.cursor()
mycursor.execute("SELECT  asset FROM `stockprice`  " )
myresult = mycursor.fetchall() 
nombresActivos=[]
for rest in myresult:
    
    nombresActivos.append(rest[0])


driver = webdriver.Chrome(executable_path=r'C:\Users\Usuario\scrapy\chromedriver.exe')
driver.get('https://api.etorostatic.com/sapi/instrumentsmetadata/V1.1/instruments/bulk?bulkNumber=1&cv=2e55718c9eb4e6c6e66008e88f0adf7a_1f8f66afa7d0d88dfa6a30e657e6c40a&totalBulks=1')
dataAsset = driver.find_elements(By.XPATH,'//pre')[0].text
datajsonAsset=json.loads(dataAsset)
instrument_map = {}
#OBTENGO INFO DE LOS ACTIVOS
for instrument in datajsonAsset["InstrumentDisplayDatas"]:
  if instrument["IsInternalInstrument"] != True:
    instrument_id = instrument["InstrumentID"]
    symbol_full = instrument["SymbolFull"]
    InstrumentDisplayName=instrument["InstrumentDisplayName"]

    image_uri = instrument["Images"][2]["Uri"]
    instrument_map[instrument_id] = {"SymbolFull": symbol_full, "ImageURI": image_uri, "instrument_id": instrument_id,"InstrumentDisplayName":InstrumentDisplayName}
#OBTENGO PRECIO DE LOS ACTIVOS"""

driver.get('https://api.etorostatic.com/sapi/candles/closingprices.json?cv=2679181eacb94174273960facfcac4c8_acaacaf19d0c11e0b5936698f216eb94')
dataPrice = driver.find_elements(By.XPATH,'//pre')[0].text
datajsonPrice=json.loads(dataPrice)
driver.close()
for element in datajsonPrice:
    instrument_id = element["InstrumentId"]
    closing_price = element["OfficialClosingPrice"]

    # Verificar si el InstrumentID existe en el instrument_map
    if instrument_id in instrument_map:
        # Agregar OfficialClosingPrice al instrument_map
        instrument_map[instrument_id]["OfficialClosingPrice"] = closing_price

# Imprimir el instrument_map actualizado

for key, assets in instrument_map.items():
  if  assets["SymbolFull"] in nombresActivos :
#si existe en bd
    print("------------------ en bd")
    if "OfficialClosingPrice" in assets:
          """print("tiene ")"""
    else:
          assets["OfficialClosingPrice"]=""
    query2 = "UPDATE `stockprice` SET `price`='"+ str( assets["OfficialClosingPrice"])+"'WHERE  `asset`= '"+assets["SymbolFull"]+"'" 

    print(query2)

    BD.execute_query(BD.connection, query2)    


  else:
      #si no existe en bd
      print("------------------ no en bd")

      if "OfficialClosingPrice" in assets:
          """print("tiene closin")"""
      else:
          assets["OfficialClosingPrice"]=""
      query = "INSERT INTO `stockprice`(`asset`, `price`,`webID`,`displayName`,`img`) VALUES ('" + assets["SymbolFull"] + "','"+ str(assets["OfficialClosingPrice"])+"','"+ str(assets["instrument_id"])+"','"+ assets["InstrumentDisplayName"]+"','"+ assets["ImageURI"]+"')"
      BD.execute_query(BD.connection, query)