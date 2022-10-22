# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:06:30 2022

@author: mruizpta
"""

import urllib.request
import time
from bs4 import BeautifulSoup

class filing:
    def __init__(self,date,code,company,tradetype,cargo,value,insider):
        self.date=date
        self.code = code
        self.company = company
        self.tradetype = tradetype
        self.title = cargo

        self.value = value
        self.insider = insider
while 1==1:
    
    datos = urllib.request.urlopen("http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=730&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&xs=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1").read().decode()

    soup =BeautifulSoup(datos)
    table = soup.find_all("tbody")
    line =table[1].find_all("tr")
    """filing=filing("hoy","TSLA","teska","BUY","CEO","1000","Elon")"""
    fillings=[]
    for fill in line:
        date=fill.find_all("td")[1].find_all("a")[0].getText();
        code= fill.find_all("td")[3].find_all("a")[0].getText()
        company =fill.find_all("td")[4].find_all("a")[0].getText()
        insider =fill.find_all("td")[5].find_all("a")[0].getText()
        cargo= fill.find_all("td")[6].getText()
        trade =fill.find_all("td")[7].getText()
        value =fill.find_all("td")[12].getText()
        fills =filing(date,code,company,trade,cargo,value,insider)
        fillings.append(fills)  
    print(fillings[0].company,fillings[1].company)
    time.sleep(10)


"""1 date ,3 code,4 company, 5 insider, 6 cargo, 7 trade tyoe, 12 value"""