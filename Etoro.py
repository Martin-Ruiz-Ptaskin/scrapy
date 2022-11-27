# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:54:05 2022

@author: mruizpta
"""

import time
import random
import mysql.connector
from mysql.connector import Error
from selenium import webdriver 
from threading import Thread, Barrier
amount=[]
class innversor:
    def __init__(self,investor,stock):
        self.investor=investor
        self.stock = stock
        
"""---------------------------------------------------"""
        
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

mycursor = mydb.cursor()
"""mycursor.execute("SELECT * FROM bitcoin") cachelist=[]
myresult = mycursor.fetchall()


for rest in myresult:
    resultados= cartera(rest[0],rest[1])
    cachelist.append(resultados)"""
"""----------------------FIN CONECCION----------------------------"""
inversores=[]
def func(threads,url):


 
 vacios=[]
 for u in url: 
   driver = webdriver.Chrome(executable_path=r'C:\\Users\\mruizpta\\chromedriver_win32\\chromedriver.exe')
   
   time.sleep( random.randint(0,3))
   driver.get('https://www.etoro.com/people/'+u+'/portfolio')
   autos = driver.find_elements_by_xpath('//div[@class="i-portfolio-table-instrument"]')
   print(u," ",len(autos))
   
   if len(autos) ==0:
    print ("No tiene nada")
    vacios.append(u) 

   acciones=[] 
   if len(autos) >0:
       for auto in autos:
                # Por cada anuncio hallo el preico
        stock = auto.find_element_by_xpath('.//div[@class="i-portfolio-table-name"]').text
        """print(stock)"""
        acciones.append(stock)
       inversor= innversor(u,acciones)
       inversores.append(inversor) 
   driver.close()
 print(len(inversores),"inversores len")
 print(len(vacios),"vacios len")
 print(len(url),"url len")
 print(len(vacios)/len(url))
 while (len(vacios)/len(url))>0.25:
  for u in vacios: 
   driver = webdriver.Chrome(executable_path=r'C:\\Users\\mruizpta\\chromedriver_win32\\chromedriver.exe')
   
   time.sleep( random.randint(0,3))
   driver.get('https://www.etoro.com/people/'+u+'/portfolio')
   autos = driver.find_elements_by_xpath('//div[@class="i-portfolio-table-instrument"]')
   print(u," ",len(autos))
   print(u)
   
   if len(autos) ==0:
    print ("No tiene nada")
    

   acciones=[] 
   if len(autos) >0:
       vacios.remove(u)
       for auto in autos:
                # Por cada anuncio hallo el preico
        stock = auto.find_element_by_xpath('.//div[@class="i-portfolio-table-name"]').text
        """print(stock)"""
        acciones.append(stock)
       inversor= innversor(u,acciones)
       inversores.append(inversor) 
   driver.close()   
 print(len(inversores),"inversores len")
 print(len(vacios),"vacios len")
 print(len(url),"url len")
url =['garudolf','SiNeXo','JCA623','hambear','difaman','gauravk_in','HarpinderKang','jrotllant','BrunoBGomes','AntonioNobileC','JORDENBOER','Enslinjaco','ChineseMoney','yrm_capital','Saphirtal','Marinzgb','RauchenwaldC','Changweihsiao','hedge_fund','kingbravo10','creativemedia','CostelStoica','AmitKup','SwissWay','AlexKway','JeepsonTrading','acetoandrea','Alexebi','Nasdaki','bluewr','SalvadorMaV','LoicInv','Isiahjames','dhanpreet452','StanleyTaiwan','Annogo','adams302','OGFyahH','IngwarLattke','Flasky78','RiftenGuard','JDayTradesPro','jurajgazo','mrstocky','iliescu2605','SimoFo7','QualityHedge','Finanzzyklen','dipratom','ChaoyuanLee','smrinvestment','Tinak888','celesh','onlybacktesting','Praxantor','Charlotte2025','OliveTreeFund','Contraryfairy','raphaelpizzaia','GotfridsGirgens','Vibenpe','thomaspj','Matt1122','B3130jim','Ollipoud','olddriller','Walladoo','bryan01993','Josephpizza','FrancescoWeber','PraguermFx','Smahmood006','josephkfoury','xCorsarz_RCV','Steady-growth','Cipino90','ChartMatthew','Analisisciclico','felipehid','calintrading','jocjohnson','AndreaMarcon16','MaxDividend','ioatri','ingruc','HappyOwlz','Aukie2008','Stranden93','a11680','DmitriiIshutin','AnnGnep','PairsageGroup','RonaldTagsuan','conjepense','Floriana1']



cantidad=round(len(url)/(len(url)/3))
barrier = Barrier(cantidad)
def get_sublists(original_list, number_of_sub_list_wanted):
 sublists = list()
 for sub_list_count in range(number_of_sub_list_wanted): 
  sublists.append(original_list[sub_list_count::number_of_sub_list_wanted])
 return sublists
url=get_sublists(url, cantidad)
threads = []

for a in url:
 i = Thread(target=func, args=(barrier,a,))
 i.start()
 threads.append(i)

for i in threads:
 i.join()



        

print(len(amount))
for tag in inversores:
    print (tag.investor, tag.stock)
 
  
 
 
   