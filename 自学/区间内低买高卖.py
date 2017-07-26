#区间内低买高卖
import numpy as np
#设置基本参数
start = '2016-02-01'
end   = '2016-03-28'
capital_base = 1000000
refresh_rate = 10
benchmark = 'HS300'
freq = 'm'

#设置股票池 以平安银行为例
universe = ['000001.XSHE', ]

def initialize(account):
    account.interval=30    #区间统计周期 单位为天
    account.lowRate=0.2    #区间内买入阈值
    account.highRate=0.8   #区间内卖出阈值
    account.weight=0.5     #仓位比例
    pass

def handle_data(account):
    moneyTotal = account.referencePortfolioValue       #获取当前账户资产总额
    price=account.referencePrice[account.universe[0]]    # 股票参考价

    highPriceDict=account.get_daily_attribute_history('highPrice', account.interval)
    highPrice=max(highPriceDict[account.universe[0]])    #获取区间长度内最高价格
    lowPriceLDict=account.get_daily_attribute_history('lowPrice', account.interval)
    lowPrice=min(lowPriceLDict[account.universe[0]])     #获取区间长度内最低价格

    buyPrice=(highPrice-lowPrice)*account.lowRate+lowPrice     #根据阈值计算买入价格
    soldPrice=(highPrice-lowPrice)*account.highRate+lowPrice   #根据阈值计算卖出价格
    if not np.isnan(price):
        buyNum=int(moneyTotal / price * account.weight) - account.valid_secpos.get(account.universe[0], 0)  #可增持仓位=总仓位-当前所持仓位
        if price <buyPrice:
            order(account.universe[0], buyNum,price,'limit')  #低位买进
        elif price >soldPrice:
            order_to(account.universe[0], 0)             #高位卖出