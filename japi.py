#Project 5 IFT 458
#Python Stock Price Requestor w/ AlphaVantage API

import urllib.request
import json

def getStockData(symbol):
    key = '3I7I7IQVF8KZ1339'
    url = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols='+symbol+'&apikey='+key
    connection = urllib.request.urlopen(url)
    response = connection.read().decode()
    print(response)
    dict = json.loads(response)
    print("The current price of {} is: ${}".format(symbol, dict["Stock Quotes"][0]["2. price"]))
    print()

if __name__ == "__main__":
    while True:
        stockSymbol = input("Enter Stock Ticker (enter q to exit): ")
        if stockSymbol != 'q':
             getStockData(stockSymbol)
        else:
            break