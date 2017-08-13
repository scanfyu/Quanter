""" 
my_strategy.py: 
This code should generate a .png chart (or charts) that illustrate the clever strategy you develop, 
along with indications of entry and exit points. 
It should also generate an orders.csv file that you feed into your market simulator to backtest the strategy.


TODO: implement MACD
"""

import helper

from matplotlib import pyplot as plt
from matplotlib import gridspec as gsp

ORDERS_FILE = "../mc2_p1/orders/macd_orders.csv"

# standard MACD 12,26,9
# faster MACD 3,5,13

def my_strategy(start, end):

	symbols = ['IBM']
	symbol = symbols[0]

	mdata = helper.setup_marketdata(symbols, start, end)
	fast = helper.get_EMA(mdata, window=12)
	slow = helper.get_EMA(mdata, window=26)
	macd = fast - slow
	signal = helper.get_EMA(macd, window=9)
	sma = helper.get_SMA(mdata, window=20)

	mdata['FAST'] = fast
	mdata['SLOW'] = slow 
	mdata['MACD'] = macd
	mdata['SIGNAL']= signal
	mdata['HISTO'] = macd - signal 
	mdata['SMA'] = sma 
	
	# switch index
	m = mdata.copy()
	m['DATE'] = m.index
	m.index = range(len(m))  

	# set up the plot
	macd = mdata.copy()
	price = mdata.copy()
	macd = mdata[['MACD', 'SIGNAL']]
	price = mdata[['IBM']]
	fig = plt.figure()
	G = gsp.GridSpec(2, 1)
	ax1 = plt.subplot(G[0, :])
	ax2 = plt.subplot(G[1, :])
	ax1.plot(price)
	ax1.set_ylabel("Price " + str(symbol))
	ax1.grid(True) 
	ax2.plot(macd)
	ax2.set_ylabel("MACD")
	ax2.set_xlabel("Date")

	in_long = False
	in_short = False
	
	helper.setup_orders_file(ORDERS_FILE)

	for i, day in m.iterrows():
		if i>0: # skip first 1 day
			if not in_long or not in_short:
				if m.loc[i-1, 'MACD'] < m.loc[i-1, 'SIGNAL'] \
					and day['MACD'] > day['SIGNAL']:
					#and (day['HISTO'] / m.loc[i-3, 'HISTO'] - 1) > 0.2: 
					helper.set_order(ORDERS_FILE, day['DATE'], symbol, 'BUY')
					in_long = True
					ax1.axvline(day['DATE'], color='green')
					ax2.axvline(day['DATE'], color='green')
				if m.loc[i-1, 'MACD'] > m.loc[i-1, 'SIGNAL'] \
					and day['MACD'] < day['SIGNAL']:
					#and (day['HISTO'] / m.loc[i-3, 'HISTO'] - 1) < -0.2:
					helper.set_order(ORDERS_FILE, day['DATE'], symbol, 'SELL')
					in_short = True
					ax1.axvline(day['DATE'], color='red')
					ax2.axvline(day['DATE'], color='red')
			if in_long:
				if m.loc[i-1, symbol] < m.loc[i-1, 'SMA'] and day[symbol] > day['SMA']: 
					helper.set_order(ORDERS_FILE, day['DATE'], symbol, 'SELL')
					in_long = False
					ax1.axvline(day['DATE'], color='black')
					ax2.axvline(day['DATE'], color='black')
			if in_short:
				if m.loc[i-1, symbol] > m.loc[i-1, 'SMA'] and day[symbol] < day['SMA']:
					helper.set_order(ORDERS_FILE, day['DATE'], symbol, 'BUY')
					in_long = False
					ax1.axvline(day['DATE'], color='black')
					ax2.axvline(day['DATE'], color='black')

	plt.tight_layout()
	plt.show()



def test():
	my_strategy('2007-12-31', '2009-12-31')

if __name__ == "__main__":
	test()