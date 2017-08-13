import pandas as pd
import numpy as np
import os
import math

from util import get_data
from matplotlib import pyplot as plt 


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

def analyse(learner, trainX, trainY, testX, testY, description):
	learner.addEvidence(trainX, trainY)
	predY = learner.query(testX)

	rmse = math.sqrt(((testY - predY) ** 2).sum()/trainY.shape[0])
	c = np.corrcoef(predY, y=testY)

	fig = plt.figure()
	plt.scatter(testY, predY)
	title = description + " rmse " + str(rmse) + " c " + str(c[0,1])
	fig.suptitle(title, fontsize=16)
	plt.xlabel('testY')
	plt.ylabel('predY')
	plt.savefig(description.strip() + ".png", bbox_inches='tight')
	plt.grid(True)
	plt.show()



###########################################################################################


def get_FDR(data, days=5):
	"""Compute and return the daily return values."""
	daily_returns = data.copy()
	daily_returns[days:] = (data[days:] / data[:-days].values) - 1
	daily_returns.ix[:5, :] = 0 # set daily returns for row 0 to 0
	return daily_returns

def get_SMA(values, window=20):
	"""Return rolling mean of given values, using specified window size."""
	return values.rolling(window, center=False).mean()

def get_RSTD(values, window=20):
	"""Return rolling standard deviation of given values, using specified window size"""
	return values.rolling(window, center=False).std()

def get_BBands(sma, stdev):
	"""Return upper and lower Bollinger Bands."""
	upper_band = sma + 2*stdev
	lower_band = sma - 2*stdev
	return upper_band, lower_band

def get_BBands_normalised(price, sma, stdev):
	"""Return a normalised bb value for the agent"""
	return (price - sma)/(2 * stdev)

def get_EMA(values, window=20):
	return values.ewm(span=window).mean()

#def get_Momentum(currentprice, pastprice):
#	return (currentprice/pastprice) - 1