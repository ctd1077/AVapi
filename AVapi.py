#!/usr/bin/python3
#Alpha Vatange API APP
#Enter in stock symbol
import plotly.plotly as py
import plotly.figure_factory as ff
import pandas as pd
import requests
import json as js
import matplotlib.pyplot as plt

def fetch_symbol():
    stock = ''
    while not stock:
        stock = input("What stock would you like to view? ")
    return requests.get(api_root + api_series + stock + api).json()

def series():
    """this function promts the user for the desired time series. Day, week, month, etc"""
    while True:
        t_type = input('Please enter time series you would like to see. ' \
                  'Daily[1], Weekly[2], Monthly[3]: ')
        if t_type == '1':
            t_type = 'Time Series (Daily)'
            return t_type
        elif t_type == '2':
            t_type = 'Weekly Time Series'
            return t_type
        elif t_type == '3':
            t_type = 'Monthly Time Series'
            return t_type
        else:
            print('Error')
            continue
    return t_type

def time_series(t_series):
    """this"""
    if t_series == 'Time Series (Daily)':
        api_series = '/query?function=TIME_SERIES_DAILY&symbol='
        return api_series
    elif t_series == 'Weekly Time Series':
        api_series = '/query?function=TIME_SERIES_WEEKLY&symbol='
        return api_series
    elif t_series == 'Monthly Time Series':
        api_series = '/query?function=TIME_SERIES_MONTHLY&symbol='
        return api_series
    else:
        print('Error') #DeBug
        print(t_series) #DeBug

def company_symbol():
    try:
        #stock = ''
        #while not stock:
            #stock = input("What stock would you like to view? ")
        stock = fetch_symbol(stock)
        if len(stock) == 0:
            print("Please enter a symbol.")
        elif (stock) == 'Error Message':
            print('else statment')
    except requests.exceptions.ConnectionError:
        print("Couldn't connect to server! Please check the network?")
    return stock

t_series = series()
api_root = 'https://www.alphavantage.co'
api_series = time_series(t_series)
api = 'Enter API code here'
fhand = fetch_symbol()
#print(fhand)
#print(fhand[t_series]) #DeBug
#print(t_series)

lst = []

for key, values in fhand.items():
    if key == t_series:
        for date, sinfo in values.items():
            #Finds the date and values for stock
            for cols, nums in sinfo.items():
                #finds the closing price
                if cols == '4. close':
                    #create list for date and price key values
                    lst.append([date,nums])

#create series from list
ds = pd.Series(lst)
#create dataframe from list
df = pd.DataFrame(lst,columns=['Date','Price'])
#print(ds)
print(df)

plt.plot(df)
plt.show()
