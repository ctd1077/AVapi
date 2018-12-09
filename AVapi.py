#!/usr/bin/python3
#Alpha Vatange API APP
#Enter in stock symbol
import urllib.request, urllib.parse, urllib.error
import requests
import json
import datetime

api_root = 'https://www.alphavantage.co'
api_location = '/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='
api = ''#Your Alpha Vantage key goes here
api_symbol = 'AMD'
#replace with (input('Please enter stock symbol:')) when complete

def fetch_location(query):
    return requests.get(api_root + api_location + query).json()
def fetch_symbol(symbol):
    return requests.get(api_root + api_symbol + symbol).json()

data = requests.get(api_root + api_location + api_symbol + api).json()

info = data['Meta Data']

for k, v in info.items():
    #split the key value to lose #
    new = k.split()
    print(new[1],':', v)



#varible time set to today's date
time = datetime.date.today()
#variable info set to time series and today's date as str
info2 = data['Time Series (Daily)'][str(time)]

#debug time
#print(time)

#loop through info var in key value pairs
for k, v in info2.items():
    #split the key value to lose #
    new2 = k.split()
    print(new2[1],':', '{:>10}'.format(v), '\n')
