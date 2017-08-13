import pandas as pd


def get_daily_returns(df):
	"""Compute and return the daily return values."""
	daily_returns = df.copy()
	daily_returns[1:] = (df[1:] / df[:-1].values) - 1
	daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0
	return daily_returns

def get_rolling_mean(values, window=20):
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