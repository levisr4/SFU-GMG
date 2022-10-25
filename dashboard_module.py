# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:42:39 2022

@author: Hans
"""
import fredapi as fa
import pandas as pd
import plotly as py
import plotly.express as px
import plotly.io as pio 
import numpy as np

fred = fa.Fred(api_key='fdba3cdea3e53d5321ecd4f3d07ae939')

def grab_fred_data(fred_id, title):
    x = pd.DataFrame(fred.get_series(fred_id))
    fig = px.line(x, x=x.index, y=0, title=title)
    return fig, x

def dash(data, column):
    latest_date = data.index[-1].date()
    latest_data = np.int(data[column].tail(1))
    
    weekly_series = data[column].tail(780).diff(periods=5).fillna(method='bfill').fillna(method='ffill')
    monthly_series = data[column].tail(780).diff(periods=20).fillna(method='bfill').fillna(method='ffill')
    quarterly_series = data[column].tail(780).diff(periods=60).fillna(method='bfill').fillna(method='ffill')
    
    daily_change = latest_data - (data[column].iloc[-2])
    weekly_change = latest_data - (data[column].iloc[-6])
    monthly_change = latest_data - (data[column].iloc[-21])
    quarterly_change = latest_data - (data[column].iloc[-61])
    
    weekly_zscore = (weekly_change - weekly_series.mean())/weekly_series.std()
    monthly_zscore = (monthly_change - monthly_series.mean())/monthly_series.std()
    quarterly_zscore = (quarterly_change - quarterly_series.mean())/quarterly_series.std()
    series = [latest_date, latest_data, daily_change, weekly_change, weekly_zscore, monthly_change, monthly_zscore, quarterly_change, quarterly_zscore]
    return series