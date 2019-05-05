#!/usr/bin/python3
#Alpha Vantage API APP

import requests
import numpy as np
import pandas as pd
import json as js
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def fetch_symbol(stock):
    return requests.get(api_root + api_series + stock + api, stream=False).json()

def company_symbol():
    try:
        stc = ''
        while not stc:
            stc = input("What stock would you like to view? ")
            print('Please wait while we process your request...')
        stock = fetch_symbol(stc)
        if len(stc) == 0:
            print("Please enter a symbol.")
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
    #try except block here
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
        print('Error')

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
    df = df.set_index('Date')
    df.sort_index(inplace=True)
    return df

def createDframe2(fhand):
    """This function finds the date and volume for the selected stock
    and creates and returns the dataframe"""
    lst = []
    for key, values in fhand.items():
        if key == t_series:
            for date, sinfo in values.items():
                # Finds the date and values for stock
                for cols, vol in sinfo.items():
                    # finds the volume
                    if cols == '5. volume':
                        # create list for date and volume key values
                        lst.append([date, vol])

    df = pd.DataFrame(lst, columns=['Date', 'Volume'])
    df = df.set_index('Date')
    df.sort_index(inplace=True)
    return df

def chart():

    df = createDframe(fhand)
    df = df['Price'].astype(float)
    plt.style.use('seaborn-whitegrid')
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.xaxis.set_major_locator(MaxNLocator(nbins=12))
    ax.plot(df)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Price Chart')
    return plt.show()

def chart2():

    df = createDframe2(fhand)
    df = df['Volume'].astype(float)
    plt.style.use('seaborn-whitegrid')
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.xaxis.set_major_locator(MaxNLocator(nbins=12))
    ax.plot(df)
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.title('Volume Chart')
    return plt.show()


if __name__ == '__main__':
    t_series = series()
    api_root = 'https://www.alphavantage.co'
    api_series = time_series(t_series)
    api = #'API KEY GOES HERE'
    fhand = company_symbol()

    while True:
        ans = input('Which chart would you like to see? \nPress 1 for Price and 2 for Volume or 3 to quit: ')
        if ans == '1':
            chart()
            continue
        elif ans == '2':
            chart2()
            continue
        elif ans == '3':
            print('Have a good day!')
            break
        else:
            print('Please check your response and try again.')
            continue
