"""
bollinger_strategy.py: 
This code should generate a .png chart that illustrates the bollinger bands, 
and entry and exit points for a bollinger-based strategy.

It should also generate an orders.csv file that you feed into your market simulator 
to backtest the strategy. 
"""

import pandas as pd
import helper

from matplotlib import pyplot as plt


ORDERS_FILE = "../mc2_p1/orders/bb_orders.csv"


def bollinger_strategy(start, end, symbol='IBM'):
	symbols = [symbol]

	mr = helper.setup_marketdata(symbols, start, end)

	rsma = helper.get_SMA(mr)
	rstd = helper.get_rolling_std(mr)
	upper, lower = helper.get_bollinger_bands(rsma, rstd)


	mr['UPPER'] = upper
	mr['LOWER'] = lower
	mr['SMA'] = rsma
	mr = mr.dropna() # drop frist 20 trading days
	m = mr.copy()
	m['Date'] = mr.index
	m.index = range(len(m))

	# set up plot
	ax = mr.plot()
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	ax.set_title("Bollinger Band - BUY and SELL Signals")


	in_long = False
	in_short = False

	helper.setup_orders_file(ORDERS_FILE)

	for i, day in m.iterrows():
		if i>0: # skip first day
			if not in_long and not in_short:
				if m.loc[i-1, symbol] < m.loc[i-1, 'LOWER'] and day[symbol] > day['LOWER']: # BUY signal
					helper.set_order(ORDERS_FILE, day['Date'], symbol, 'BUY')
					in_long = True
					ax.axvline(day['Date'], color='green')

				if m.loc[i-1, symbol] > m.loc[i-1, 'UPPER'] and day[symbol] < day['UPPER']: # SELL signal
					helper.set_order(ORDERS_FILE, day['Date'], symbol, 'SELL')
					in_short = True
					ax.axvline(day['Date'], color='red')

			if in_long:
				if m.loc[i-1, symbol] < m.loc[i-1, 'SMA'] and day[symbol] > day['SMA']: # crossing SMA from below
					helper.set_order(ORDERS_FILE, day['Date'], symbol, 'SELL')
					in_long = False
					ax.axvline(day['Date'], color='black')

			if in_short:
				if m.loc[i-1, symbol] > m.loc[i-1, 'SMA'] and day[symbol] < day['SMA']: # crossing SMA from above
					helper.set_order(ORDERS_FILE, day['Date'], symbol, 'BUY')
					in_short = False
					ax.axvline(day['Date'], color='black')

	plt.savefig('bb_buy_sell_signals.png', bbox_inches='tight')
	plt.show()
	

def test():
	bollinger_strategy('2007-12-31', '2009-12-31')


if __name__ == "__main__":
	test()
  