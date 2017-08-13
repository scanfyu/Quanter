#移动平均线之金叉和死叉

import numpy as np
#设置基本参数
start = '2015-01-01'
end   = '2016-02-28'
capital_base = 1000000
refresh_rate = 1
benchmark = 'HS300'
freq = 'd'

#设置股票池 以平安银行为例
universe = ['000001.XSHE', ]

def initialize(account):
    account.slowMA=20      #慢速均线周期  单位天
    account.fastMA=15      #快速均线周期
    account.preslowMA=0     #上一周期慢线  用于判断金叉死叉
    account.prefastMA=0     #上一周期快线
    pass

def handle_data(account):
    slowMAList=account.get_attribute_history('closePrice', account.slowMA)[account.universe[0]]   #获取慢速周期内收盘价列表
    slowMA=calc_MA(slowMAList)    #计算20日均线   即慢线
    fastMAList=account.get_attribute_history('closePrice',account.fastMA)[account.universe[0]]   #获取快速周期内收盘价格列表
    fastMA=calc_MA(fastMAList)    #计算15日均线   即快线

    if slowMA==fastMA:
        moneyTotal = account.referencePortfolioValue      #获取当前账户资产总额
        price=account.referencePrice[account.universe[0]]   # 股票参考价
        buyNum=int(moneyTotal / price) - account.valid_secpos.get(account.universe[0], 0)  #可增持仓位=总仓位-当前所持仓位

        if account.preslowMA>account.prefastMA:      #慢线高于快线，即趋势为快线上穿慢线，形成金叉
            print  'we got a golden cross on:  ',account.current_date,
            print(slowMA)
            order(account.universe[0], buyNum)  #买入操作
        elif account.prefastMA>account.preslowMA:    #快线高于慢线，即趋势为快线下穿慢线，形成死叉
            print  'we got a death cross on:  ',account.current_date,
            print(slowMA)
            order_to(account.universe[0], 0)   #全部卖出

    account.preslowMA=slowMA
    account.prefastMA=fastMA

#加权平均算法计算MA值
def calc_MA(MAList):
    result=0
    length=len(MAList)
    if length>0:
        for i in MAList:
            result +=i
        result= result / length
    return round(result,2)