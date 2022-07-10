from __future__ import annotations
from pydantic import BaseModel
import requests
import json
from pprint import pprint


API_KEY = "xxo4ENCqcP1JnhvEt4JNs7a91JqIVXp440MNxPxj"




import requests

class StockData():
    
    def __init__(self, symbol: str, api_key: str) -> None:
        self.symbol = symbol
        self.api_key = api_key
        self.url = "https://yfapi.net/v6/finance/quote"
        self.response = self._get_response()
        self.data = self._get_data()
        self.deserialized_data = self._deserialize_data()
        self.result = self.deserialized_data['quoteResponse']["result"][0]
        
        
    def _get_response(self) -> requests.Response:
        querystring = {"symbols": self.symbol}
        headers = {'x-api-key': self.api_key}
        response = requests.request("GET", self.url, headers=headers, params=querystring)
        return response
    
    def _get_data(self) -> dict:
        data = self.response.text
        return data
    
    
    def _deserialize_data(self) -> dict:
        # convert from json to python dict
        deserialized = json.loads(self.data)
        return deserialized
    
    def decode_stock_type(self) -> str:
        # figure Crypto Stock or somthing else
        return self.result['type']
    
    


    
    



class StockQuote(BaseModel):
    """Summary
    
    real time quote data for stocks, ETFs, mutuals funds, bonds, crypto and national currencies.
    """
    ask: float
    askSize: int
    averageDailyVolume10Day: int
    averageDailyVolume3Month: int
    bid: float
    bidSize: int
    bookValue: float
    currency: str
    displayName: str
    dividendDate: int
    earningsTimestamp: int
    earningsTimestampEnd: int
    earningsTimestampStart: int
    epsCurrentYear: float
    epsForward: float
    epsTrailingTwelveMonths: float
    esgPopulated: bool
    exchange: str
    exchangeDataDelayedBy: int
    exchangeTimezoneName: str
    exchangeTimezoneShortName: str
    fiftyDayAverage: float
    fiftyDayAverageChange: float
    fiftyDayAverageChangePercent: float
    fiftyTwoWeekHigh: float
    fiftyTwoWeekHighChange: float
    fiftyTwoWeekHighChangePercent: float
    fiftyTwoWeekLow: float
    fiftyTwoWeekLowChange: float
    fiftyTwoWeekLowChangePercent: float
    fiftyTwoWeekRange: str
    financialCurrency: str
    firstTradeDateMilliseconds: int
    forwardPE: float
    fullExchangeName: str
    gmtOffSetMilliseconds: int
    language: str
    longName: str
    market: str
    marketCap: int
    marketState: str
    messageBoardId: str
    postMarketChange: float
    postMarketChangePercent: float
    postMarketPrice: float
    postMarketTime: int
    priceEpsCurrentYear: float
    priceHint: int
    priceToBook: float
    quoteSourceName: str
    quoteType: str
    region: str
    regularMarketChange: float
    regularMarketChangePercent: float
    regularMarketDayHigh: float
    regularMarketDayLow: float
    regularMarketDayRange: str
    regularMarketOpen: float
    regularMarketPreviousClose: float
    regularMarketPrice: float
    regularMarketTime: int
    regularMarketVolume: int
    sharesOutstanding: int
    shortName: str
    sourceInterval: int
    symbol: str
    tradeable: bool
    trailingAnnualDividendRate: float
    trailingAnnualDividendYield: float
    trailingPE: float
    triggerable: bool
    twoHundredDayAverage: float
    twoHundredDayAverageChange: float
    twoHundredDayAverageChangePercent: float









test = StockData("UPST", API_KEY)
stock_data = test.result

data = StockQuote(**stock_data)
print(data.region)

