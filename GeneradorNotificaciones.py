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
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

"""---------------------------------------------------"""

connection = create_db_connection("localhost", "root", "", "scrapy")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
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
    def __init__(self,activo,cantidad,operador,value,interesados):
        self.activo=activo
        self.operador = operador+"[cantidad:"+str(cantidad)+",value:"+str(value)+"]"
        self.cantidad=cantidad
        self.value = value
        self.interesados = interesados

        
"""------inicio get assets"""

mycursor = mydb.cursor()
mycursor.execute("SELECT activo FROM `position traker`")
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
    Assets.append(activoFromBd(rest[1], rest[3], rest[2], rest[5],1))

"""----------------------- Fin Get Assets-----------------------------"""
def mainNoti():

    ActivosParaEvaluarName=[]
    ActivosParaEvaluar=[]
    EmitirNotificacion=[]
    for elemento in Assets:
        """Remuevo caracteres molestos"""
        if str(elemento.value).find(","):
                  elemento.value=str(elemento.value).replace(",", "")
        if str(elemento.value).find("$"):
                 elemento.value=str(elemento.value).replace("$", "")
        if str(elemento.value).find("+"):
                     print("tiene +")
                     elemento.value=elemento.value[1:]
        print(elemento.value)
        """----------------------------"""       
        if elemento.activo in ActivosParaEvaluarName:
         for value in ActivosParaEvaluar:

              if value.activo ==elemento.activo:
                 if len(str(value.value))>2:
                     
                  value.value==0 
                
                 if len(str(elemento.value))>2:    
                  if str(elemento.value[0])=="-" :
                      elemento.value= str(elemento.value).replace("-", "")
                      value.value= int(value.value)- (-1*int(elemento.value))
                 else:
                     elemento.value=0
                     
                
                 try:
                  value.value= int(value.value)+int(elemento.value)
                 except:
                     print("err")
                 value.cantidad+=elemento.cantidad
                 value.interesados+=1
                 value.operador+=","+elemento.operador+"[cantidad:"+str(elemento.cantidad)+",value:"+str(elemento.value)+"]"
         
        else:
         

         ActivosParaEvaluarName.append(elemento.activo)
         ActivosParaEvaluar.append(elemento)


    for activos in ActivosParaEvaluar:
        if activos.interesados>=2:
            EmitirNotificacion.append(activos)
        if str(activos.value)[0]=="-" :
             activos.value= str(activos.value).replace("-", "")
             activos.value=-1*int(activos.value)
             
        if int(activos.value) >2000000:
           
            EmitirNotificacion.append(activos)

    for noti in EmitirNotificacion:
      if noti.activo in nombresActivos:
          print("entra en el update " +noti.activo)
          update="UPDATE  `notificaciones` SET  `data`='"+noti.operador+"', `monto`='"+ str(noti.value) +"', `interesados`='"+str(noti.interesados)+"' WHERE 'activo'='"+noti.activo+"' "
          execute_query(connection, update)
      else:
       print("No es el update " +noti.activo)


       query="INSERT INTO `notificaciones`( `activo`, `data`, `monto`, `interesados`) VALUES ('"+noti.activo+"','" +noti.operador +"','"+str(noti.value) +"','"+ str(noti.interesados)+"')"
       execute_query(connection, query)
      
      ticker_yahoo = yf.Ticker(noti.activo)
      data = ticker_yahoo.history()
      last_quote = data['Close'].iloc[-1]
      print(noti.activo, last_quote)
      query2="INSERT INTO `position traker`( `activo`, `precioCompra`) VALUES ('"+noti.activo+"','" +last_quote+"')"
      execute_query(connection, query2)
mainNoti()