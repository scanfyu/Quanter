"""MC2-P1: Market simulator."""

import pandas as pd
import numpy as np
import datetime as dt
import os

import matplotlib.pyplot as plt

from util import get_data, plot_data

#plt.style.use('dark_background')

ORDERS_FILE = "bag_orders.csv" 
LEVERAGE_ON = False


def assess_portfolio(port_val):
    # .values to avoid alignment on index
    daily_rets = port_val[1:].values / port_val[:-1] - 1
    # Line below commented out to match test case answers
    # daily_rets = daily_rets[1:] # exclude day 1

    # Cumulative return
    cr = port_val[-1] / port_val[0] - 1

    # Average daily return
    adr = daily_rets.mean()

    # Standard deviation of daily return
    sddr = daily_rets.std()

    # Sharpe Ratio, risk adjusted (0%) return
    sr = (adr - 0) / sddr
    sr *= 252**0.5 # adjustment for daily sampling (for annual measure)

    return cr, adr, sddr, sr


def get_price_by_date(prices, symbol, date):
    return prices.loc[date][symbol]

def get_symbols(orders):
    symbols = []
    for ixorder, order in orders.iterrows():
        if order['Symbol'] not in symbols:
            symbols += [order['Symbol']]
    return symbols

def leverage(longs, shorts, cash):
    # leverage = (sum(longs) + sum(abs(shorts))) / (sum(longs) - sum(abs(shorts)) + cash)
    l = sum(longs.values())
    s = sum(map(abs, shorts.values()))
    return (l + s) / (l - s + cash) #TODO take care that we don't divide through 0.0


def compute_portvals(orders_file = "./orders/orders.csv", start_val = 1000000):
    # this is the function the autograder will call to test your code

    orders = pd.read_csv(orders_file, index_col='Date', parse_dates=True, na_values=['nan'])
    orders = orders.sort_index()
    orders['Date'] = orders.index
    orders.index = range(len(orders))
    # orders looks like this:
    #    Symbol Order  Shares       Date
    # 0    AAPL   BUY    1500 2011-01-14
    # 1    AAPL  SELL    1500 2011-01-19

    symbols = get_symbols(orders)

    start_date = orders.head(1)['Date'].values[0]
    end_date = orders.tail(1)['Date'].values[0]

    dates = pd.date_range(start_date, end_date)
    price_data = get_data(symbols, dates)
    spy = price_data['SPY']

    portfolio = pd.DataFrame(0, index=spy.index, #spy.index indicates trading days
            columns=['Cash', 'Value'] + symbols)
    portfolio['Date'] = portfolio.index
    portfolio.index = range(len(portfolio))
    # portfolio looks like this:
    #   Cash  Value  AAPL  IBM  GOOG  XOM       Date
    #0     0      0     0    0     0    0 2011-01-14
    #1     0      0     0    0     0    0 2011-01-18
    #2     0      0     0    0     0    0 2011-01-19

    # setup starting values
    cash = start_val
    portfolio.loc[0, 'Cash'] = start_val
    portfolio.loc[0, 'Value'] = start_val
    ixlast = len(portfolio)-1
    

    longs, shorts = {}, {}
    for key in symbols:
        longs[key], shorts[key] = 0, 0


    for ixday, day in portfolio.iterrows():
        for ixorder, order in orders.iterrows():
            if day['Date'] == order['Date']: # we are placing a trade
                symbol = order['Symbol']
                shares = order['Shares']
                price = get_price_by_date(price_data, order['Symbol'], order['Date']) # How much will we need?
                
                if order['Order'] == 'BUY':
                    #############################################################################
                    if (LEVERAGE_ON):
                        shares_temp = portfolio.loc[ixday, symbol] + shares # plus because we BUY
                        if (shares_temp <= 0):
                            shorts[symbol] = price * shares_temp
                        else:
                            longs[symbol] = price * shares_temp
                        if leverage(longs, shorts, cash - (price * shares)) > 2.0:
                            break
                    
                    #############################################################################
                    cash -= (price * shares)
                    portfolio.loc[ixday,'Cash'] = cash
                    portfolio.loc[ixday, symbol] += shares

                if order['Order'] == 'SELL':
                    #############################################################################
                    if (LEVERAGE_ON):
                        shares_temp = portfolio.loc[ixday, symbol] - shares # minus because we SELL
                        if (shares_temp >= 0):
                            longs[symbol] = price * shares_temp
                        else:
                            shorts[symbol] = price * shares_temp
                        if leverage(longs, shorts, cash + (price * shares)) > 2.0:
                            break
                    
                    ############################################################################
                    cash += (price * shares)
                    portfolio.loc[ixday,'Cash'] = cash
                    portfolio.loc[ixday, symbol] -= shares

        value = 0
        symbol_value = 0
        for symbol in symbols:
            symbol_value = portfolio.loc[ixday, symbol] * get_price_by_date(price_data, symbol, day['Date'])
            value += symbol_value
        value = value + cash
        portfolio.loc[ixday, 'Value'] = value     

        if ixday < ixlast:
            # the day is over, update the row for the next day
            portfolio.loc[ixday+1, ['Cash']+symbols] = portfolio.loc[ixday, ['Cash']+symbols]

    #print(portfolio.tail(5))

    portfolio.index = portfolio['Date']
    return portfolio['Value']

def test_code():
    # this is a helper function you can use to test your code
    # note that during autograding his function will not be called.
    # Define input parameters


    of = "./orders/" + ORDERS_FILE
    sv = 10000

    # Process orders
    portvals = compute_portvals(orders_file = of, start_val = sv)
    if isinstance(portvals, pd.DataFrame):
        portvals = portvals[portvals.columns[0]] # just get the first column
    else:
        "warning, code did not return a DataFrame"
    
    # Get portfolio stats
    # Here we just fake the data. you should use your code from previous assignments.
    start_date = portvals.index[0]
    end_date = portvals.index[-1]

    spy = get_data(['IBM'], pd.date_range(start_date,end_date)).ix[:,'IBM']

    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = assess_portfolio(portvals)
    cum_ret_SPY, avg_daily_ret_SPY, std_daily_ret_SPY, sharpe_ratio_SPY = assess_portfolio(spy)

    
    # Plot for MC2-Project-2
    ax = (portvals/portvals[0]).plot()
    ax = (spy/spy[0]).plot()
    ax.grid(True)
    ax.set_xlabel("Date")
    ax.set_ylabel("Normalised price")
    ax.legend(['IBM Managed', 'IBM'])
    ax.set_title("IBM Managed vs. IBM")
    
    #plt.savefig('ibm_bs_vs_spy.png', bbox_inches='tight')
    plt.show()
    

##########################################################################################
#Test Cases order.csv
##########################################################################################

def test_orders_01_csv():

    of = "./orders/" + ORDERS_FILE
    sv = 10000

    portvals = compute_portvals(orders_file = of, start_val = sv)
    if isinstance(portvals, pd.DataFrame):
        portvals = portvals[portvals.columns[0]] # just get the first column
    else:
        "warning, code did not return a DataFrame"

    start_date = portvals.index[0]
    end_date = portvals.index[-1]
    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = assess_portfolio(portvals)

    num_days = len(portvals)
    last_day_portval = portvals.values[-1]
    print(last_day_portval)
    print(sharpe_ratio)
    print(avg_daily_ret)

if __name__ == "__main__":
  test_code()
