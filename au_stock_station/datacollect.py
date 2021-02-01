import pandas as pd
from pandas_datareader import data as wb
from tqdm import tqdm
import yfinance as yf

class Info():

    def __init__(self,ticker):
        self.ticker = ticker
        self.Ticker = self.ticker+'.T' 

    def get_price(self,start,end):

        price_data = pd.DataFrame()
        price_data = wb.DataReader(self.Ticker,start,end)

        return price_data

    def get_financials(self):

        Data = yf.Ticker(self.Ticker)
        financials = Data.financials

        return financials

    def get_balance_sheet(self):

        Data = yf.Ticker(self.Ticker)
        balance_sheet = Data.balance_sheet

        return balance_sheet

    def get_cashflow(self):

        Data = yf.Ticker(self.Ticker)
        cashflow = Data.cashflow

        return cashflow

    def get_info(self):

        Data = yf.Ticker(self.Ticker)
        info = Data.info

        return info



