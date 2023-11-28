# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 12:28:26 2023

@author: Usuario
"""

from yahooquery import Ticker
from yahooquery import search
from datetime import datetime
import json
class valuation_measures:
    def __init__(self,asOfDate,activo,EnterpriseValue,EnterprisesValueEBITDARatio,EnterprisesValueRevenueRatio,ForwardPeRatio,MarketCap,PbRatio,PeRatio,PsRatio):
        self.activo=activo
        self.asOfDate=asOfDate

        self.EnterprisesValueEBITDARatio =EnterprisesValueEBITDARatio
        self.EnterprisesValueRevenueRatio=EnterprisesValueRevenueRatio
        self.ForwardPeRatio = ForwardPeRatio
        self.MarketCap = MarketCap
        self.PbRatio = PbRatio
        self.PeRatio = PeRatio
        self.PegRatio = PsRatio
    
        
# Símbolo de NVDA (NVIDIA Corporation) en Yahoo Finance
aapl = Ticker('aapl')

# Obtener información detallada de NVDA


#print(type( aapl.cash_flow(trailing=False)))
json_valuation_measures = aapl.valuation_measures.to_json(orient='records')
json_cash = aapl.cash_flow(trailing=False).to_json(orient='records')
#print(json_cash)


print(json_valuation_measures)
"""
print("----------------------")
print(json_cash)

Voy a analizarlo por separado no mergear 
"""
data=json.loads(json_valuation_measures)
data2=json.loads(json_cash)
def unix_to_dmy(unix_time):
    dt = datetime.fromtimestamp(unix_time / 1000)  # Dividir por 1000 para obtener segundos en lugar de milisegundos
    return dt.strftime("%d/%m/%Y")  # Formato "dmy"

# Acceder a los valores en los diccionarios y convertir la fecha
for item in data:
    as_of_date_unix = item['asOfDate']
    as_of_date_dmy = unix_to_dmy(as_of_date_unix)
   
    print("As Of Date (Unix):", as_of_date_unix)
    print("As Of Date (dmy):", as_of_date_dmy)
    print("Period Type:", item['periodType'])
    print("Enterprise Value:", item['EnterpriseValue'])
    print("PE Ratio:", item['PeRatio'])
    # Agreg
for item in data2:
    as_of_date_unix = item['asOfDate']
    as_of_date_dmy = unix_to_dmy(as_of_date_unix)
   
    print("As Of Date (Unix):", as_of_date_unix)
    print("As Of Date (dmy):", as_of_date_dmy)

    # Agreg
       
"""
# Market Cap (Capitalización de Mercado)
market_cap = nvda_info['quotes'][0]['marketCap']

# Cash - Debt (Efectivo - Deuda)
cash = nvda_info['financials']['cash']
debt = nvda_info['financials']['longTermDebt']
cash_debt = cash - debt

# Revenue (Ingresos)
revenue = nvda_info['financials']['revenue']

# Net Income (Ingresos Netos)
net_income = nvda_info['financials']['netIncome']

# FCB (Free Cash Flow Before Dividends Paid)
fcb = nvda_info['cashflow']['freeCashflow']

# SBC (Stock-Based Compensation)
sbc = nvda_info['financials']['stockBasedCompensation']

# Enterprise Value (Valor de la Empresa)
# Para calcular el EV, necesitarías datos adicionales, como el valor de mercado de acciones preferentes y otros elementos de valor.
# EV = Market Cap + Deuda Neta + Valor de Mercado de Acciones Preferentes + Intereses Minoritarios - Efectivo y Equivalentes de Efectivo

# Imprimir los valores
print("Market Cap:", market_cap)
print("Cash - Debt:", cash_debt)
print("Revenue:", revenue)
print("Net Income:", net_income)
print("FCB:", fcb)
print("SBC:", sbc)
"""