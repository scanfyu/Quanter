import pandas as pd
import numpy as np
import os

from util import get_data


def setup_marketdata(symbols, start, end, addSPY=False):
	dates = pd.date_range(start, end)
	market = get_data(symbols, dates, addSPY=addSPY)
	market = market.dropna() # remove non trading days
	return market


def setup_orders_file(name):
	open(name, 'w').close()
	os.utime(name, None)
	with open(name, 'a') as f:
		print("Date,Symbol,Order,Shares", file=f)

def set_order(name, date, symbol, order, shares=100):
	with open(name, 'a') as f:
		print(str(date.date()) + "," + str(symbol) + "," + str(order) + "," + str(shares), file=f)

###########################################################################################

def get_daily_returns(df):
	"""Compute and return the daily return values."""
	daily_returns = df.copy()
	daily_returns[1:] = (df[1:] / df[:-1].values) - 1
	daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0
	return daily_returns

def get_SMA(values, window=20):
	"""Return rolling mean of given values, using specified window size."""
	return values.rolling(window, center=False).mean()

def get_rolling_std(values, window=20):
	"""Return rolling standard deviation of given values, using specified window size"""
	return values.rolling(window, center=False).std()

def get_bollinger_bands(rm, rstd):
	"""Return upper and lower Bollinger Bands."""
	upper_band = rm + 2*rstd
	lower_band = rm - 2*rstd
	return upper_band, lower_band

def get_EMA(values, window=20):
	return values.ewm(span=window).mean()