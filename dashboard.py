#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 15:34:18 2022

@author: patriciaregina
"""

""" Data Sources """
import investpy as inv
import yfinance as yf

""" Data Manipulation """
import pandas as pd
import numpy as np





""" Commodities """

""" Gold """

gol = yf.Ticker("GC=F")

# get stock info
gol.info

# get historical market data
gol_hist = gol.history(period="max")


""" Crude Oil """

cl = yf.Ticker("CL=F")

# get stock info
cl.info

# get historical market data
cl_hist = cl.history(period="max")






""" Foreign Exchange """
""" Developed Markets """

""" CAD """
cad = yf.Ticker("CAD=X")

# get stock info
cad.info

# get historical market data
cad_hist = cad.history(period="max")


""" EUR """
eur = yf.Ticker("EUR=X")

# get stock info
eur.info

# get historical market data
eur_hist = eur.history(period="max")


""" JPY """
jpy = yf.Ticker("JPY=X")

# get stock info
jpy.info

# get historical market data
jpy_hist = jpy.history(period="max")


""" GBP """
gbp = yf.Ticker("GBP=X")

# get stock info
gbp.info

# get historical market data
gbp_hist = gbp.history(period="max")


""" CHF """
chf = yf.Ticker("CHF=X")

# get stock info
chf.info

# get historical market data
chf_hist = chf.history(period="max")


""" AUD """
aud = yf.Ticker("AUD=X")

# get stock info
aud.info

# get historical market data
aud_hist = aud.history(period="max")


""" SEK """
sek = yf.Ticker("SEK=X")

# get stock info
sek.info

# get historical market data
sek_hist = sek.history(period="max")



""" Emerging Market """

""" CNY """
cny = yf.Ticker("CNY=X")

# get stock info
cny.info

# get historical market data
cny_hist = cny.history(period="max")


""" KRW """
krw = yf.Ticker("KRW=X")

# get stock info
krw.info

# get historical market data
krw_hist = krw.history(period="max")


""" INR """
inr = yf.Ticker("INR=X")

# get stock info
inr.info

# get historical market data
inr_hist = inr.history(period="max")


""" BRL """
brl = yf.Ticker("BRL=X")

# get stock info
brl.info

# get historical market data
brl_hist = brl.history(period="max")


""" CLP """
clp = yf.Ticker("CLP=X")

# get stock info
clp.info

# get historical market data
clp_hist = clp.history(period="max")


""" RUB """
rub = yf.Ticker("RUB=X")

# get stock info
rub.info

# get historical market data
rub_hist = rub.history(period="max")


""" TRY """
tryl= yf.Ticker("TRY=X")

# get stock info
tryl.info

# get historical market data
try_hist = tryl.history(period="max")






""" Equity """
""" USA """

""" S&P 500 """
sp = yf.Ticker("ES=F")

# get stock info
sp.info

# get historical market data
sp_hist = sp.history(period="max")


""" Nasdaq """
nas = yf.Ticker("NQ=F")

# get stock info
nas.info

# get historical market data
nas_hist = nas.history(period="max")


""" Russel 2000 """
rus = yf.Ticker("RTY=F")

# get stock info
rus.info

# get historical market data
rus_hist = rus.history(period="max")


""" VIX """





""" Europe """


""" Euro Stoxx 50 """
stoxx50 = yf.Ticker("^STOXX50E")

# get stock info
stoxx50.info

# get historical market data
stoxx50_hist = stoxx50.history(period="max")


""" Euro Stoxx Banks """



""" Other DM """

""" Nikkei """
nik = yf.Ticker("^N225")

# get stock info
nik.info

# get historical market data
nik_hist = nik.history(period="max")


""" TSX """


""" FTSE 100 """
ftse = yf.Ticker("^FTSE")

# get stock info
ftse.info

# get historical market data
ftse_hist = ftse.history(period="max")


""" ASX 200 """




""" Emerging Markets """

""" CSI 300 """

""" Brazil """

""" Kospi """








