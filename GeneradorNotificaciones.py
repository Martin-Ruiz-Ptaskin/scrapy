# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 00:00:21 2023

@author: Usuario
"""
import sys
sys.path.append(r'C:\Users\Usuario\scrapy\conectorsql.py')
from datetime import datetime, timedelta

from selenium import webdriver 
from selenium.webdriver.common.by import By
import yfinance as yf
import DBconection as BD
import EconomicCalendar
import requests
import json
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 18:47:59 2023

@author: Usuario
"""

import mysql.connector
from mysql.connector import Error
BD.entorno
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
if BD.entorno!="prod":
    connection = create_db_connection("localhost", "root", "", "scrapy")
if BD.entorno=="prod":
    connection = create_db_connection("50.87.144.185", "datodtal_scrapy", "%V]B]Rvvl}uo", "datodtal_scrapy")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        #print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
"""---------------------------------------------------"""
if BD.entorno!="prod":
    print("hostBD :localhost")
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="scrapy"
    )

if BD.entorno=="prod":
    mydb = mysql.connector.connect(
  host="50.87.144.185",
  user="datodtal_scrapy",
  password="%V]B]Rvvl}uo",
  database="datodtal_scrapy"
)
cursor = mydb.cursor()

class activoFromBd:
    def __init__(self,idOp,activo,cantidad,operador,value,interesados,tipo,position,own,bigsell,idList,fecha):
        self.activo=activo
        self.idOp=idOp

        self.operador ='{"operador": "'+str( operador)+'", "cantidad":"'+str(cantidad)+'", "value":"'+str(value)+'", "type":"'+str(tipo)+'", "cargo":"'+str(position)+'", "own":"'+str(own)+'", "fecha":"'+str(fecha)+'"}'
        self.cantidad=cantidad
        self.value = value
        self.interesados = interesados
        self.tipo = tipo
        self.position = position
        self.own = own
        self.bigsell=bigsell
        self.idList=[idOp]
        self.fecha=[fecha]
    def to_json(self):
        try:
            operador_dict = json.loads(self.operador)
        except json.decoder.JSONDecodeError as e:
            # Handle the case where self.operador is not a valid JSON string
            print(f"Error decoding JSON: {e}")
            operador_dict = None

        return {
            "idOp": self.idOp,
            "activo": self.activo,
            "operador": operador_dict,  # Convert the operador string to a dictionary
            "cantidad": self.cantidad,
            "value": self.value,
            "interesados": self.interesados,
            "tipo": self.tipo,
            "position": self.position,
            "own": self.own,
            "bigsell": self.bigsell,
            "idList": self.idList,
            "fecha": self.fecha.isoformat() if isinstance(self.fecha, datetime) else None
        }

        
class notificacionesExistentes:
    def __init__(self,activo,idList):
        self.activo=activo
        self.idList =idList
       
"""------inicio get assets"""

mycursor = mydb.cursor()
mycursor.execute("SELECT activo,relatedActivosEnOperacion FROM `notificaciones` where tipoNotificacion='Insider' " )
myresult = mycursor.fetchall() 
nombresActivos=[]
for rest in myresult:
    
    nombresActivos.append(notificacionesExistentes(rest[0],rest[1]))
fecha_actual = datetime.now()

# Restar un mes
fecha_mes_pasado = fecha_actual - timedelta(days=160)  # Se asume que un mes tiene aproximadamente 30 días

# Formatear la fecha en el formato deseado
fecha_formateada = fecha_mes_pasado.strftime("%Y-%m-%d")   

mycursor.execute("SELECT *FROM `activosenoperaciones` WHERE `fecha` >="+fecha_formateada+"")
print("SELECT *FROM `activosenoperaciones` WHERE `fecha` >`"+fecha_formateada+"`")

myresult = mycursor.fetchall() 
Assets=[]  
for rest in myresult:
    print(rest[0])
    resultados= rest[0]
    Assets.append(activoFromBd(rest[0],rest[1], rest[3], rest[2], rest[5],1,rest[7],rest[9],rest[8],0,[],rest[4]))

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
        try:
        
             
             if elemento.own and str(elemento.own).find("%"):
                         if elemento.own != "New":
                        
                          elemento.own= abs(int(float((str(elemento.own).replace("%", "").replace(">", "")))))
                       
             if str(elemento.value).find(","):
                      elemento.value=str(elemento.value).replace(",", "")
             if str(elemento.value[0])=="-":
                     
                     elemento.value=str(int(elemento.value[2:])*-1)
             else :
                         elemento.value=str(elemento.value[2:])
         
        except Error as err:
            elemento.value=0
            print(err)
        """----------------------------"""       
        if elemento.activo in ActivosParaEvaluarName:
        
         for value in ActivosParaEvaluar:
              if value.activo ==elemento.activo:

                 if len(str(value.value))>2:
                     
                  value.value==0 
                
                 
                     
                
                 try:
                  """Sumo el valor de todas las ventas de los insider"""
                  value.idList.append(elemento.idOp)

                  if value.tipo != "fund":
                   value.value= int(value.value)+int(elemento.value)

                  if(elemento.own >25):
                      value.bigsell=+1
                      print(value.bigsell)
                 except:
                     print("err")
                 value.cantidad+=elemento.cantidad
                 value.interesados+=1
                
                 value.operador+=","+str( elemento.operador)+""
                 """ print( value.operador)
                 print("-----------------------------------")"""

        else:
         
         ActivosParaEvaluarName.append(elemento.activo)
         ActivosParaEvaluar.append(elemento)


    for activos in ActivosParaEvaluar:
        """Validaciones para emitir notificaciones"""
        
        if activos.interesados>=7 and abs(int(activos.value)) <1000000:

            EmitirNotificacion.append(activos)
            continue
        if activos.interesados>=2 and abs(int(activos.value)) >1000000:
            EmitirNotificacion.append(activos)
            continue
            
        if  abs(int(activos.value)) >1000000 and activos.bigsell==1:
             EmitirNotificacion.append(activos)
             continue    
        
    """INSIDER PART FIN
    """        
    for noti in EmitirNotificacion:
      last_quote = 0
      existe=0
      continues=0
      for enBD in nombresActivos:
          """Verifico si existe y """
          """Si Existe se queda en 0 quiere decir que no hay nuevos en el subset y si es 1, si continues es 1 quiere decir que debe continuar ya que no hay nada nuevo que agregar """
          if noti.activo ==enBD.activo:
              print("es aca")
              print(noti.activo)
                  
              set1 = set(noti.idList)
              set2 = set(eval(enBD.idList))
              #print(set1,set2 , noti.activo)
              if set1.issubset(set2):
               continues=1
               print("ya existe")
               break
              else:
               print("no existe")

               existe=1
               break
               
      if continues==0:
            print("pasa a la 2")
            try:
                
             fechaEconomica=EconomicCalendar.calendarUpdate(noti.activo)
             ticker_yahoo = yf.Ticker(noti.activo)
             #print(ticker_yahoo)

             #print(fechaEconomica)
             data = ticker_yahoo.history()
             last_quote = data['Close'].iloc[-1]

            except:
                print("err al obtener fecha economica")
            
            BigSellMultiplication=1
            fechaEconimocaMultipliation=1
            if noti.bigsell>1:
                BigSellMultiplication*noti.bigsell
            if fechaEconomica !=False:
                fechaEconimocaMultipliation*2
                fechaEconomica=""
            importancia=0
            """ print(BigSellMultiplication)
            print(fechaEconimocaMultipliation)
            print(int(noti.value)/200000)
            print((int(noti.interesados)/10))

            print(BigSellMultiplication)
            print(fechaEconimocaMultipliation)"""
            print(existe)
            importancia=abs( ( ( (int(noti.value)/200000) * (1+(int(noti.interesados)/10) ) )*BigSellMultiplication)*fechaEconimocaMultipliation)
            """Ver aca"""
            if  noti.activo in AssetsTracked: 
                
                print("update amount ")
                query2 = "UPDATE `position traker` SET `precioTop`='"+ str(float(last_quote))+"', precioMin='"+ str(float(last_quote))+"'  WHERE  `activo`= '"+noti.activo+"'" 
                print(query2)

                execute_query(connection, query2)
            #(noti.activo, last_quote)
            else:
             query2="INSERT INTO `position traker`( `activo`, `precioCompra`, `precioTop`, `precioMin`) VALUES ('"+noti.activo+"','" +str(last_quote)+"','" +str(last_quote)+"','" +str(last_quote)+"')"
             execute_query(connection, query2)
     
            ("error al obtener cotizacion")
            if existe==1:
             ("deberia entrar en el update " +noti.activo)
             update="UPDATE  `notificaciones` SET  `data`='"+("["+noti.operador +"]" ) +"', `monto`='"+ str(noti.value) +"', `relatedActivosEnOperacion`='"+ str(noti.idList) +"',`interesados`='"+str(noti.interesados)+"' , `Importancia`='"+str(importancia)+"' , `ExtraData`='"+str(fechaEconomica)+"', `usado`=0    WHERE activo='"+noti.activo+"' "
              
             execute_query(connection, update)
            else:
             print("No es el update " +noti.activo)
             query="INSERT INTO `notificaciones`( `activo`, `data`, `monto`, `interesados`, `Precio_int`, `tipoNotificacion`,`importancia` ,`ExtraData`,`relatedActivosEnOperacion`   ) VALUES ('"+noti.activo+"','"+("["+noti.operador +"]" ) +"','"+str(noti.value) +"','"+ str(noti.interesados)+"','"+ str(last_quote) +"','Insider','"+ str(importancia) +"','"+ str(fechaEconomica) +"','"+ str(noti.idList) +"')"
             execute_query(connection, query)
            customNotification(noti.activo)    

def customNotification(asset_deseado):
    query_paso_1 = f"SELECT webID FROM stockprice WHERE asset = '{asset_deseado}'"
    webID_result = None
    
    try:
        mycursor.execute(query_paso_1)
        resultadosSQL=mycursor.fetchall()
        print(webID_result)
    except Error as err:
        print(f"Error: '{err}'")
   
    
    if resultadosSQL:
        webID_result = resultadosSQL[0]

        webID_obtenido = webID_result[0]
    
        # Paso 2: Buscar en la tabla usuarios si el webID está en la columna assets
        query_paso_2 = f"SELECT name FROM usuarios WHERE FIND_IN_SET('{webID_obtenido}', assets) > 0"
        usuarios_result = None
    
        try:
            cursor.execute(query_paso_2)
            usuarios_result = cursor.fetchall()
        except  Error as err:
            print(f"Error: '{err}'")
           
    
        if usuarios_result:
            print("Usuarios encontrados:")
            for row in usuarios_result:
                print("row")
                print(row)
                url = 'http://localhost:3000/customNotification'
                try:

                    data = {
                        'users': row,
                        'info':asset_deseado
                    }
                    requests.post(url,json=data)
                except requests.exceptions.RequestException as e:
                    # Handling exceptions
                    print(f'Error making the POST request: {e}')
        else:
            print("No se encontraron usuarios con el webID en la columna assets.")
    else:
        print("No se encontró webID para el asset "+ asset_deseado)
        query="INSERT INTO stockprice (asset, webID) SELECT '"+asset_deseado+"', MAX(webID) + 1 FROM stockprice; "
        execute_query(connection,query)

mainNoti()
#customNotification("nvda","hoal")