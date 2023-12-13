import yfinance as yf
from datetime import datetime
import pytz
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 18:47:59 2023

@author: Usuario
"""

import DBconection as BD



        
"""------inicio get assets"""

mycursor = BD.mydb.cursor()
mycursor.execute("SELECT asset FROM `economiccalendar`")
myresultCalendar = mycursor.fetchall() 
nombresActivosCalendar=[]
for rest in myresultCalendar:
    resultados= rest[0]
    nombresActivosCalendar.append(resultados)



def calendarUpdate(activoName):
    try:
     stockCalendar = yf.Ticker(activoName)
     dataCalendar= ( stockCalendar.get_earnings_dates())
     fechas_lista = dataCalendar.index.tolist()
    except BD.Error as err:
        print(err)
    try:    
        current_date = datetime.now(pytz.timezone('America/New_York'))
    
        #Encontrar el Timestamp más cercano a la fecha actual
        fechas_futuras = [fecha for fecha in fechas_lista if fecha >= current_date]
        
        #Encontrar la fecha más cercana en el futuro
        fecha_mas_cercana_futuro = min(fechas_futuras, default=None)
        #print(fechas_lista)
        if len(fechas_futuras) >0:
         row_data = dataCalendar.loc[fecha_mas_cercana_futuro]
        else:
            
         return False
        if activoName in nombresActivosCalendar:
          """noda"""
        else:
            query = "INSERT INTO `economiccalendar`(`asset`, `date`,`EPS`) VALUES ('" + str(activoName) + "','"+ str(fecha_mas_cercana_futuro)+ "','"+ str(row_data.values[0])+ "')"  
            
            BD.execute_query(BD.connection, query)
    except BD.Error as err:
       print(err)
    return    dias_faltantes(fecha_mas_cercana_futuro)



def dias_faltantes(fecha_futura_str):
    # Obtener la fecha actual en la zona horaria de Argentina
    zona_horaria_argentina = pytz.timezone('America/Argentina/Buenos_Aires')
    fecha_actual = datetime.now(zona_horaria_argentina).date()

    # Convertir la cadena de fecha futura a un objeto datetime sin zona horaria
    fecha_futura = datetime.strptime(str(fecha_futura_str), "%Y-%m-%d %H:%M:%S%z").replace(tzinfo=None)

    # Calcular la diferencia entre la fecha futura y la fecha actual
    diferencia = fecha_futura.date() - fecha_actual

    # Obtener el número de días faltantes
    dias_faltantes = diferencia.days
    if dias_faltantes<45:
        return fecha_futura_str
    else :
     return False
