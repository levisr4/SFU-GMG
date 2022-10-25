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
canada_1_yr = vi.get_series_observations("TB.CDN.1Y.MID", response_format='csv')[1]
canada_two_yr = vi.get_series_observations("BD.CDN.2YR.DQ.YLD", response_format='csv')[1]
canada_five_yr = vi.get_series_observations("BD.CDN.5YR.DQ.YLD", response_format='csv')[1]
canada_ten_yr = vi.get_series_observations("BD.CDN.10YR.DQ.YLD", response_format='csv')[1]
canada_thirty_yr = vi.get_series_observations("BD.CDN.LONG.DQ.YLD", response_format='csv')[1]


"""Inflation Tracker"""
canada_inflation_ten_yr = vi.get_series_observations("STATIC_ATABLE_V122544_V122553", response_format='csv')[1]


"""EUROPE, MIDDLE EAST, AND AFRICA"""
"""Fixed Income Rates"""
emea_two_yr = pd.DataFrame(QueryECB_YC("B.U2.EUR.4F.G_N_A.SV_C_YM.SR_2Y").items())
emea_five_yr = pd.DataFrame(QueryECB_YC("B.U2.EUR.4F.G_N_A.SV_C_YM.SR_5Y").items())
emea_ten_yr = pd.DataFrame(QueryECB_YC("B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y").items())
emea_thirty_yr = pd.DataFrame(QueryECB_YC("B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y").items())

ester_six_mo = pd.DataFrame(QueryECB_ESTR("B.EU000A2QQF40.CR").items())
ester_twelve_mo = pd.DataFrame(QueryECB_ESTR("B.EU000A2QQF57.CR").items())

"""Inflation Tracker"""
#I couldn't find it - Hans

"""JAPAN"""
"""Fixed Income Rates"""
japan_ten_yr = pd.DataFrame(QueryECB("FM", "M.JP.JPY.RT.BZ.JPY10YZ_R.YLDE").items())

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

dashboard_df = pd.DataFrame(columns = ['latest_date', 'latest_data', 'daily_change', 'weekly_change', 'weekly_zscore', 'monthly_change', 'monthly_zscore', 'quarterly_change', 'quarterly_zscore'])

dashboard_df.loc['US04M'] = md.dash(us_threem_data, 0)

dashboard_df.to_excel('C:/Users/Hans/Desktop/test_repo/dashboard_df.xlsx')
