# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 00:00:21 2023

@author: Usuario
"""
import sys
sys.path.append(r'C:\Users\Usuario\scrapy\conectorsql.py')

from selenium import webdriver 
from selenium.webdriver.common.by import By
import yfinance as yf
import mysql.connector
from mysql.connector import Error
        
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        ("MySQL Database connection successful")
    except Error as err:
        (f"Error: '{err}'")

    return connection

"""---------------------------------------------------"""

connection = create_db_connection("localhost", "root", "", "scrapy")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
       # print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
"""---------------------------------------------------"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="scrapy"
)
class activoFromBd:
    def __init__(self,activo,cantidad,operador,value,interesados,tipo):
        self.activo=activo
        self.operador ="[operador: "+str( operador)+", cantidad:"+str(cantidad)+", value:"+str(value)+", type:"+str(tipo)+"]"
        self.cantidad=cantidad
        self.value = value
        self.interesados = interesados
        self.tipo = tipo
        
"""------inicio get assets"""

mycursor = mydb.cursor()
mycursor.execute("SELECT activo FROM `notificaciones`")
myresult = mycursor.fetchall() 
nombresActivos=[]
for rest in myresult:
    resultados= rest[0]
    nombresActivos.append(resultados)
    
mycursor.execute("SELECT * FROM `activosenoperaciones`")

myresult = mycursor.fetchall() 
Assets=[]  
for rest in myresult:
    resultados= rest[0]
    Assets.append(activoFromBd(rest[1], rest[3], rest[2], rest[5],1,rest[7]))

mycursor.execute("SELECT activo FROM `position traker`")

myTrakedAssets = mycursor.fetchall() 
AssetsTracked=[]  
for rest in myTrakedAssets:
    AssetsTracked.append(rest[0])
"""----------------------- Fin Get Assets-----------------------------"""
def mainNoti():

    ActivosParaEvaluarName=[]
    ActivosParaEvaluar=[]
    EmitirNotificacion=[]
    """INSIDER PART"""
    for elemento in Assets:
        """Remuevo caracteres molestos"""
        print(elemento.value)
        try:
         if str(elemento.value).find(","):
                  elemento.value=str(elemento.value).replace(",", "")
         if str(elemento.value[0])=="-":
                 
                 elemento.value=str(int(elemento.value[2:])*-1)
         else :
                     elemento.value=str(elemento.value[2:])
        except Error as err:
            elemento.value=0
            print(f"Error: '{err}'")
        """----------------------------"""       
        if elemento.activo in ActivosParaEvaluarName:
         for value in ActivosParaEvaluar:

              if value.activo ==elemento.activo:
                 if len(str(value.value))>2:
                     
                  value.value==0 
                
                 
                     
                
                 try:
                  
                  value.value= int(value.value)+int(elemento.value)
                 except:
                     print("err")
                 """  value.cantidad+=elemento.cantidad
                 value.interesados+=1
                 print("-----------------------------------")
                 print( value.operador)
                 print("---------------")"""
                 value.operador+=";"+str( elemento.operador)
                 """ print( value.operador)
                 print("-----------------------------------")"""

        else:
         

         ActivosParaEvaluarName.append(elemento.activo)
         ActivosParaEvaluar.append(elemento)


    for activos in ActivosParaEvaluar:
        if activos.interesados>=2 and abs(int(activos.value)) >1000000:
            EmitirNotificacion.append(activos)
            continue
             
        
    """INSIDER PART FIN
    """        
    for noti in EmitirNotificacion:
      last_quote = 0
      try:
           
            ticker_yahoo = yf.Ticker(noti.activo)
            data = ticker_yahoo.history()
            last_quote = data['Close'].iloc[-1]
            if noti.activo in AssetsTracked: 
                
                print("update amount ")
                query2 = "UPDATE `position traker` SET `precioTop`='"+ str(float(last_quote))+"'  WHERE  `activo`= '"+noti.activo+"'" 
                execute_query(connection, query2)
            #(noti.activo, last_quote)
            else:
             query2="INSERT INTO `position traker`( `activo`, `precioCompra`) VALUES ('"+noti.activo+"','" +str(last_quote)+"')"
             execute_query(connection, query2)
      except:
           ("error al obtener cotizacion")
      if noti.activo in nombresActivos:
          ("entra en el update " +noti.activo)
          update="UPDATE  `notificaciones` SET  `data`='"+(noti.operador +"]" ) +"', `monto`='"+ str(noti.value) +"', `interesados`='"+str(noti.interesados)+"'  WHERE activo='"+noti.activo+"' "
          (update)
          execute_query(connection, update)
      else:
       ("No es el update " +noti.activo)


       query="INSERT INTO `notificaciones`( `activo`, `data`, `monto`, `interesados`, `Precio_int`  ) VALUES ('"+noti.activo+"','"+(noti.operador +"]" ) +"','"+str(noti.value) +"','"+ str(noti.interesados)+"','"+ str(last_quote) +"')"
       execute_query(connection, query)

mainNoti()
