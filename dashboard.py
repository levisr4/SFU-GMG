# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 15:47:19 2022

@author: Hans
"""

""" Data Sources """
import fredapi as fa #US Federal Reserve
fred = fa.Fred(api_key='fdba3cdea3e53d5321ecd4f3d07ae939')

import yfinance as yf #General Market Data
from pyvalet import ValetInterpreter #Bank of Canada
import pandasdmx as sdmx
import requests
import numpy as np


from urllib.request import urlopen
from xmltodict import parse

"""Data Manipulation"""
import pandas as pd
import datetime
from scipy import stats

def QueryECB_YC(series): #For European Central Bank
    with urlopen("https://sdw-wsrest.ecb.europa.eu/service/data/YC/" + series) as url:
         raw = parse(url.read().decode('utf8'))
    data = raw['message:GenericData']['message:DataSet']['generic:Series']['generic:Obs']
    res = {x['generic:ObsDimension']['@value']: 
           float(x['generic:ObsValue']['@value'])
           for x in data}
    return res

def QueryECB_ESTR(series):
    with urlopen("https://sdw-wsrest.ecb.europa.eu/service/data/EST/" + series) as url:
         raw = parse(url.read().decode('utf8'))
    data = raw['message:GenericData']['message:DataSet']['generic:Series']['generic:Obs']
    res = {x['generic:ObsDimension']['@value']: 
           float(x['generic:ObsValue']['@value'])
           for x in data}
    return res

def QueryECB(database, series):
    with urlopen("https://sdw-wsrest.ecb.europa.eu/service/data/" + database + "/" + series) as url:
         raw = parse(url.read().decode('utf8'))
    data = raw['message:GenericData']['message:DataSet']['generic:Series']['generic:Obs']
    res = {x['generic:ObsDimension']['@value']: 
           float(x['generic:ObsValue']['@value'])
           for x in data}
    return res

"""Custom Modules"""
import dashboard_module as md

"""-------------------------------------------Rates--------------------------------------------------"""

"""UNITED STATES"""
"""Fixed Income Rates"""
us_treasury_three_months, us_threem_data = md.grab_fred_data('dtb3', 'US Treasury 3M')
us_treasury_six_months, us_sixm_data = md.grab_fred_data('dtb6', 'US Treasury 6M')
us_treasury_one, us_one_data = md.grab_fred_data('DTB1YR', 'US Treasury 1Y')
us_treasury_two, us_two_data = md.grab_fred_data('dgs2', 'US Treasury 2Y')
us_treasury_five, us_five_data = md.grab_fred_data('dgs5', 'US Treasury 5Y')
us_treasury_ten, us_ten_data = md.grab_fred_data('dgs10', 'US Treasury 10Y')
us_treasury_thirty, us_thirty_data = md.grab_fred_data('dgs30', 'US Treasury 30Y')
"""Inflation Rates"""
us_ten_be, us_ten_be_data = md.grab_fred_data('T10YIE', 'US 10Y Breakeven Inflation Rate') #TIPS, basically
us_five_five_be, us_five_five_be_data = md.grab_fred_data('T5YIFR', 'US 5Y, 5Y Forward Inflation Rate') #This series is a measure of expected inflation (on average) over the five-year period that begins five years from today.

"""Volatility tracker"""
move_index = yf.Ticker('^move').history(period='max')


"""CANADA"""
"""Fixed Income Rates"""
vi = ValetInterpreter()
canada_sixm_yr = vi.get_series_observations("TB.CDN.180D.MID", response_format='csv')[1]
canada_sixm_yr['label'] = pd.to_numeric(canada_sixm_yr['label'])
canada_sixm_yr['id'] = pd.to_datetime(canada_sixm_yr['id'])
canada_sixm_yr = canada_sixm_yr.set_index('id')

canada_1_yr = vi.get_series_observations("TB.CDN.1Y.MID", response_format='csv')[1]
canada_1_yr['label'] = pd.to_numeric(canada_1_yr['label'])
canada_1_yr['id'] = pd.to_datetime(canada_1_yr['id'])
canada_1_yr = canada_1_yr.set_index('id')

canada_two_yr = vi.get_series_observations("BD.CDN.2YR.DQ.YLD", response_format='csv')[1]
canada_two_yr['label'] = pd.to_numeric(canada_two_yr['label'])
canada_two_yr['id'] = pd.to_datetime(canada_two_yr['id'])
canada_two_yr = canada_two_yr.set_index('id')

canada_five_yr = vi.get_series_observations("BD.CDN.5YR.DQ.YLD", response_format='csv')[1]
canada_five_yr['label'] = pd.to_numeric(canada_five_yr['label'])
canada_five_yr['id'] = pd.to_datetime(canada_five_yr['id'])
canada_five_yr = canada_five_yr.set_index('id')

canada_ten_yr = vi.get_series_observations("BD.CDN.10YR.DQ.YLD", response_format='csv')[1]
canada_ten_yr['label'] = pd.to_numeric(canada_ten_yr['label'])
canada_ten_yr['id'] = pd.to_datetime(canada_ten_yr['id'])
canada_ten_yr = canada_ten_yr.set_index('id')

canada_thirty_yr = vi.get_series_observations("BD.CDN.LONG.DQ.YLD", response_format='csv')[1]
canada_thirty_yr['label'] = pd.to_numeric(canada_thirty_yr['label'])
canada_thirty_yr['id'] = pd.to_datetime(canada_thirty_yr['id'])
canada_thirty_yr = canada_thirty_yr.set_index('id')
 

"""Inflation Tracker"""
canada_inflation_ten_yr = vi.get_series_observations("STATIC_ATABLE_V122544_V122553", response_format='csv')[1]
canada_inflation_ten_yr['label'] = pd.to_numeric(canada_inflation_ten_yr['label'])
canada_inflation_ten_yr['id'] = pd.to_datetime(canada_inflation_ten_yr['id'])
canada_inflation_ten_yr = canada_inflation_ten_yr.set_index('id')

"""EUROPE, MIDDLE EAST, AND AFRICA"""
"""Fixed Income Rates"""
emea_two_yr = pd.DataFrame(QueryECB_YC("B.U2.EUR.4F.G_N_A.SV_C_YM.SR_2Y").items())
emea_two_yr[1] = pd.to_numeric(emea_two_yr[1])
emea_two_yr[0] = pd.to_datetime(emea_two_yr[0])
emea_two_yr = emea_two_yr.set_index(0)

emea_five_yr = pd.DataFrame(QueryECB_YC("B.U2.EUR.4F.G_N_A.SV_C_YM.SR_5Y").items())
emea_five_yr[1] = pd.to_numeric(emea_five_yr[1])
emea_five_yr[0] = pd.to_datetime(emea_five_yr[0])
emea_five_yr = emea_five_yr.set_index(0)

emea_ten_yr = pd.DataFrame(QueryECB_YC("B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y").items())
emea_ten_yr[1] = pd.to_numeric(emea_ten_yr[1])
emea_ten_yr[0] = pd.to_datetime(emea_ten_yr[0])
emea_ten_yr = emea_ten_yr.set_index(0)

emea_thirty_yr = pd.DataFrame(QueryECB_YC("B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y").items())
emea_thirty_yr[1] = pd.to_numeric(emea_thirty_yr[1])
emea_thirty_yr[0] = pd.to_datetime(emea_thirty_yr[0])
emea_thirty_yr = emea_thirty_yr.set_index(0)

ester_six_mo = pd.DataFrame(QueryECB_ESTR("B.EU000A2QQF40.CR").items())
ester_six_mo[1] = pd.to_numeric(ester_six_mo[1])
ester_six_mo[0] = pd.to_datetime(ester_six_mo[0])
ester_six_mo = ester_six_mo.set_index(0)

ester_twelve_mo = pd.DataFrame(QueryECB_ESTR("B.EU000A2QQF57.CR").items())
ester_twelve_mo[1] = pd.to_numeric(ester_twelve_mo[1])
ester_twelve_mo[0] = pd.to_datetime(ester_twelve_mo[0])
ester_twelve_mo = ester_twelve_mo.set_index(0)


"""Inflation Tracker"""
#I couldn't find it - Hans

"""JAPAN"""
"""Fixed Income Rates"""
japan_ten_yr = pd.DataFrame(QueryECB("FM", "M.JP.JPY.RT.BZ.JPY10YZ_R.YLDE").items())
japan_ten_yr[1] = pd.to_numeric(japan_ten_yr[1])
japan_ten_yr[0] = pd.to_datetime(japan_ten_yr[0])
japan_ten_yr = japan_ten_yr.set_index(0)

"""Bond Futures"""
#I couldn't find it - Hans
"""Inflation Tracker"""
#I coudln't find it - Hans

"""---------------------------------------------Credit------------------------------------------------"""
"""USA"""
usa_hy_oas = pd.DataFrame(fred.get_series("BAMLH0A0HYM2"))
usa_ig_oas = pd.DataFrame(fred.get_series("BAMLC0A0CM"))
# I couldn't find datasource for CDX IG and HY

"""Europe, Middle East, and Africa (EMEA)"""
euro_hy_oas = pd.DataFrame(fred.get_series("BAMLHE00EHYIOAS"))
emea_ig_oas = pd.DataFrame(fred.get_series("BAMLEMELLCRPIEMEAUSOAS"))
itraxx_cross_swap = yf.Ticker('DBXM.DE').history(period='max')


""" Commodities """

""" Gold """
gol = yf.Ticker("GC=F")
gol.info
gol_hist = gol.history(period="max")

""" Crude Oil """
cl = yf.Ticker("CL=F")
cl.info
cl_hist = cl.history(period="max")



""" Foreign Exchange """
""" Developed Markets """

""" CAD """
cad = yf.Ticker("CAD=X")
cad.info
cad_hist = cad.history(period="max")

""" EUR """
eur = yf.Ticker("EUR=X")
eur.info
eur_hist = eur.history(period="max")

""" JPY """
jpy = yf.Ticker("JPY=X")
jpy.info
jpy_hist = jpy.history(period="max")

""" GBP """
gbp = yf.Ticker("GBP=X")
gbp.info
gbp_hist = gbp.history(period="max")

""" CHF """
chf = yf.Ticker("CHF=X")
chf.info
chf_hist = chf.history(period="max")

""" AUD """
aud = yf.Ticker("AUD=X")
aud.info
aud_hist = aud.history(period="max")

""" SEK """
sek = yf.Ticker("SEK=X")
sek.info
sek_hist = sek.history(period="max")


""" Emerging Market """

""" CNY """
cny = yf.Ticker("CNY=X")
cny.info
cny_hist = cny.history(period="max")

""" KRW """
krw = yf.Ticker("KRW=X")
krw.info
krw_hist = krw.history(period="max")

""" INR """
inr = yf.Ticker("INR=X")
inr.info
inr_hist = inr.history(period="max")

""" BRL """
brl = yf.Ticker("BRL=X")
brl.info
brl_hist = brl.history(period="max")

""" CLP """
clp = yf.Ticker("CLP=X")
clp.info
clp_hist = clp.history(period="max")

""" RUB """
rub = yf.Ticker("RUB=X")
rub.info
rub_hist = rub.history(period="max")

""" TRY """
tryl= yf.Ticker("TRY=X")
tryl.info
try_hist = tryl.history(period="max")


""" Equity """
""" USA """

""" S&P 500 """
sp = yf.Ticker("ES=F")
sp.info
sp_hist = sp.history(period="max")

""" Nasdaq """
nas = yf.Ticker("NQ=F")
nas.info
nas_hist = nas.history(period="max")

""" Russel 2000 """
rus = yf.Ticker("RTY=F")
rus.info
rus_hist = rus.history(period="max")


dashboard_df = pd.DataFrame(columns = ['latest_date', 'latest_data', 'daily_change', 'weekly_change', 'weekly_zscore', 'monthly_change', 'monthly_zscore', 'quarterly_change', 'quarterly_zscore'])

dashboard_df.loc['US03M'] = md.dash(us_threem_data, 0)
dashboard_df.loc['US06M'] = md.dash(us_sixm_data, 0)
dashboard_df.loc['US01Y'] = md.dash(us_one_data, 0)
dashboard_df.loc['US02Y'] = md.dash(us_two_data, 0)
dashboard_df.loc['US05Y'] = md.dash(us_five_data, 0)
dashboard_df.loc['US10Y'] = md.dash(us_ten_data, 0)
dashboard_df.loc['US30Y'] = md.dash(us_thirty_data, 0)
dashboard_df.loc['US10YBE'] = md.dash(us_ten_be_data, 0)
dashboard_df.loc['US5YFI'] = md.dash(us_five_five_be_data, 0)

dashboard_df.loc['CAD06M'] = md.dash(canada_sixm_yr, 'label')
dashboard_df.loc['CAD01Y'] = md.dash(canada_1_yr, 'label')
dashboard_df.loc['CAD02Y'] = md.dash(canada_two_yr, 'label')
dashboard_df.loc['CAD05Y'] = md.dash(canada_five_yr, 'label')
dashboard_df.loc['CAD10Y'] = md.dash(canada_ten_yr, 'label')
dashboard_df.loc['CAD30Y'] = md.dash(canada_thirty_yr, 'label')
dashboard_df.loc['CADI10Y'] = md.dash(canada_inflation_ten_yr, 'label')

dashboard_df.loc['EM02Y'] = md.dash(emea_two_yr, 1)
dashboard_df.loc['EM05Y'] = md.dash(emea_five_yr, 1)
dashboard_df.loc['EM10Y'] = md.dash(emea_ten_yr, 1)
dashboard_df.loc['EM30Y'] = md.dash(emea_thirty_yr, 1)

dashboard_df.loc['ES06M'] = md.dash(ester_six_mo, 1)
dashboard_df.loc['ES12M'] = md.dash(ester_twelve_mo, 1)

dashboard_df.loc['JPN10Y'] = md.dash(japan_ten_yr, 1)

dashboard_df.loc['USHY'] = md.dash(usa_hy_oas, 0)
dashboard_df.loc['USIG'] = md.dash(usa_ig_oas, 0)
dashboard_df.loc['EUHY'] = md.dash(euro_hy_oas, 0)
dashboard_df.loc['EMIG'] = md.dash(emea_ig_oas, 0)

dashboard_df.loc['GOLD'] = md.dash(gol_hist, 'Close')
dashboard_df.loc['OIL'] = md.dash(cl_hist, 'Close')

dashboard_df.loc['CAD'] = md.dash(cad_hist, 'Close')
dashboard_df.loc['EUR'] = md.dash(eur_hist, 'Close')
dashboard_df.loc['JPY'] = md.dash(jpy_hist, 'Close')
dashboard_df.loc['GBP'] = md.dash(gbp_hist, 'Close')
dashboard_df.loc['CHF'] = md.dash(chf_hist, 'Close')
dashboard_df.loc['AUD'] = md.dash(aud_hist, 'Close')
dashboard_df.loc['SEK'] = md.dash(sek_hist, 'Close')

dashboard_df.loc['CNY'] = md.dash(cny_hist, 'Close')
dashboard_df.loc['KRW'] = md.dash(krw_hist, 'Close')
dashboard_df.loc['INR'] = md.dash(inr_hist, 'Close')
dashboard_df.loc['BRL'] = md.dash(brl_hist, 'Close')
dashboard_df.loc['CLP'] = md.dash(clp_hist, 'Close')
dashboard_df.loc['RUB'] = md.dash(rub_hist, 'Close')
dashboard_df.loc['TRY'] = md.dash(try_hist, 'Close')

dashboard_df.loc['S&P'] = md.dash(sp_hist, 'Close')
dashboard_df.loc['NAS'] = md.dash(nas_hist, 'Close')
dashboard_df.loc['RUS'] = md.dash(rus_hist, 'Close')

dashboard_df.to_excel(r'C:\Users\Hans\Desktop\SFUGMG\SFU-GMG/dashboard_df.xlsx')
