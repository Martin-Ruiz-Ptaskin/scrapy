# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:28:46 2022

@author: Usuario
VER ESTO PARA PRECIO DE ACTIVOS
https://api.etorostatic.com/sapi/instrumentsmetadata/V1.1/instruments/bulk?bulkNumber=1&cv=3d7fb2671fb8b4a97f3b7ad1ce5b0dc6_56427fb9fa56ff5eb047b7a38803ffec&totalBulks=1
"""
import json
import requests
import json
from selenium import webdriver 
driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
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

class investor:
    def __init__(self,name,assets,realCID):
        self.name=name
        self.assets = assets
        self.realCID = realCID

class assetsId:
    def __init__(self,id,assets):
        self.id=id
        self.assets = assets
        
        
class ListaActivosInversor:
    def __init__(self,name,value,compradores):
        self.name=name
        self.value = value
        self.compradores=compradores
        
        
"""DEVUELVE ASSET POR ID"""        
def existe_asset_con_id(id_deseado, lista):
    for i, asset in enumerate(lista):
        if asset.name == id_deseado:
            return True, i
    return False, -1

"""VER DIFERENCIAS"""
assets_vendidos=[]
assets_comprados=[]

def crearNotificaciones(ActyvityFromBD,activity,name):
    frombd=json.loads(ActyvityFromBD)
    actividad=json.loads(activity)
    
    for activo in frombd:
        
          for activoEnWeb in actividad:
            if(activo['InstrumentID']==activoEnWeb['InstrumentID']):
  
              

               diferencia= int(activo['Invested'])-int(activoEnWeb['Invested'])
               if(diferencia <0):
                       existe=0
                       operacion="venta"
                       for obj in assets_comprados:
                         if obj.name == activo['InstrumentID']:
                           obj.compradores=obj.compradores+1
                           existe=1
                           
                         
                       if existe==0 :
                          
                        assets_vendidos.append(ListaActivosInversor(activo['InstrumentID'],diferencia,0))
                       print("activosenoperaciones")
                       query2 = "INSERT INTO `activosenoperaciones`(`activo`, `operador`,`cantidad`,`value`,`movimiento`) VALUES ('" + \
                       activo['InstrumentID']+ "','"+name+ "','"+str(diferencia)+ "','-','"+ operacion + "')"
                       execute_query(connection, query2)
               if(diferencia >0):
                       operacion="compra"

                       existe=0
                       for obj in assets_vendidos:
                         if obj.name == activo['InstrumentID']:
                           obj.compradores=obj.compradores+1
                           existe=1
                        
                       if existe==0 :
                         assets_comprados.append(ListaActivosInversor(activo['InstrumentID'],diferencia,0))
                       print("activosenoperaciones")

                       query2 = "INSERT INTO `activosenoperaciones`(`activo`, `operador`,`cantidad`,`value`,`movimiento`) VALUES ('" + \
                       activo['InstrumentID']+ "','"+name+ "','"+str(diferencia)+ "','-','"+ operacion + "')"
                       execute_query(connection, query2)




mycursor = mydb.cursor()

def Etoromain():
    mycursor.execute("SELECT * FROM `inversores`")
    cachelist=[]
    myresult = mycursor.fetchall()        
    for rest in myresult:
       resultados= investor(rest[1],rest[2],"")
       cachelist.append(resultados)

    url =['robier89','JCA623','JORDENBOER','Enslinjaco','ChineseMoney']
    """,'SiNeXo','BrunoBGomes','AntonioNobileC','JORDENBOER','Enslinjaco','ChineseMoney','yrm_capital','Saphirtal','Marinzgb','RauchenwaldC','Changweihsiao','hedge_fund','kingbravo10','creativemedia','CostelStoica','AmitKup','SwissWay','AlexKway','JeepsonTrading','acetoandrea','Alexebi','Nasdaki','bluewr','SalvadorMaV','LoicInv','Isiahjames','dhanpreet452','StanleyTaiwan','Annogo','adams302','OGFyahH','IngwarLattke','Flasky78','RiftenGuard','JDayTradesPro','jurajgazo','mrstocky','iliescu2605','SimoFo7','QualityHedge','Finanzzyklen','dipratom','ChaoyuanLee','smrinvestment','Tinak888','celesh','onlybacktesting','Praxantor','Charlotte2025','OliveTreeFund','Contraryfairy','raphaelpizzaia','GotfridsGirgens','Vibenpe','thomaspj','Matt1122','B3130jim','Ollipoud','olddriller','Walladoo','bryan01993','Josephpizza','FrancescoWeber','PraguermFx','Smahmood006','josephkfoury','xCorsarz_RCV','Steady-growth','Cipino90','ChartMatthew','Analisisciclico','felipehid','calintrading','jocjohnson','AndreaMarcon16','MaxDividend','ioatri','ingruc','HappyOwlz','Aukie2008','Stranden93','a11680','DmitriiIshutin','AnnGnep','PairsageGroup','RonaldTagsuan','conjepense','Floriana1']

    """
    totalDivider=len(url)
    investors=[]

    urlAssets='https://api.etorostatic.com/sapi/instrumentsmetadata/V1.1/instruments/bulk?bulkNumber=1&cv=3d7fb2671fb8b4a97f3b7ad1ce5b0dc6_56427fb9fa56ff5eb047b7a38803ffec&totalBulks=1'
    assets=[]
    activosGenerales=[]
    response = requests.get(urlAssets)

    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener el contenido de la respuesta
        contenido = json.loads(response.content)
        for asset in contenido['InstrumentDisplayDatas']:
            activo=assetsId(asset['InstrumentID'], asset['SymbolFull'])
            assets.append(activo)
        

    """print(assetsjson)"""
    for u in url:
        driver.get('https://www.etoro.com/api/logininfo/v1.1/users/'+ u.lower() +'?client_request_id=cfb768a2-8ff4-4166-8d60-0fb25f68c9e5')
        data = driver.find_elements(By.XPATH,'//pre')[0].text
        datajson=json.loads(data)
        investorObjet=investor(u, "", datajson["realCID"])
        investors.append(investorObjet)
    for id in investors:
        
        driver.get('https://www.etoro.com/sapi/trade-data-real/live/public/portfolios?cid='+ str(id.realCID) +'&client_request_id=2db01e24-a694-4da2-8d33-2607731e15eb')
        data = driver.find_elements(By.XPATH,'//pre')[0].text
        try :
         datajsonUsr=json.loads(data)['AggregatedPositions']
        except:
            datajsonUsr=""
            totalDivider-=1
        for activoDeInversor in datajsonUsr :
            assets_filtrados = list(filter(lambda asset: asset.id ==activoDeInversor['InstrumentID'] , assets))
            activoDeInversor['InstrumentID']=assets_filtrados[0].assets
            for objeto in activosGenerales:
                if objeto.name == assets_filtrados[0].assets:
                    """print("ya paso " +objeto.name)"""
                    objeto.value = activoDeInversor['Invested']
                    objeto.compradores=  objeto.compradores+1
                    break
            
            else:
                activosGenerales.append(ListaActivosInversor(assets_filtrados[0].assets,(activoDeInversor['Invested']/ totalDivider ),1))

        id.assets=datajsonUsr
        existe=0
        activityFromBD=""
        for cache in cachelist:
         print(cache.name)
         if cache.name == id.name:
            existe = 1
            activityFromBD = cache.assets

        if (existe == 1):
         print("entra en update")
         crearNotificaciones(activityFromBD,json.dumps(datajsonUsr),cache.name)
         query = "UPDATE `inversores` SET `stocks`='" + \
           json.dumps(datajsonUsr) +"' WHERE `name`='" + id.name + "'"
         """execute_query(connection, query)"""

        else:
         print("entra en insert")

         query = "INSERT INTO `inversores`(`name`, `stocks`) VALUES ('" + \
          id.name + "','"+json.dumps(id.assets)+"')"
         execute_query(connection, query)
         
         
    etiquetas = [] # Etiquetas para cada porción de la torta
    valores = [] # Valores para cada porción de la torta

    for a in activosGenerales:
        etiquetas.append(a.name)
        valores.append((a.value)/totalDivider)
        
        """print(a.name +" " + str(a.value) + " " +str(a.compradores))"""
        


    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90) # Utiliza la función pie() para crear el gráfico de torta
    plt.title('Gráfico de Torta') # Establece el título del gráfico

    # Mostrar el gráfico
    plt.show()
Etoromain()