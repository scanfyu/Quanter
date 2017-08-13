"""
use a bagged KNNLearner k=1 to predict the future return of a 5 trading day period
make it work for IBM and ML4T-240
X values must be min 3 technical features normalised to a range between -1.0 to 1.0
Y values is the future 5 day return

0. write function to calaculate return of n days
1. step plot the data - current price/future price current return/predicted return

a) split up training and test data - done
b) normalise X values - open
c) build a strategy to create an order.csv file - open

Create a trading policy based on what your learner predicts for future return. 
As an example you might choose to buy when the forecaster predicts the price 
will go up more than 1%, then hold for 5 days.
"""

import helper
import DataSetup as ds 
import KNNLearner as knn
import BagLearner as bag
import numpy as np

from matplotlib import pyplot as plt


ORDERS_FILE = "../mc2_p1/orders/bag_orders.csv"


#######
# create strategy here
#######
def strategy(train_start, train_end, trade_start, trade_end, symbol='IBM'):
	symbols = [symbol]

	marketdata = helper.setup_marketdata(symbols, trade_start, trade_end)

	# TODO add 0 in front of the data to fit with marketdata
	traindata = ds.DataSetup(symbol, train_start, train_end)
	tradedata = ds.DataSetup(symbol, trade_start, trade_end)

	train = np.zeros((traindata.shape[0]-20, 4))
	train[:,0] = traindata.bbands(20,20,norm=True)
	train[:,1] = traindata.momentum(5,20)
	train[:,2] = traindata.volatility(5,20,20)
	train[:,3] = traindata.fdr(5,20)

	trainX = train[:,0:-1]
	trainY = train[:,-1]

	trade = np.zeros((tradedata.shape[0]-20, 4))
	trade[:,0] = tradedata.bbands(20,20,norm=True)
	trade[:,1] = tradedata.momentum(5,20)
	trade[:,2] = tradedata.volatility(5,20,20)
	trade[:,3] = tradedata.fdr(5,20)

	tradeX = trade[:,0:-1]
	tradeY = trade[:,-1]

	learner = bag.BagLearner(learner = knn.KNNLearner, kwargs = {'k': 1}, \
		bags = 20, boost = False, verbose = False)

	learner.addEvidence(trainX, trainY)
	predY = learner.query(tradeX)

	m = marketdata.copy()
	m['Date'] = marketdata.index
	m.index = range(len(m))

	print(m['Date'].values)


	# set up plot
	ax = marketdata.plot()
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	ax.set_title("BagLearner Strategy - BUY and SELL Signals")

	in_long = False
	in_short = False

	helper.setup_orders_file(ORDERS_FILE)
	timer = 0

	for i, day in m.iterrows():
		if i>=20: # skip first 20 days
			timer -= 1
			print(predY[i-20], day[symbol])
			if not in_long and not in_short:
				if predY[i-20] > 0.01 and timer < 0: #BUY signal
					helper.set_order(ORDERS_FILE, day['Date'], symbol, 'BUY')
					in_long = True
					ax.axvline(day['Date'], color='green')
					timer = 5
				if predY[i-20] < 0.01 and timer < 0: #SELL sigal
					helper.set_order(ORDERS_FILE, day['Date'], symbol, 'SELL')
					in_short = True
					ax.axvline(day['Date'], color='red')
					timer = 5
			if in_long and timer == 0:
				helper.set_order(ORDERS_FILE, day['Date'], symbol, 'SELL')
				in_long = False
				ax.axvline(day['Date'], color='black')

			if in_short and timer == 0:
				helper.set_order(ORDERS_FILE, day['Date'], symbol, 'BUY')
				in_short = False
				ax.axvline(day['Date'], color='black')

	plt.show()

def test():
	strategy('2007-12-31', '2009-12-31', '2009-12-31', '2011-12-31', 'ML4T-240')

if __name__ == "__main__":
	test()

