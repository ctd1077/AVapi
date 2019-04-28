#!/usr/bin/python3
#Alpha Vatange API APP

import requests
import numpy as np
import pandas as pd
import json as js
import matplotlib.pyplot as plt

def fetch_symbol(stock):
    return requests.get(api_root + api_series + stock + api, stream=False).json()

def company_symbol():
    try:
        stc = ''
        while not stc:
            stc = input("What stock would you like to view? ")
        stock = fetch_symbol(stc)
        if len(stc) == 0:
            print("Please enter a symbol.")
        #elif len(stc).isdigit() == True:
            #print ("It Works")
        #elif stock != '"Meta Data"':
            #print('elif statment')
            # Takes to long. Waits for JSON file and doesn't ask
            # to enter in another stock fetch_symbol
            # qyuicker way to tell not a stock symbol?
    except requests.exceptions.ConnectionError:
        print("Couldn't connect to server! Please check the network?")
    return stock

def series():
    """This function promts the user for the desired
    time series. Day, week, month, etc"""
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
            print(t_type)
            continue
    return t_type

def time_series(t_series):
    """The time_series function takes the selected time series and return
    the correct format for the url to retrive the symbol time series"""
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

def date_price_df(fhand, t_series):
    """The date_price_df function takes the file handle and creates a simple
    data frame made up of the date and price"""
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
    return lst

def createDframe(fhand):
    """This function finds the date and price for the selected stock
    and creates and returns the dataframe"""
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
    df = pd.DataFrame(lst,columns=['Date','Price'])
    return df

def createDframe2(fhand):
    """This function finds the date and volume for the selected stock
    and creates and returns the dataframe"""
    lst = []
    for key, values in fhand.items():
        if key == t_series:
            for date, sinfo in values.items():
                #Finds the date and values for stock
                for cols, vol in sinfo.items():
                    #finds the volume
                    if cols == '5. volume':
                        #create list for date and volume key values
                        lst.append([date,vol])


    df = pd.DataFrame(lst,columns=['Date','Volume'])
    return df

if __name__ == '__main__':
    t_series = series()
    api_root = 'https://www.alphavantage.co'
    api_series = time_series(t_series)
    api = #'API KEY GOES HERE'
    fhand = company_symbol()
    # Debug Print and test df
    print(createDframe2(fhand))
