


import helper


class DataSetup(object):


	def __init__(self, data):
		self.data = data

	def sma(self, period):
		sma = helper.get_SMA(data, period)
		sma = sma[period:].values
		return sma

	def ema(self, period):
		ema = helper.get_SMA
		ema = ema[period:].values
