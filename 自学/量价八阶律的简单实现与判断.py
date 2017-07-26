#通过价量关系选股择时
#基于沪深300

import numpy as np
import pandas as pd
#设置基本参数
start = '2014-01-01'
end   = '2016-04-16'
capital_base = 1000000
refresh_rate = 1
benchmark = 'HS300'
freq = 'd'

#设置股票池 以平安银行为例
universe = set_universe('HS300')

#全局参数
Timelenth=10     # 成交量和价格指标周期 单位为天  做长线  就调为20、30、120
VOLrate=0.3     # 成交量判断比率 调节系统灵敏度
VOLrang=2       # 成交量区间长度
VOLintL={}       # 成交量增缩量区间记录 判断是否符合区间长度
VOLcotL={}       # 成交量平量区间记录
VALrate=0.02     #价格走势判断比率
VALrang=2       # 价格区间长度
VALintL={}       # 价格区间记录 判断是否符合区间长度
VALcotL={}       # 平价区间记录

def initialize(account):
    account.weight=0.01
    pass

def handle_data(account):
    curTime=str(account.current_date)[:10]
    cash=account.cash

    for stock in account.universe:
        VALstate=-2
        VOLstate=-2
        '''成交量趋势模块
        '''
        global VOLintL
        global VOLcotL
        VOLintL.setdefault(stock, 0)
        VOLcotL.setdefault(stock, 0)
        fastVOLList=account.get_attribute_history('turnoverVol', Timelenth)[stock]
        fastVOL=np.mean(fastVOLList)   #获取15日成交量均线
        curVOL=account.get_attribute_history('turnoverVol', 1)[stock][0]   #上一交易日成交量

        #处理数据，判断增量缩量及后续操作
        if curVOL > (fastVOL * (1+VOLrate)):
            VOLcotL[stock]=0
            if VOLintL[stock]>0:
                VOLintL[stock] +=1
            else:
                VOLintL[stock]=1
            if VOLintL[stock]>=VOLrang:
                VOLstate=1
        elif curVOL < (fastVOL * (1-VOLrate)):
            VOLcotL[stock]=0
            if VOLintL[stock]<0:
                VOLintL[stock] -=1
            else:
                VOLintL[stock]=-1
            if abs(VOLintL[stock]) >= VOLrang:
                VOLstate=-1
        else:
            VOLcotL[stock] +=1
            if VOLcotL[stock] >= VOLrang:
                VOLstate=0

        '''价格趋势模块
        '''
        global VALintL
        global VALcotL
        VALintL.setdefault(stock, 0)
        VALcotL.setdefault(stock, 0)
        fastMAList=account.get_attribute_history('closePrice',Timelenth)[stock]
        fastMA=np.mean(fastMAList)    #计算15日均线
        VALlist=account.get_attribute_history('closePrice', 2)[stock]
        curVAL=VALlist[1]  #交易日收盘价
        preVAL=VALlist[0]  #上一交易日收盘价
        #print curTime,preVAL,curVAL

        #处理数据，判断价格走势区间
        if curVAL > (preVAL * (1+VALrate)):
            VALcotL[stock]=0
            if VALintL[stock]>0:
                VALintL[stock] +=1
            else:
                VALintL[stock]=1
            if VALintL[stock]>=VALrang:
                VALstate=1
        elif curVAL < (preVAL * (1-VALrate)):
            VALcotL[stock]=0
            if VALintL[stock]<0:
                VALintL[stock] -=1
            else:
                VALintL[stock]=-1
            if abs(VALintL[stock]) >= VALrang:
                VALstate=-1
        else:
            VALcotL[stock] +=1
            if VALcotL[stock] >= VALrang:
                VALstate=0


        '''逻辑处理模块
        '''
        curState=statePackage(VOLstate,VALstate)
        price=account.referencePrice[stock]   # 股票参考价
        buyNum=account.valid_secpos.get(stock, 0)

        if curState == 1:
            buyNum += int(cash * account.weight / price)
        elif curState == 2:
            buyNum = int(buyNum / 2)
        elif curState == 3:
            buyNum = int(buyNum * 2 / 3)
        elif curState == 4:
            buyNum = int(buyNum * 5 / 6)
        elif curState == 5:
            buyNum =0
        elif curState == 6:
            buyNum += int(cash * 0.3 * account.weight / price)
        elif curState == 7:
            buyNum += int(cash * 0.6 * account.weight / price)
        elif curState == 8:
            buyNum += int(cash  * account.weight / price)

        order_to(stock, buyNum)

#量价八阶律封装  输入当前价格状态和成交量状态，返回处于什么量价阶段
def statePackage(volstate,valstate):
    #量增价平=1，量增价升=2，量平价升=3，量减价升=4，量减价平=5，量减价减=6，量平价减=7，量增价减=8
    stateDict={'1,0':1,'1,1':2,'0,1':3,'-1,1':4,'-1,0':5,'-1,-1':6,'0,-1':7,'1,-1':8}
    key=str(volstate)+','+str(valstate)
    return stateDict.get(key,0)