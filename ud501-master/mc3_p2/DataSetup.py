
import helper


class DataSetup(object):


	def __init__(self, symbol, start, end):
		self.data = helper.setup_marketdata([symbol], start, end)
		self.shape = self.data.shape

	def sma(self, period=20, cut=20, norm = False):
		"""
		Returns the Simple Moving Average
		"""
		sma = self.data.rolling(period, center=False).mean()
		sma = sma[cut:].values
		if norm:
			return ((sma / self.data[cut:].values) - 1)[:,0]
		else: 
			return sma[:,0]


	def ema(self, period=20, cut=20, norm = False):
		"""
		Returns the Exponential Moving Average
		"""
		ema = self.data.ewm(span=period).mean()
		ema = ema[cut:].values
		if norm:
			return ((ema / self.data[cut:].values) - 1)[:,0]
		else:
			return ema[:,0]


	def rstd(self, period=20, cut=20, norm=False):
		"""
		Returns the Rolling Standard Deviation
		"""
		rstd = self.data.rolling(period, center=False).std()
		rstd = rstd[cut:].values
		return rstd[:,0]


	def fdr(self, period=5, cut=20):
		"""
		Return Futur Daily Return for period Days
		"""
		fdr = self.data.copy()
		fdr[period:] = (self.data[period:] / self.data[:-period].values) - 1
		fdr.ix[:period, :] = 0 # set daily returns for row 0 to 0
		fdr = fdr[cut:].values
		return fdr[:,0]


	def bbands(self, period=20, cut=20, norm=False):
		if norm:
			sma = helper.get_SMA(self.data, period)
			rstd = helper.get_RSTD(self.data, period)
			bbn = helper.get_BBands_normalised(self.data, sma, rstd)
			bbn = bbn[cut:].values
			return bbn[:,0]
		else:
			return None

	def momentum(self, period=5, cut=20):
		momentum = (self.data[:-period]/self.data[period:].values) - 1
		momentum = momentum[(cut-period):].values
		return momentum[:,0]
		

	def volatility(self, fdr_period=5, vot_period=20, cut=20):
			fdr = helper.get_FDR(self.data, fdr_period)
			vot = helper.get_RSTD(fdr, vot_period) # volatility
			vot = vot[cut:].values
			return vot[:,0]
