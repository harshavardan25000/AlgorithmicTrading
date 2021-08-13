import numpy as np
import pandas as pd
from secrets import get_secret
import requests
stocks=pd.read_csv("/Users/harshavardanmanam/Desktop/projects/AlgorithmicTrading/data/sp_500_stocks.csv")
symbol='AAPL'
token=get_secret()
api_url='https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={token}'.format(symbol=symbol,token=token)

data=requests.get(api_url).json()

print(data)
price=data['latestPrice']
market_cap=data['marketCap']
print(price,market_cap)