# AT-MATLAB学习日记——第一周

从本周开始学习AT-MATLAB量化知识。

## 本周目标1：学习量化课堂中的基础知识

1. 熟悉AT入门知识：界面及结构
2. 熟悉AT进阶知识：相关函数构建及数据处理

## AT入门

平台是基于Windows的。。。

介绍了如何安装：感觉可以去实验室了。

介绍了基本界面：用过同花顺以及东方财富的相关软件的可以跳读。

介绍了如何登陆账户：想起了之前用米筐回测的时候用代码初始化一直失败的经历。。。

策略操作逻辑：重点来了。

* 调用策略主函数包括：回测函数、回放函数、交易函数、优化函数
* Pro输出结果包括：回测绩效报告、策略行情回放、真实/模拟交易、输出最优函数
* 策略编写时，需要：命名策略、配置对应参数、调用traderRunBacktest函数、在该函数中输入策略AmaTrade的信息与相关参数后进行回测
* 软件需要MATLAB支持

### 数据内容：[链接](https://www.digquant.com.cn/study.php?mod=course&sub=AT%E9%87%8F%E8%83%BD&aid=99)

| 数据名称     | 数据内容（Double） |
| -------- | ------------ |
| time     | 时间           |
| price    | 成交价          |
| open     | 开盘价          |
| high     | 最高价          |
| low      | 最低价          |
| close    | 收盘价          |
| volume   | 成交量          |
| turnover | 成交金额         |

| 历史Bar数据： traderGetKData | 数据字段：历史K线数据 |
| ----------------------- | ----------- |
| time                    | 时间          |
| open                    | 开盘价格        |
| high                    | 最高价格        |
| low                     | 最低价         |
| close                   | 收盘价         |
| volume                  | 成交量         |
| turnover                | 成交金额        |
| openinteres             | 持仓量         |

| 历史TICK数据： traderGetTickData | 数据字段     |
| --------------------------- | -------- |
| time                        | 时间       |
| price                       | 成交价      |
| volume                      | 成交量      |
| volumetick                  | tick内成交量 |
| openinterest                | 持仓量      |
| bidprice                    | 前5档买价    |
| bidvolume                   | 前5档买量    |
| askprice                    | 前5档卖价    |
| askvolume                   | 前5档卖量    |

| 实时行情数据： tradergetrtDataMulti | 数据字段  |
| ---------------------------- | ----- |
| Market                       | 市场    |
| Time                         | 时间    |
| Code                         | 标的代码  |
| CurrentPrice                 | 当前价   |
| CurrentQuantity              | 当前成交量 |

### **常用数据类别**

| Market市场枚举：代码 | 名称      | Market市场枚举：代码 | 名称        |
| ------------- | ------- | ------------- | --------- |
| SZSE          | 深圳证券交易所 | DCE           | 大连商品交易所   |
| SSE           | 上海证券交易所 | CZCE          | 郑州商品交易所   |
| SHFE          | 上海期货交易所 | CFFEX         | 中国金融期货交易所 |

| FQ复权：类型 | 方向   |
| ------- | ---- |
| NA      | 不复权  |
| FWard   | 向前复权 |
| BWard   | 向后复权 |

| Kfrequency K线类型：级别 | K线类型   |
| ------------------ | ------ |
| min                | 分钟线    |
| day                | 日线     |
| tick               | Tick数据 |

*FilledUp数据补齐*：True（补齐）；False（不补齐）

### 新回测结构

订阅数据：对数据进行计算后返回计算的结果。节省取回后计算的时间。

## AT进阶

### 数据提取：[函数使用](https://www.digquant.com.cn/study.php?mod=course&sub=AT%E9%87%8F%E8%83%BD&aid=101)

| 函数名                       | 说明                                       |
| ------------------------- | ---------------------------------------- |
| **traderGetCodeList**     | 获得指数（包含权重和成分股）、行业板块（没有权重，只有成分股）、地域板块（没有权重，只有成分股）、期权板块的信息，包括成分股及权重等信息 |
| **traderGetCurrentBar**   | 获得当前bar的信息                               |
| **traderGetCurrentBarV2** | 获得当前bar的信息                               |
| **traderGetCurrentTick**  | 获取当前的tick的所有信息                           |
| **traderGetCurTickInfo**  | 获取当前的tick信息                              |
| **traderGetFutureInfo**   | 获取期货信息                                   |
| **traderGetFutureInfoV2** | 获取期货信息                                   |
| **traderGetKData**        | 根据起止时间点提取K线数据；可通过此函数获取该时段内重要的价量数据        |
| **traderGetRegKData**     | 根据已注册的数据序列获取K线数据；可通过此函数获取该时段内重要的价量数据     |
| **traderGetRegTimeLine**  | 获取注册数据的时间序列                              |
| **traderGetRegUserData**  | 根据已注册的用户自行导入的外部数据获取K线数据；可通过此函数获取该时段内重要的价量数据 |
| **traderGetRegUserIndi**  | 根据已注册的用户自建因子序列获取数据索引序列                   |
| **traderGetRtDataMulti**  | 获取多组股票或期货实时报价，品种类型需保持一致，全为股票或全为期货        |
| **traderGetTickData**     | 根据某一时间点提取Tick数据                          |
| **traderGetTickDataV2**   | 提取某一时间段的Tick数据                           |
| **traderGetTradingDays**  | 获取交易日期                                   |
| **traderGetTradingTime**  | 获取交易时间                                   |

### 标的配置

函数：**traderGetTargetList**

说明：若在策略的调用脚本中已定义标的资产，则可在策略函数中通过此函数获取标的资产信息

语法：TargetList = traderGetTargetList( )

输出参数：

​	TargetList：标的资产结构体，具体结构如下

* Market ：市场类型，字符串格式
* Code：交易品种代码，字符串格式，如‘000002’

 示例：

​	策略调用脚本中已定义

```matlab
targetList(1).Market = 'CFFEX';
targetList(1).Code = 'IF0000';
```

​	策略中获取标的资产信息

```matlab
TargetList = traderGetTargetList( )
```

### 账户信息获取：[详细](https://www.digquant.com.cn/study.php?mod=course&sub=AT%E9%87%8F%E8%83%BD&aid=103)

| 函数名称                              | 说明                    |
| --------------------------------- | --------------------- |
| **traderGetAccountConfig**        | 获取当前账户的配置信息           |
| **traderGetAccountInfoV2**        | 通过账户句柄索引序列号获得账户当前资金情况 |
| **traderGetAccountInfo**          | 通过账户句柄获得账户当前资金情况      |
| **traderGetAccountPosInfo**       | 获取指定帐号当前所有持仓信息        |
| **traderGetAccountPositionV2**    | 获得当前仓位信息              |
| **traderGetAccountPosition**      | 获得当前仓位信息              |
| **traderGetAccountPositionDir**   | 获得当前多头或者空头的仓位信息       |
| **traderGetAccountPositionDirV2** | 获得当前多头或者空头的仓位信息       |
| **traderGetAlgoFinished**         | 获取算法下单时当前母单里已经完成的子单数目 |
| **traderGetHandleList**           | 获得账户句柄                |
| **traderGetParentOperation**      | 获取当前正在执行的母单信息         |

### 开平仓设置：[详细](https://www.digquant.com.cn/study.php?mod=course&sub=AT%E9%87%8F%E8%83%BD&aid=104)

1. **考虑当前仓位的开平仓指令**

| 函数名称               | 说明                     |
| ------------------ | ---------------------- |
| traderBuy          | 买入下单，若初始有空头持仓，则先平仓，再买入 |
| traderBuyV2        | 买入下单，若初始有空头持仓，则先平仓，再买入 |
| traderBuyToCover   | 买入平仓下单                 |
| traderBuyToCoverV2 | 买入平仓,前提是有空仓,否则操作无效     |
| traderSell         | 卖出平仓下单                 |
| traderSellV2       | 多单的平仓下单，即卖出平仓下单        |
| traderSellShort    | 卖出下单，若初始有多头持仓，则先平仓，再卖出 |
| traderSellShortV2  | 卖出下单，若初始有多头持仓，则先平仓，再卖出 |

2. **不考虑当前仓位的开平仓指令**

| 函数名称               | 说明                             |
| ------------------ | ------------------------------ |
| traderCloseAll     | 平指定账户所有持仓(不包含冻结部分)，回测中不支持使用此接口 |
| traderDirectBuy    | 买入下单，初始持仓无影响                   |
| traderDirectBuyV2  | 买入下单，初始持仓无影响                   |
| traderDirectSell   | 卖出下单，初始持仓无影响                   |
| traderDirectSellV2 | 卖出下单，初始持仓无影响                   |

3. **以仓位为目标，可双向调整直接达到目标仓位**

| 函数名称               | 说明                                  |
| ------------------ | ----------------------------------- |
| traderPositionTo   | 调仓到指定仓位                             |
| traderConfigTo     | 对账户进行配置。配置型回测专用，与traderBuy等交易函数不能混用 |
| traderPositionToV2 | 调仓到指定仓位                             |

### 委托单查询

| 函数名称                               | 说明                 |
| ---------------------------------- | ------------------ |
| **traderCancelOrder**              | 撤销未成交的限价单          |
| **traderGetLastChangeOrder**       | 获取最后一个状态改变的报单      |
| **traderGetStopOrderInfoByID**     | 获取止盈、止损、跟踪止盈单的订单信息 |
| **traderGetStopOrderInfoByTarget** | 获取开仓订单号的订单信息       |
| **traderIsStopOrderFired**         | 判断止盈止损单是否触发        |
| **traderOrderFilledPrice**         | 判断限价单是否成交          |

### 日内平仓设置

- 函数名称：**traderDailyCloseTime**

- 函数说明：日内平仓时间设置

- 语法：

  traderDailyCloseTime(time)

- 用法：

  输入参数：

  time：平仓时间，整型，如：112500代表11:25:00

- 示例：

  在当日14:00平掉所有持仓

  ```matlab
  traderDailyCloseTime(140000);
  ```

### 策略回测函数：[链接](https://www.digquant.com.cn/study.php?mod=course&sub=AT%E9%87%8F%E8%83%BD&aid=107)

| 函数名称                    | 说明         |
| ----------------------- | ---------- |
| **traderSetBacktest**   | 设置回测初始信息   |
| **traderRunBacktest**   | 实现策略的回测    |
| **traderRunBacktestV2** | 实现策略的回测    |
| **traderSetParalMode**  | 设置函数计算并行模式 |

### 策略回放函数：[链接](https://www.digquant.com.cn/study.php?mod=course&sub=AT%E9%87%8F%E8%83%BD&aid=108)

| 函数名称                       | 说明              |
| -------------------------- | --------------- |
| **traderRunReplay**        | 实现策略的回放         |
| **traderRunReplayByOrder** | 报单变化驱动的策略回放启动函数 |

### 启动与终止交易：[链接](https://www.digquant.com.cn/study.php?mod=course&sub=AT%E9%87%8F%E8%83%BD&aid=109)

| 函数名称                          | 说明                  |
| ----------------------------- | ------------------- |
| **traderRunRealTrade**        | 实现策略的实盘交易，只支持单一策略   |
| **traderRunRealTradeByOrder** | 报单状态变化驱动的策略实时交易启动函数 |
| **traderShowRealTrade**       | 显示正在进行的实时运算         |
| **traderStartRealTrade**      | 实现策略的实时交易，支持多策略同时交易 |
| **traderStopRealTrade**       | 停止实时运算              |

### 算法下单：[链接](https://www.digquant.com.cn/study.php?mod=course&sub=AT%E9%87%8F%E8%83%BD&aid=110)

1. **twap - 时间加权平均价格算法下单**

* 用途：在回测、回放、实盘交易以及策略优化中实现twap( Time Weighted Average Price ) 算法下单，主要思想是将交易时间均匀分割，并将需要执行的订单均匀分配在每个分割点上，一方面通过拆单减少对市场的影响，另一方面获得一个较低的平均成交价格，从而降低交易成本。
* 函数结构：twap ( ChildOrderNum, ChildOrderInterval )
* 输入参数说明：

ChildOrderNum为将一个母单拆分为子单的手数，ChildOrderInterval为相邻子单之间的tick时间间隔

* 调用格式：在回测、回放、实盘交易以及策略优化函数最后两个输入项分别输入@twap及参数数值
* 示例：

对策略strategy进行回测和实盘交易，使用twap算法下单，具体地，将母单拆分为10手每个子单，每隔12个tick下一个子单

```Matlab
traderRunBacktest('Strategy',@Strategy,{var1,var2,var3},targetList,'min',1,20150301,20150331,@twap,{10,12});

traderStartRealTrade('Strategy',@Strategy,{var1,var2,var3},AccountList,targetList,'min',1,20150501,@twap,{10,12});
```

2. **vwap -成交量加权平均价格算法下单**

* 用途：在回测、回放、实盘交易以及策略优化中实现vwap(Volume Weighted Average Price ) 算法下单，主要思想是将交易时间均匀分割，并将需要执行的订单均匀分配在每个分割点上，一方面通过拆单减少对市场的影响，另一方面获得一个较低的平均成交价格，从而降低交易成本。
* 函数结构：vwap(ChildOrderNum,ChildOrderInterval)  
* 输入参数说明：

ChildOrderNum为将一个母单拆分为子单的个数，ChildOrderInterval为相邻子单之间的tick时间间隔

* 调用格式：在回测、回放、实盘交易以及策略优化函数最后输入项输入@vwap及参数数值
* 示例：

对策略strategy进行回放，使用vwap算法下单，具体地，将母单拆分为10个子单，每隔12个tick下一个子单,

```Matlab
traderRunReplay('Strategy',@Strategy,{var1,var2,var3},targetList,'min',1,20150301,'20150529T000000.000','20150529T235959.000',@vwap,{10,12});
```

### 数据处理：[链接](https://www.digquant.com.cn/study.php?mod=course&sub=AT%E9%87%8F%E8%83%BD&aid=111)

| 函数名称                       | 说明          |
| -------------------------- | ----------- |
| **traderAppendKDataScope** | 扩充低频数据      |
| **traderRegKData**         | 注册数据        |
| **traderRegUserData**      | 注册用户外部导入的数据 |
| **traderRegUserIndi**      | 注册用户自建的外部因子 |

### 历史回测

1. 回测逻辑

策略：止盈、止损、跟踪止盈；

方式：采用tick数据回测，同时满足止盈止损时，采用tick数据启动；

例子：下一根bar开盘价，下一tick，对手价成交，下几个tick或下几个tick对手价等；

（仅机构版支持止盈止损设置以及 tick 级别数据回测）



*编写逻辑：*

StrategyspeculateMACD为策略名称，该策略需要输入的变量参数为：Freq，stopTar，profitTar，pct，shareNum，对StrategyspeculateMACD进行回测的调用方法如下图：

![StrategyspeculateMACD](https://www.digquant.com.cn/data/attachment/portal/201705/17/151721lz0xceefccmf585q.png)



2. 回测设置

初始化信息设置，使用traderSetBacktest对回测过程中的各项配置提前赋值或选择。该函数仅限于期货策略使用，股票策略无需配置。

```matlab
traderSetBacktest(InitialCash,Costfee,Rate,SlidePrice,PriceLoc,DealType,LimitType)
```

*输入参数：*

* InitialCash：初始资本，默认为1000000
* Costfee：手续费率，默认为0.0025
* Rate：无风险利率，默认为0.02
* SlidePrice：滑价，默认为0
* PriceLoc：市价单成交位置：0-当前bar收盘价；1-下一个bar开盘价；2-下一个bar第二个tick;n-下一个bar第n个tick;默认为1，即下一个bar的开盘价；
* DealType：市价单成交类型：0-成交价；1-对方最优价；2-己方最优价；默认0
* LimitType：限价单成交方式：0-直接成交；1-下一个bar内没有该价格时，撤单处理；默认0

示例：

* 在回测时设置初始资本1000000元、手续费率0.0025、无风险利率0.02、滑价0、默认1下一个bar的开盘价、默认0成交价、默认0直接成交
* 则输入为：

```Matlab
traderSetBacktest(1000000,0.0025,0.02,0,1,0,0);
```

* 回测账户设置，对AccountList入参，根据标的选择期货（FutureBackReplay）或证券回测账号（StockBackReplay）

示例：

* 针对期货策略进行回测：

```Matlab
AccountList(1) = {'FutureBackReplay'};
```

* 回测启动设置，使用traderRunBacktest对策略执行回测。

```matlab
traderRunBacktest(StrategyName,TradeFun,varFunParameter,AccountList,TargetList,KFrequency,KFreNum,BeginDate,EndDate,FQ,AlgoTradeFun,varAlgoFunParameter)
```



*输入参数：*

* StrategyName：策略名称，字符串类型
* TradeFun：策略函数，格式：@函数名称
* varFunParameter：策略函数中用到的参数
* AccountList：账户名称，cell 型
* TargetList：策略标的列表，为结构体类型，格式为：
* Market ：市场类型，字符串格式
* Code：交易品种代码，字符串格式，如'000002'
* KFrequency：K线类型的整型，如 day, min
* KFreNum：频率
* BeginDate：开始日期，整型，如20140608
* EndDate：结束日期，整型，如20140701
* FQ：复权类型，'NA'为不复权，'FWard'向前复权，'BWard'向后复权
* AlgoTradeFun：算法交易函数，格式：@算法交易函数
* varAlgoFunParameter:算法交易函数中用到的参数

示例：

* 对策略strategy回测，策略参数为{var1,var2,var3}，回测时间区间为2015年3月份，频率为1分钟,期货回测

```matlab
AccountList(1) = {'FutureBackReplay'};
```

```matlab
traderRunBacktest('strategy',@strategy,{var1,var2,var3},AccountList,TargetList,'min',1,20150301, 20150331,'FWard');
```

* 对策略strategy回测，策略参数为{var1,var2,var3}，回测时间区间为2015年3月份，频率为1分钟,股票回测，行情数据前复权

```matlab
AccountList(1) = {'StockBackReplay'};
```

```matlab
traderRunBacktest('strategy',@strategy,{var1,var2,var3},AccountList,TargetList,'min',1,20150301, 20150331,'FWard');
```



3. 绩效报告

绩效报告以高效的计算方法展现给用户包括交易资料、周期分析、策略分析、交易分析四大维度，五十多个指标，让用户快速了解自己策略的业绩，优化参数，反复验证。

### AT 策略构建

1. **策略操作逻辑**

Auto-Trader的策略操作主要由两部分构成：

* 策略主函数的Function脚本，内容包括策略的主函数，输入参数，计算逻辑和对句柄和数据的设置等；
* 操作执行函数的Script脚本，分为回测、回放、交易和参数优化四种，每一种都对应一个对策略主函数的操作调用，操作函数在使用时都需要单独进行设置，包括对策略主函数中内置参数的提前赋值，以及操作函数自身的参数设置。

![策略逻辑](http://www.digquant.com.cn/data/attachment/portal/201705/17/103746wlp7gfjowow5wfjw.png)

例如，创建了一个Function脚本，在其上进行策略AmaTrade的编写，完成后将该Function脚本改名为AmaTrade，若需要对策略AmaTrade进行回测操作，只需另行创建一个Script脚本，配置AmaTrade内的参数，调用traderRunBacktest函数，在traderRunBacktest函数中输入策略AmaTrade的信息与相关参数后，运行该脚本，即进入对AmaTrade的回测中，回测报告将展示在Auto-Trader终端中。同理回放与交易函数亦如此操作。

![逻辑界面](http://www.digquant.com.cn/data/attachment/portal/201705/17/103840kyhyqmzoh5yhqhof.png)

Auto-Trader开始进入回测状态

![回测界面](http://www.digquant.com.cn/data/attachment/portal/201705/17/103924f44hw4ow90fye6h4.png)



2. **新建策略**

以下为策略主函数的输入参数示范模板，实际应用中不需要严格参照本模板。更多策略示例，可参照Auto-Trader安装目录下的example策略模板。



**Function StrategyName(输入参数)**

```matlab
%----------策略初始化与是否日内平仓设置----------%

traderDailyCloseTime(145000);   %每天14：50平仓，若不需要日内平仓可不设置

targetList = traderGetTargetList(); 

%获取交易标的信息(可在回测文件中设置)，存入targetList，包括所在市场（market）以及代码(code)

HandleList = traderGetHandleList();  %获得账户句柄信息

marketposition=traderGetAccountPosition(HandleList(1),targetList(1).Market,targetList(1).Code); 

%根据targetList，HandleList中的信息获得该账户持仓情况

[BarNumber,BarTime,BarOpen,BarHigh,BarLow,BarClose,BarVolume,BarTurnOver,BarOpenInterest]=traderGetCurrentBar(targetList(1).Market,targetList(1).Code);  

%获取当前Bar的信息，可根据当前Bar的情况设置是否开仓

[name,lastTD,Multiple,MinMove,TradingFeeOpen,TradingFeeClose,TradingFeeCloseToday,LongMargin,ShortMargin] = traderGetFutureInfo(targetList(1).Market,targetList(1).Code);  %获取期货的基本信息

 

%----------提取策略所需数据----------%

[time,open,high,low,close,volume,turnover,openinterest]=traderGetKData(Market,Code,KFrequency,KFreNum,BeginDate,EndDate,FilledUp,FQ);  %根据策略逻辑需要，在策略读取所需的Bar数据，从而进行后续的计算

[time,price,volume,volumetick,openinterest,bidprice1,bidvolume1,askprice1,askvolume1]=traderGetTickData(Market,Code,Date);   %根据策略逻辑需要，在策略读取所需的Tick数据，从而进行后续的计算

 

%----------策略内部计算与基本逻辑----------%

%策略内部的参数计算或条件判断

 

%----------策略主体，交易逻辑判断----------%

traderBuy(Handle,Market,Code,Contracts,Price,PriceType,OrderTag);

%买入下单，若初始有空头持仓，则先平仓，再买入

traderSell(Handle,Market,Code,Contracts,Price,PriceType,OrderTag);

%卖出平仓下单

traderSellShort(Handle,Market,Code,Contracts,Price,PriceType,OrderTag);

%卖出下单，若初始有多头持仓，则先平仓，再卖出

traderBuyToCover(Handle,Market,Code,Contracts,Price,PriceType,OrderTag);

%买入平仓下单

traderDirectBuy(Handle,Market,Code,Contracts,Price,PriceType,OrderTag);

%买入下单，影响初始持仓

traderDirectSell(Handle,Market,Code,Contracts,Price,PriceType,OrderTag);

%卖出下单，影响初始持仓

traderPositionTo(Handle,Market,Code,Position,Price,PriceType,OrderTag);

%以仓位为目标，直接调整至某仓位，可双方向调整
```



以双均线策略为例：

![双均线策略](https://www.digquant.com.cn/data/attachment/portal/201705/17/152953nfaiotk6moupd6zb.png)



### 如何使用 AT 进行简单的策略回测

1. **开启 Matlab**

Auto-Trader Pro策略研究是基于Matlab平台对策略进行编写以及分析，点击“菜单栏”中“MATLAB”按键，开启Matlab平台。

正常情况下，Matlab安装完毕后，点击按键即可打开Matlab。若点击出现无反应，或弹出提醒、错误窗口，可能是您未完成matlab的正常安装，或未设置matlab的系统变量。

Matlab系统变量设置方法：开始→控制面板→系统→高级系统设置→高级→环境变量，在系统变量中找到变量“Path”，点击“编辑”，在弹出的“编辑系统变量”栏里，加上“;”，将Matlab.exe所在的目录路径，即Matlab安装路径添加进去，确定即可。

![环境变量](http://www.digquant.com.cn/data/attachment/portal/201703/06/170744iuc7600sjzrt2pkk.png)

2. **了解 AT 策略组成**

Auto-Trader的策略操作主要有两部分构成：

①*策略主函数*：内容主要包括策略所需用到的参数，对参数的计算以及策略逻辑体现

②*策略执行函数*：包含策略中所需要的参数，例如需要作用的标的以及时间区间等参数，以及定义被调用的策略主函数是用以回测或者模拟实盘。

![策略界面](http://www.digquant.com.cn/data/attachment/portal/201703/06/170854ntnw2dn2ngjjdvqx.png)



3. **编写回测策略主文件结构**

```matlab
Function StrategyName(bInit,bDayBegin,cellPar) %定义策略函数的名称

%括号内输入的参数为固定结构，其中cellPar为策略执行函数入参参数。

% bInit是策略运行时的initialize，在策略逻辑运行前为1，当开始判断是否下单后，该变量为0.

% bDayBegin 在一天的第一根Bar为1，其他时刻为0

 

%外部和全局参数声明（这是一个固定结构）

global g_idxKDay; %申明日频或者分钟频率的数据index           

    global g_idxSignal; %申明因子

   

%初始化回测帐户

    if bInit

        traderSetParalMode(false);%默认是true，因子计算函数并行执行，速度快，但是不能调试，false串行执行可以设断点调试

        g_idxKDay = traderRegKData('day',1); %只有注册之后才能获取数据。分钟数据的获取方法为 traderRegKData('min',1)。后面的数字是刷新频率。

        g_idxSignal = traderRegUserIndi(@getSignal,{g_idxKDay,cellPar的入参});

        TLen = length(g_idxKDay(:,1));

 

%交易逻辑

    else

        %----------策略内部计算与基本逻辑----------%

%策略内部的参数计算或条件判断

 

% ----------策略主体，交易逻辑判断----------%

traderBuyV2(HandleIdx,TargetIdx,Contracts,Price,PriceType,OrderTag);

%买入下单，若初始有空头持仓，则先平仓，再买入

traderSellV2(HandleIdx,TargetIdx,Contracts,Price,PriceType,OrderTag);

%卖出平仓下单

traderSellShortV2(HandleIdx,TargetIdx,Contracts,Price,PriceType,OrderTag);

%卖出下单，若初始有多头持仓，则先平仓，再卖出

traderBuyToCoverV2(HandleIdx,TargetIdx,Contracts,Price,PriceType,OrderTag);

%买入平仓下单

traderDirectBuyV2(HandleIdx,TargetIdx,Contracts,Price,PriceType,OrderTag);

%买入下单，影响初始持仓

traderDirectSellV2(HandleIdx,TargetIdx,Contracts,Price,PriceType,OrderTag);

%卖出下单，影响初始持仓

TraderPositionToV2(HandleIdx,TargetIdx,Position,Price,PriceType,OrderTag);

%以仓位为目标，直接调整至某仓位，可双方向调整

 

% 计算因子的自定义函数

function value=getSignal(cellPar,bpPFCell)

%调用该函数的参数将会全部被赋给cellPar

%bpPFCell为一个时间序列，标记特定的刷新时刻

%参数声明

%函数计算，计算出来的结果可用于交易逻辑的判断
```



4. **编写策略执行文件**

```matlab
Code2 = {'IC0000', 'IF0000'};

m=1;

for j = 1:length(Code2)

    targetList(m).Market  = 'CFFEX';

    targetList(m).Code  =  Code2{j};

    m = m+1;

end

 

%---------定义变量----------% 

%定义策略主函数中所要入参cellPar中的变量                 

 

%指定操作的账户，例如以下为期货模拟账户

AccountList(1) = {'FutureSimAcc'};

 

%回测

%设置回测参数，设置InitialCash初始资本，Costfee手续费率，Rate无风险利率，SlidePrice滑价，DealType市价单成交类型，LimitType限价单成交方式。

traderSetBacktest(InitialCash,Costfee,Rate,SlidePrice,PriceLoc,DealType,LimitType);

 

%启动回测

traderRunBacktestV2(StrategyName,TradeFun,varFunParameter,AccountList,TargetList,KFrequency,KFreNum,BeginDate,EndDate,FQ,AlgoTradeFun,varAlgoFunParameter);
```



5. **运行策略，进行回测**

策略（包括策略主函数以及策略执行函数）完成后，保存策略。在MATLAB端打开策略执行文件，点击运行：

![策略运行](http://www.digquant.com.cn/data/attachment/portal/201703/06/171258l70ttjk2a2tlknxk.png)

MATLAB端命令窗口会显示：

![命令窗口](http://www.digquant.com.cn/data/attachment/portal/201703/06/171344kk19zwuu32u4ig9n.png)

返回到Auto-Trader客户端显示回测正在进行：

![回测界面](http://www.digquant.com.cn/data/attachment/portal/201703/06/171423f4i7p3vluf7xev7b.png)



6. **完成回测，查看绩效报告**

回测完成后显示对该策略的绩效报告：

![绩效报告](https://www.digquant.com.cn/data/attachment/portal/201705/17/155049xr1c3ko91zhhixt1.png)



----



## 本周目标2：MATLAB策略编程

1. 熟悉MATLAB语法
2. 熟悉如何使用MATLAB编写策略
3. 了解如何评价策略

### 简答数据类型

#### 1.1 实数和虚数

类型： uint64/double/single/int8/int16/int32/int64/unit8/uint16/uint32

类型之间直接转换

```matlab
int32(1.1)
```

判断是否为某种类型

```matlab
isa(temp,'double')
```

虚数的表示如 赋值2i给a 就是

```matlab
 >> a = 2i;
```

或

```matlab
>> a = 2j;
```

单个数字的共轭加‘

```matlab
>> b = a';
```

查找相关方法：

```matlab
>> methods('int32');
>> methods(11);
```

注意:

1. i或j前面直接加数字表示虚数，但是i和j前面不加数字也可以用来表示其他变量。虚数表达不需要加*
2. isa(variable,type)判断某个变量是否为某种类型
3. methods(’int32’).查找某种数据类型的所有可调用的函数。注意直接写类型名字的时候要加引号，或者直接改为某种类型下的一个实例。

#### 1.2 向量(数组)

一维数值数组。MATLAB 允许你创建列向量和行向量，列向量通过在方括号[]内把数值用分号(行向量用逗号或空格）隔开来创建，对元素的个数没有限制。

列向量

```matlab
>> a = [2; 1; 4];
```

行向量

```matlab
>> a = [2, 1, 4];
```

数量乘法: 把一个向量的每个元素乘上一一个数。
方法：直接在[]外面乘上一个数，或变量直接乘上一个数。

```matlab
>> new_vector = vector*const;
```

转置：

```matlab
>> new_vector = transpose(vector);
```

共轭转置：用’表示（如果向量元素均为实数，共轭转置和transpose的效果一样）

```matlab
>> new_vector = vector‘;
```

共轭不转置：conj

```matlab
>> new_vector = conj(vector);
```

向量加减： 只有相同长度的行之间或列之间可以加减。行和列之间不能直接加减（可转置后操作）。

```matlab
>> new_vector = vector1 - vector2;
```

向量元素乘除： 同上要求，但需要在运算符号前加.

```matlab
>> new_vector = vector1 .* vector2;
```

向量平方等:注意前面加.

```matlab
>> new_vector = vector1.^2;
```

向量点乘：dot

```matlab
>> new_vector  = dot( vector1,vector2);
```

向量合并：（同为行直接逗号，同为列；）

```matlab
>> new_vector  = [vector1,vector2];
```

等差序列：

(1) 从1开始每隔.1生成一个元素，元素的最大值为2

```matlab
>> new_vector = [1:.1:2];
```

(2) 从1开始到2输出10个等差序列，使得最小值为1，最大值为2

```matlab
>> new_vector = linspace(1,2,10);
```

(3) 对数值从1开始到2输出10个对数值等差序列，使得最小对数值为1，最大对数值为2

```matlab
>> new_vector = logspace(1,2,10);
%或者
>> new_vector = 10.^(linspace(1,2,10));
```

长度：

```matlab
>> len = length(vector);
```

最大值：max,类似还有min,sum,sqrt,std,mean,abs等

```matlab
>> max_value = max(vector);
```

是否包含某元素：

```matlab
>> ismember(element,vector);
```

数组交集

```matlab
>> intersect(vector1,vector2);
```

数组并集

```matlab
>> union(vector1,vector2);
```

数组相邻求差值，结果与原数组少一个元素

```matlab
>> diff(vector);
```

复制

```matlab
>> repmat(a,[2,3]); 
%将a行方向复制两次，列方向复制3次
```

注意:

1. Matlab识别中英文输入法，分号等需要在英文输入法下键入，否则报错。
2. 每个执行命令后面加入分号的目的是不输出结果。如果不写分号，在每次执行命令之后会把执行结果在执行界面显示。

#### 1.3 特殊数组

```matlab
a = zeros(3,4) %3行4列 
b = zeros(4) %只有一个参数时，生成二维数组 
c = zeros(4,1) 
d = zeros(3,4,5); %多维数组
a = ones(2) %全 1 
b = eye(2) %对角 1 
c = rand(2) % [0,1] 均匀分布随机数 
d = randn(2) %正态分布随机数 
e = false(2) %生成值全为1(true)或0(false) 的逻辑数组 %MATLAB 中，对逻辑数组的判断只有0和非0两种结果，非0的数一律认为是true 
f = nan(2) %生成值全为 NaN 的数组
```

#### 1.4 矩阵的复制 repmat

```matlab
a = [1 2;3 4] 
disp('[a a a;a a a] = ') 
disp([a a a;a a a]) 
disp('repmat(a,2,3) = ') 
disp(repmat(a,2,3)) %按行复制 2 次，按列复制 3 次
```

$\bf{注意:}$

1. disp表示输出元素

#### 1.5 Kronecker 乘积

```matlab
     %C = kron(A,B)，用 A 的每个元素乘以 B 矩阵，然后按 A 的元素顺序排列 
     a = [1 2;3 4] 
     b = ones(2,3) 
     disp('kron(a,b) = ') 
     disp(kron(a,b)) 
     disp('kron(b,a) = ') 
     disp(kron(b,a)) %repmat 可以用 kron 代替
```

#### 1.6 获取元素

一维数组

```matlab
    a = rand(1,8)
    disp('a(1:2:end) = ') %end 表示最后一个元素，对于步长不为 1 的情况，如果不能整除，也不会报错
```

高维数组

```matlab
    a = rand(4,5) 
    disp('a(3,4) = ') 
    disp(a(3,4)) 
    disp('a(3,:) = ') 
    disp(a(3,:)) 
    disp('a(:,[2,4]) = ') 
    disp(a(:,[2,4]))
```

#### 1.7 删除数组元素

```matlab
    a = zeros(4,5); 
    for i = 1:numel(a) 
        a(i) = i; 
    end 
    a 
    a(3,:) = []; 
    disp('a(3,:) = [];') 
    a 
    a(1) = []; %对多维数组，如果 a(1) = []，将破坏多维结构 
    disp('a(1) = [];') 
    a
```

#### 1.8 排序sort

```matlab
    %[Y,I] = sort(X,dim,mode) 
    %mode: 'ascend' 升序 'descend' 降序，默认前者 
    %dim: 按第几维排序，默认是 1，注意对矩阵，第 1 维是列，第 2 维是行。但对一维数组来说，默认只对那一维排序 
    %如果 X 是一维数组，那么 X(I) = Y，即 Y 为对 X 重新排列后的数组 
    %如果 X 是多维数组，那么对于第 dim 维的每个子数组，X 对应在 I 上的取值就是 Y
    a = rand(1,8) 
    disp('[s,i] = sort(a)') 
    [s,i] = sort(a) %这里的排序其实按第 2 维 
    disp('a(i) = ') 
    disp(a(i)) 
    b = rand(4,5) 
    disp('[~,i1] = sort(b(:,2),''descend'');') 
    [~,i1] = sort(b(:,2),'descend'); 
    disp('c = b(i1,:)') c = b(i1,:) %把所有的列按第二列降序排序
```

注意:

1. %后面为注释，不执行
2. ~在表示获取位置的数据不读取
3. i1也代表一个可赋值的变量. 变量名区分大小写，以英文字符开始，之后可以使用字母、数字或下划线但不能使用空格和标点符号，名字长度不超过31、

#### 1.9 查找满足条件的坐标 find

```matlab
    clear 
    clc 
    a = rand(1,8) 
    disp('a>0.5') 
    disp(a>0.5) %逻辑数组的返回结果是和 a 维度一样的矩阵 
    disp('find(a>0.5)') 
    disp(find(a>0.5)) 
    disp('find(a>0.5,1,''last'')') 
    disp(find(a>0.5,1,'last')) %返回符合条件的前n个元素，n后面可跟 'first' (默认) 或者 'last' 表示从后往前找符合条件的元素 
    disp('a(a>0.5)') 
    disp(a(a>0.5)) 
    disp('a(find(a>0.5))') 
    disp(a(find(a>0.5))) %a(find(表达式))建议直接写为 a(表达式)，效率更高
```

注意:

1. clear 表示所有的赋值清空
2. clc表示界面输出清空

#### 1.10 满足条件的赋值

```matlab
    disp('a(a>0.5) = 0') 
    a(a>0.5) = 0
```

#### 1.11 空格相关

```matlab
    b = blanks(5) %返回5个空格的字符串 
    c = ' test ' 
    disp('deblank(c)') 
    disp(deblank(c)) %去除末尾空格 
    disp(char(10)) 
    disp('strtrim(c)') 
    disp(strtrim(c)) %去除头尾空格 
    disp(char(10)) 
    disp('isspace(c)') 
    disp(isspace(c)) %判断字符串的每个元素是否是空格 
    disp('isletter(c)')
```

#### 1.12 字符串相关

```matlab
    clear 
    clc 
    c = ' test ' 
    ischar(c)  %判断是否为字符串
    disp(isletter(c)) %判断字符串的每个元素是否是字母
    a = 'Thank you ' 
    b = 'very much' 
    disp('[a b] = ') 
    disp([a b]) 
    disp(char(10)) 
    disp('strcat(a,b)') 
    disp(strcat(a,b)) %去除字符串后面的空格
```

#### 1.13 字符串查找与替换

```matlab
    %findstr 在未来的 MATLAB 中将消失，请用 strfind 
    clear 
    clc 
    s = ' How much wood would a woodchuck chuck? ' 
    disp('strfind(s,''a'')') 
    disp(strfind(s,'a')) %被查找的一定要写在前面 
    disp('strfind(''a'',s)') 
    strfind('a',s) 
    disp('strfind(s,''wood'')') 
    disp(strfind(s,'wood')) 
    disp('strfind(s,''Wood'')') %区分大小写 
    strfind(s,'Wood') 
    disp('strrep(s,'' '',''\'')') 
    disp(strrep(s,' ','\')) %字符串替换，不改变原始字符串
```

#### 1.14 instr从特定位置开始查找

```matlab
    %类似 Excel 的 instr 函数 
    %instr(开始位置，从哪里找，找什么) 
    %从 from 里面，找从 pos 开始的第一个 what 所在的位置
    clear 
    clc 
    s = ' How much wood would a woodchuck chuck? ' 
    disp('instr(1,s,''wood'')') 
    disp(instr(1,s,'wood')) 
    disp('instr(5,s,''wood'')') 
    disp(instr(5,s,'wood'))
```

#### 1.15 字符串比较

```matlab
    clear 
    clc 
    a = 'Thank you very much' 
    b = 'thank you very much' 
    c = 'thank you' 
    disp('strcmp(a,b)') 
    disp(strcmp(a,b)) 
    disp('strcmpi(a,b)') 
    disp(strcmpi(a,b)) %不区分大小写 
    disp('strncmp(a,c,5)') 
    disp(strncmp(a,c,5)) %比较前5个字符 
    disp('strncmpi(a,c,5)') 
    disp(strncmpi(a,c,5)) %不区分大小写
```

#### 1.16 字符串转换

```matlab
    clear 
    clc 
    a = 'Thank' 
    disp('lower(a) = ') 
    disp(lower(a)) 
    disp(char(10)) 
    disp('upper(a) = ') 
    disp(upper(a)) 
    a = '123' 
    disp('b = str2num(a)') 
    b = str2num(a) 
    disp('c = num2str(b)') 
    c = num2str(b)
```

#### 1.17 字符串调用函数

```matlab
    clear
    clc
    a = [1,2,3]
    c = str2func('max')
    c(a)%输出3
```

#### 1.18 把字符串当命令执行 eval

```matlab
    a = [1,2,3];
    eval('max(a)')
```

#### 1.19 矩阵求本征值和本征向量

```matlab
    %det：行列式 
    %inv：逆运算 
    %pinv：伪逆运算（对于病态矩阵） 
    %sqrtm：求平方根 
    %[V,D] = eig(A)：D 特征值，V 特征向量 
    %norm：范数(1,2,inf,'fro')，默认为2 
    %cond：条件数 
    clear 
    clc 
    a = magic(4) 
    disp('[v,d] = eig(a)') 
    [v,d] = eig(a)
```

#### 1.20 逻辑运算

```matlab
    a = [true,false,true,true,false] 
    b = [true,false,true,false,true] 
    disp('a&b') 
    disp(a&b) %或 and(a,b)：两个数组中相同位置的值都非 0 时返回 1，否则返回 0 
    disp('a|b') 
    disp(a|b) %或 or(A,B)：两个数组中相同位置的值都为 0 时返回 0，否则返回 1 
    disp('~a') 
    disp(~a) %对数组中的元素取反，非 0 变 0，0 变 1 
    disp('xor(a,b)') 
    disp(xor(a,b)) %两个数组中相同位置的值只有一个非 0 时返回 1，否则返回 0 
    disp('any(a)') 
    disp(any(a)) 
    disp('all(a)') 
    disp(all(a)) 
    c = 5 
    disp('c>0 && c<3') 
    disp(c>0 && c<3) %% 两端必须是逻辑变量或者表达式，连逻辑数组都不行，返回值也是逻辑变量
```

#### 1.21 语句

if语句

```matlab
    clear 
    clc 
    a = 1; 
    if a>1 
        disp('a>1') 
    elseif  a =  = 1 
        disp('a =  = 1') 
    else 
        disp('a<1') 
    end
```

switch语句

```matlab
    clear 
    clc 
    b = 'orange'; 
    switch b %可比较字符串 %这里不会依次执行，如果判断成功，会自动 break 
        case 'apple' 
            disp('apple') 
        case 'orange' 
            disp('orange') 
        case 'pineapple' 
            disp('pineapple') 
        otherwise 
            disp('other') 
    end
```

while语句

```matlab
    clear 
    clc 
    k = 0; 
    while true 
        k = k+1 
        if k>3 
            break %continue 和 break 对 for 和 while 均有效 
        end 
    end %return 结束此程序
```

### 其他数据类型

#### 1.1 cell类型

类似数组，但是其元素不像数组一样限制为数，cell类型的元素可以是数、数组或其他cell。数组的构建是在外面加[],而cell是{}.

```matlab
    >> a = {[1,2],[2,3,4],4};
    >> c = {a, 4};
```

下面的代码在数组报错

```matlab
    >>  b = [[2,3],[2;3],4]% Error using horzcat; Dimensions of matrices being concatenated are not consistent.
```

在cell中正确执行

```matlab
    >>  b = {[2,3],[2;3],4}
```

查看某个元素类型

```matlab
    >> a(1) %[1x2 double]
```

查看某个元素详细内容

```matlab
    >> a{1} %1     2
```

访问某个元素内的某些数据

```matlab
    >> a{1}(1:2) %访问的是A中的第一个cell里面内容1-2的数据
```

删除某个序号

```matlab
    >> a(1)=[];%不能使用cell{1}=[],这是把第一个cell内容置空没有删除
    >> a(:)=[] %删除所有的cell,其他的删除一次类推
```

m行n列的cell类型

```matlab
    >> A = cell(m，n)
```

内容显示

```matlab
    >> celldisp(A)  % 完全显示细胞型变量的内容  
```

注意：

1. ()是输出第几个元素的类型，{}是输出第几个元素的具体内容

#### 1.2 结构类型（struct）

结构体的特点是一个变量可以有属性（或字段），而且有很简单的方法去调用这个属性或字段。

比如 一个班有53个学生，每个学生的属性有 年龄，性别，名字等，在Matlab中

```matlab
    clear all
    clc
    student(1).name = '张三'
    student(1).age = 15
    student(1).sex = 'boy'
    student(2).name = '张四'
    student(2).age = 16
    student(2).sex = 'boy'
    ,,,
```

上面就是给第一和第二个学生分别赋值了名字、年龄、性别信息、 此时student便是结构类型，每个元素都有属性可以调用。 属性的赋值可以是任何类型。

其他赋值方法。

```matlab
    % sturct('field1',values1,'field2',values2,…)其中field是字段
    a = struct('name',{'张三','张四'},'age',{15，16},'sex',{'boy','boy’});
```

删除特定属性

```matlab
    rmfield(a,'sex') 
```

一个例子

```matlab
    targetList(1).Market  =  'SHFE';
    targetList(1).Code  =  'RB0000';
    targetList(2).Market  =   'DCE';
    targetList(2).Code  = 'JM0000';
```

注意：

1. 注意下面的field需要加引号,，而且多个长度时用cell储存
2. struct也可以组成矩阵。 new_struct = [struct1 ; struct2];

#### 1.3 struct 和 cell的转换

struct转成cell，实际上是指struct每个元素的所有元素输出为一个cell。

```matlab
    a = struct('name',{[1,2],'张四'},'age',{15,16},'sex',{'boy','boy'});
    b = struct2cell(a)
```

cell转成struct需要指明属性的名字

```matlab
    c = cell2struct(b,{'name','age','sex'})
```

### Matlab 绘图

#### 1.1 简单绘图

```matlab
    x = -pi:0.1:pi; y = sin(x); z = 10*cos(x); plot(x,y)
```

plot参数

```matlab
    plot(x,y,'--ro','LineWidth',2,... %线宽 
        'MarkerEdgeColor','k',... %标记的边框颜色 
         'MarkerFaceColor','k',... %标记的填充色 'MarkerSize',4) %标记的大小
    %plot(x1,y1,LineSpec,'PropertyName',PropertyValue) 
    %LineSpec： 
    %- 实线，-- 虚线，: 点线，-. 点划线 
    %+ 加号，o 圆圈，* 星号，. 点，x 十字，s 方块，d 菱形，^ 向上三角形，v向下三角形，>向右三角形，<向左三角形，p五角星，h六角形 
    %r 红色，g 绿色，b 蓝色，c 青色，m 品红，y 黄色，k 黑色，w 白色 
    %也可以用编辑图的方法来实现 plottools
```

注意:

1. …在语句结尾指的是另起一行. 另起一行的内容与前面合在一起算一个语句
2. plot可以每两个（自变量、因变量）把多个图放在一起

#### 1.2 其它图形

散点图

```matlab
    scatter(x,y)
```

三维网格图

```matlab
    [X,Y] = meshgrid(-8:0.5:8); %生成网格矩阵 
    R = sqrt(X.^2 + Y.^2); 
    Z = sin(R)./R; 
    mesh(X,Y,Z)
```

直方图： hist(x)

曲面图: surf(x,y,z)

柱状图： bar(x)

面积图： area(x)

多图叠加：

```matlab
    plot(x,y) 
    hold on %后续图形叠加 
    scatter(x,y) 
    hold off %结束叠加，输出图形 
    %bar3：三维柱状图 %pie/pie3：饼图/三维饼图 %scatter3：三维散点图
```

多个图形在一个图上分别画出：

```matlab
    subplot(2,2,1) 
    %subplot(m,n,p)： m：拆成多少行，n：拆成多少列，p：当前输出位置（先按行后按列，与数组的定位方式不同） 
    plot(x,y) 
    subplot(2,2,2)； plot(x,z) 
    subplot(2,2,3)； plot(x,y+z) 
    subplot(2,2,4)； plot(x,y-z) 
    %先使用 subplot，再使用 plot，无需 hold on/off %关闭图形窗口结束当前 subplot
```

----



### 函数

#### 函数

函数是一组语句一起执行任务。在MATLAB中，函数定义在单独的文件。文件函数的文件名应该是相同的。

函数操作在自己的工作空间，它也被称为本地工作区，独立的工作区，在 MATLAB 命令提示符访问，这就是所谓的基础工作区的变量。

函数可以接受多个输入参数和可能返回多个输出参数

函数语句的语法是：

```matlab
function [out1,out2, ..., outN] = myfun(in1,in2,in3, ..., inN)
```

例子：

下面的函数名为mymax，应当书面，在一个文件名为mymax.m。它需要五个数字作为参数并返回最大的数字。

创建函数文件，名为mymax.m 并输入下面的代码：

```matlab
function max = mymax(n1, n2, n3, n4, n5)
%This function calculates the maximum of the
% five numbers given as input
max =  n1;
if(n2 > max)
    max = n2;
end
if(n3 > max)
   max = n3;
end
if(n4 > max)
    max = n4;
end
if(n5 > max)
    max = n5;
end
```

一个函数的第一行以 function关键字开始。它给出了函数的名称和参数的顺序。在我们的例子中，mymax 函数有5个输入参数和一个输出参数。

注释行语句的功能后提供的帮助文本。这些线条打印，当输入：

```matlab
help mymax
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
This function calculates the maximum of the
five numbers given as input
```

可以调用该函数为：

```matlab
mymax(34, 78, 89, 23, 11)
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
ans = 89
```

----



### 匿名函数

#### 匿名函数

一个匿名的函数就像是在传统的编程语言，在一个单一的 MATLAB 语句定义一个内联函数。它由一个单一的 MATLAB表达式和任意数量的输入和输出参数。

可以定义一个匿名函数在MATLAB命令行或在一个函数或脚本。

这种方式，可以创建简单的函数，而不必为他们创建一个文件。

创建一个匿名函数表达式的语法

```matlab
f = @(arglist)expression
```

在这个例子中，我们将编写一个匿名函数名为 power，这将需要两个数字作为输入并返回第二个数字到第一个数字次幂。

创建一个脚本文件，并键入下面的代码：

```matlab
power = @(x, n) x.^n;
result1 = power(7, 3)
result2 = power(49, 0.5)
result3 = power(10, -10)
result4 = power (4.5, 1.5)
```

当您运行该文件时，它会显示：

```matlab
result1 = 343
result2 = 7
result3 = 1.0000e-10
result4 = 9.5459
```

----

### M 文件

#### M文件

MATLAB允许写两个程序文件：

- 脚本 - 脚本文件 .m 扩展程序文件。在这些文件中写的一系列命令，想一起执行。脚本不接受输入和不返回任何输出。他们在工作区中的数据操作。
- 函数 -函数文件 .m 扩展程序文件。函数可以接受输入和返回输出。内部变量是本地的函数。

可以使用MATLAB 编辑器或其他任何文本编辑器来创建 .m 文件。在本节中，我们将讨论的脚本文件。 MATLAB 命令和函数调用的脚本文件包含多个连续的行。可以运行一个脚本，在命令行中键入其名称。

**创建并运行脚本文件**

创建脚本文件，需要使用文本编辑器。可以打开 MATLAB 编辑器，可使用两个方法：

使用命令提示符

使用IDE

如果是在命令提示符下使用命令提示符下，键入编辑。这将打开编辑器。可以直接键入编辑，然后在文件名（ .m 扩展程序文件名）

```matlab
edit 
Or
edit 
```

上面的命令将在默认情况下，MATLAB 目录中创建文件。如果想存储在一个特定的文件夹中的所有程序文件，那么一定要提供整个路径。

让我们创建一个文件夹名为 progs。在命令提示符处键入以下命令（>>）：

```matlab
mkdir progs    % create directory progs under default directory
chdir progs    % changing the current directory to progs
edit  prog1.m  % creating an m file named prog1.m
```

如果首次创建的文件，MATLAB 会提示您进行确认。单击“Yes”。

另外，如果使用的是IDE，选择 NEW -> Script。这也打开编辑器，并创建一个文件名为命名。输入代码后可以命名并保存文件。

在编辑器中输入下面的代码：

```matlab
NoOfStudents = 6000;
TeachingStaff = 150;
NonTeachingStaff = 20;
Total = NoOfStudents + TeachingStaff ...
    + NonTeachingStaff;
disp(Total);
```

创建和保存文件后，可以运行在两个方面：

编辑器窗口中单击“Run”按钮或

只要在命令提示符下键入文件名（不含扩展名）：>> prog1

命令窗口提示显示的结果是：

```matlab
6170
```

**例子：**
创建一个脚本文件，然后输入下面的代码：

```matlab
f = exp(-d)
```

上面的代码编译和执行时，它会产生以下结果：

```matlab
c = 12
d = 12.6570
e = 63.2849
f = 3.1852e-06
```

----

### 变量

#### 变量

在MATLAB环境下，每一个变量是一个数组或矩阵。

在一个简单的方法，您可以指定变量。例如，

```matlab
x = 3           % defining x and initializing it with a value
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
x = 3
```

它创建了一个1-1的矩阵名为x和的值存储在其元素。让我们查看另一个例子，

```matlab
x = sqrt(16)     % defining x and initializing it with an expression
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
x = 4
```

请注意：

一旦一个变量被输入到系统中，你可以引用它。

变量在使用它们之前，必须有值。

当表达式返回一个结果，不分配给任何变量，系统分配给一个变量命名ans，以后可以使用。

例如，

```matlab
sqrt(78)
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
ans = 8.8318
```

可以使用这个变量 ans:

```matlab
9876/ans
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
ans = 1.1182e+03
```

让我们来看看另一个例子：

```matlab
x = 7 * 8;
y = x * 7.89
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
y = 441.8400
```

#### 多个赋值

可以有多个任务在同一行。例如，

```matlab
a = 2; b = 7; c = a * b
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
c = 14
```

#### 我已经忘记了变量！？

who 命令显示所有已经使用的变量名。

```matlab
who
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
Your variables are:
a    ans  b    c    x    y  
```

whos 命令显示多一点有关变量：

当前内存中的变量

每个变量的类型

内存分配给每个变量

无论他们是复杂的变量与否

```matlab
whos
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
 Name      Size            Bytes  Class     Attributes
  a         1x1                 8  double              
  ans       1x1                 8  double              
  b         1x1                 8  double              
  c         1x1                 8  double              
  x         1x1                 8  double              
  y         1x1                 8  double     
```

clear命令删除所有（或指定）从内存中的变量（S）。

```matlab
clear x     % it will delete x, won't display anything
clear         % it will delete all variables in the workspace
             %  peacefully and unobtrusively 
```

#### 格式命令

默认情况下，MATLAB 四个小数位值显示数字。这就是所谓的 short format.

但是，如果想更精确，需要使用 format 命令。

长(long ) 命令格式显示小数点后16位。

例如：

```matlab
format long
x = 7 + 10/3 + 5 ^ 1.2
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
x = 17.2320
```

空格格式命令回合到小数点后两位数字。例如，

```matlab
format bank
daily_wage = 177.45;
weekly_wage = daily_wage * 6
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
weekly_wage = 1064.70
```

MATLAB 显示大量使用指数表示法。

短格式e命令允许以指数的形式显示小数点后四位，加上指数。

例如，

```matlab
format short e
4.678 * 4.9
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
ans = 2.2922e+01
```

format long e命令允许以指数的形式显示小数点后四位，加上指数。例如，

```matlab
format long e
x = pi
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
x = 3.141592653589793e+00
```

format rat 格式大鼠命令给出最接近的有理表达式，从计算所得。例如，

```matlab
format rat
4.678 * 4.9
```

MATLAB将执行上面的语句，并返回以下结果：

```matlab
ans = 2063/90
```

----

### Matlab 基本语法

#### 基本语法

MATLAB 环境下的行为就像一个超级复杂的计算器。您可以使用 >> 命令提示符下输入命令。

MATLAB 是一种解释型的环境。换句话说，你给一个命令 MATLAB 就马上执行。

键入一个有效的表达，例如，

```matlab
5 + 5
```

然后按ENTER键

当点击“执行”按钮，或者按Ctrl+ E，MATLAB执行它立即返回的结果是：

```matlab
ans = 10
```

让我们使用几个例子：

```matlab
3 ^ 2           % 3 raised to the power of 2
```

当你点击“执行”按钮，或者按Ctrl+ E，MATLAB执行它立即返回的结果是：

```matlab
ans = 9
```

另外一个例子，

```matlab
sin(pi /2)      % sine of angle 90o
```

当你点击“执行”按钮，或者按Ctrl+ E，MATLAB执行它立即返回的结果是：

```matlab
ans = 1
```

MATLAB提供了一些特殊的一些数学符号的表达，像圆周率π, Inf for ∞, i (and j) for √-1 etc. Nan 代表“不是一个数字”。

**使用分号（;)**

分号（;)表示语句结束。但是，如果想抑制和隐藏 MATLAB 输出表达，表达后添加一个分号。

例如，

```matlab
x = 3;
y = x + 5
```

当点击“执行”按钮，或者按Ctrl+ E，MATLAB执行它立即返回的结果是：

```matlab
y =  8
```

**添加注释**

百分比符号（％）是用于表示一个注释行。例如，

```matlab
x = 9         % assign the value 9 to x
```

也可以写注释，使用一块块注释操作符％{％}。

MATLAB编辑器包括工具和上下文菜单项，来帮助添加，删除或更改注释的格式。



----

----

---



### 如何构造一个 Matlab 程序化交易策略

程序化交易策略顾名思义就是让程序执行一些规则化的规则所生成的策略。这次我们来点实际的教你构造一个程序化交易策略。



**一 用公式表达策略**
首先有一些交易的思路，不许能够把它说出来，在纸上变成明确的交易逻辑，有很多人用盘感下单，有些人每次下单的原因都不一样，每次都可以找出不同的交易进出场决定。但是，如果你是想做程序化交易，就必须要有明确且具体的买卖点操作逻辑，可以被完全量化。

**二 使用matlab语言写成策略脚本**
交易规则要合乎逻辑，比如只有买进没有卖出的逻辑就是无法构成一个完整的交易策略。使用matlab按照一些常用的规则不如构造指标，写入买卖逻辑，进行整合交易策略。这个就可以使用Auto-Trader编写，写入代码就是纯matlab代码，只有一些调用的API。都是纯matlab语言，并不难。

**三 回测回放**
编写好一个策略之后，我们需要拿到历史上某段时间段，某一指定频率的测试。这里有两个目的：第一个看是否程序与我们一开始的操作逻辑一致；第二个是看这个策略操作的表现如何，这只是进入下一步之前对于策略有一个大致的了解。必须看起来还可以，比如曲线往上行，或者损失并没有损失非常多的钱，如果回撤非常巨大就要进入分析最大回撤段的原因。这个可以在策略分析模块有比较详尽的分析。

**四 多品种多周期与优化测试**
把该策略在多个品种、周期上测试，查看绩效表现。采用组合优化选取参数，交叉验证，分样本外样本内检验。可以使用各种优化目标进行优化挑选参数。最优化这一部分必须非常小心，容易出现过度拟合的情形，这个是整个策略开发非常重要的一步，一般会采用walk forward 分析，重抽样技术来做一些策略过拟合检验。观察分析在不同的市场结构里面策略的表现情况，这一部分后面会有更为详尽的叙述，当然本人是不建议进行优化操作的。

**五 模拟交易**
在决定策略以后，选取的参数是否有过度拟合的嫌疑，就需要拿到实际行情里面，观察策略的绩效表现。对比模拟交易与回测中的差别，在不同市场行情下表现与回测是否具有一致性。

**六 实时交易**
在众多繁芜复杂的测试之后，最后就是要把你最强大的策略开始使用在市场上，然而这个并非容易的事情，因为成功的策略是非常多，但成功的程序化交易策略倒是少之又少，为什么？心态的问题，你是否相信你自己的策略逻辑。

**七 评估绩效与改进策略**
根据实时交易的情况，与回测校验对比，这部分非常重要，你需要知道你的策略失效条件，根据实盘的反馈进而修复改进策略，不断的注意改进每个细节，你将不断提高你的策略水平，接下来你会慢慢找到你最稳定的程序化策略，在简单与复杂之间找到平衡。如果仍是存在过拟合的问题，根据情况可以放弃该策略，重新再启程。

---

### 策略示例一 ：海龟策略

#### 策略逻辑

海龟是一个相对较为完整的交易策略，涉及到出入场时机的选择，加减仓控制，资金和风险的管理。

1. 入场方式
   海龟交易的入场方式分为两种：
   a) 突破长周期入场
   b) 长周期信号未抓住时，看更长的一个周期的信号决定是否入场
   我们需要注意的是，**海龟策略中会根据上一次发生的信号在当前的盈亏结果决定是否在当前的信号入场**，这也是我们的策略函数中定义了二元变量lastLongBreakUpSignalLose 和 lastShortBreakUpSignalLose的原因。
2. 加减仓
   在完整版海龟策略里，我们会**根据当前的资金状况和所投资标的的不同，采取不同的下单手数**，下单手数计算由子函数calNumShare1来计算
3. 资金与风险管理
   海龟的基本原则是，**根据投资标的数量均分可用资本，每一次下单不超过总体资金的固定比例，此处我们取1%**，同时针对一个标的，我们最多加仓3次。同时，根据当前可用的资金，我们会动态调整风险系数，使得可用资金越多时，下单的手数也越多，在calNumShare1函数中，我们融合了这个功能。
4. 出场方式
   在海龟中，我们采用的是止损出场的方式，**理想情况下随着我们的加仓，对于多头的情形止损线会越来越高**，但在实际运行中会导致回撤较大的问题，在后期中我们会对这一策略进行改进。
5. 其他提醒读者的事项
   在海龟交易中，需要实时记录**目前的仓位和可用资金**，以及**上一笔long/short交易信号发出时的成交价格**（追踪如果根据此次信号入场/加仓d导致的盈亏结果），这些都需要通过全局变量来进行记录，本文中作者直接定义多个全局变量，读者可以自行设计相应的数据结构来优化存储方式，提升回测速度。

#### 策略函数

```matlab
function turtleFinal(longPeriod,shortPeriod,nDayToAverage,longSecondPeriod)
    global tradeRecord;
    global crtMktCap
    global lastShortPrice lastTraded thisOrderEnded
    global isStratBegin
    global underWeightCutPrice  lastLongBreakUpSignalLose lastShortBreakUpSignalLose
    global tradedTimes
    global lastLongEntryPrice lastShortEntryPrice
    TargetList = traderGetTargetList();
    HandleList = traderGetHandleList();
    if isempty(tradeRecord)
        for i = 1:length(TargetList)
            tradeRecord(i).longPrice = 1e9;
            tradeRecord(i).shortPrice = 1e9;
        end
          lastLongBreakUpSignalLose = false;
        lastShortBreakUpSignalLose = false;
    end
    %% parameters
    dayToAvg = 20;
    lastTraded = false;
    thisOrderEnded = false;
    BUFFER_PERIOD = 60;
    MAX_TRADED = 4;
    BASE_RISK_COEFF = 0.01;
    AMT_PER_PT = 300;
    ORIGINAL_MKT_CAP = 1e7;
    NN = 2;
    HandleList = traderGetHandleList();
    nTarget = length(TargetList);
    for i = 1:nTarget
        iTarget = TargetList(i);
        market = TargetList(i).Market;
        code = TargetList(i).Code;
        [~, crtMktCap,~,~,~] = traderGetAccountInfo(HandleList);
        [time,~,high,low,close,volume,~,~] = traderGetKData(market,code,'day',1, 0-BUFFER_PERIOD, 0,false,'FWard');
        [~,~,~,~,crtPrice,~,~,~] = traderGetKData(market,code,'day',1, 0, 0,false,'FWard');
        % date = datestr(time(end));
        % date = date(1:11);
        condNoTrading =  (length(close) < BUFFER_PERIOD+1) || (volume(end)==0);
        if condNoTrading
            continue;
        end
        maxLongPeriodHigh = max(high(end-longPeriod:end-1));
        minLongPeriodLow = min(low(end-longPeriod:end-1));
        maxShortPeriodHigh = max(high(end-shortPeriod:end-1));
        minShortPeriodLow = min(low(end-shortPeriod:end-1));
          maxSecondLongPeriodHigh = max(high(end-longSecondPeriod:end-1)); % second long period to enter
        minSecondLongPeriodLow = min(low(end-longSecondPeriod:end-1)); % second long period to enter
        condBreakLongUp = crtPrice > maxLongPeriodHigh;
        condBreakSecondLongUp = crtPrice > maxSecondLongPeriodHigh;
        condBreakLongDown = crtPrice < minLongPeriodLow;
        condBreakSecondLongDown = crtPrice < minSecondLongPeriodLow;
        condBreakShortUp = crtPrice > maxShortPeriodHigh;
        condBreakShortDown = crtPrice < minShortPeriodLow;
        meanATR = calUnit(high,low,close,dayToAvg);
        if ~lastLongBreakUpSignalLose && crtPrice < (tradeRecord(i).longPrice - 2*meanATR)
              lastLongBreakUpSignalLose = true;
        end
        if ~lastShortBreakUpSignalLose && crtPrice > (tradeRecord(i).shortPrice + 2*meanATR)
            lastShortBreakUpSignalLose = true;
        end
        position = traderGetAccountPosition(HandleList,market,code);
        if position == 0
              tradeRecord(i).longPrice = crtPrice;
              tradeRecord(i).ShortPrice = crtPrice;
              if lastLongBreakUpSignalLose && condBreakLongUp
                    lastLongEntryPrice = newLongTrade(market,code,crtMktCap,HandleList(1),meanATR,ORIGINAL_MKT_CAP,BASE_RISK_COEFF,AMT_PER_PT);
                    lastLongBreakUpSignalLose = false;
                  tradedTimes = 1;
              elseif ~lastLongBreakUpSignalLose && condBreakSecondLongUp
                lastLongEntryPrice = newLongTrade(market,code,crtMktCap,HandleList(1),meanATR,ORIGINAL_MKT_CAP,BASE_RISK_COEFF,AMT_PER_PT);
                    tradedTimes = 1;
              end
            if lastShortBreakUpSignalLose && condBreakLongDown
                    lastShortEntryPrice = newShortTrade(market,code,crtMktCap,HandleList(1),meanATR,ORIGINAL_MKT_CAP,BASE_RISK_COEFF,AMT_PER_PT);
                    lastLongBreakUpSignalLose = false;
                  tradedTimes = 1;
              elseif ~lastShortBreakUpSignalLose && condBreakSecondLongDown
                %lastShortEntryPrice = newShortTrade(market,code,HandleList(1),meanATR,ORIGINAL_MKT_CAP,BASE_RISK_COEFF,AMT_PER_PT);
                orderID = newShortTrade2(market,code,crtMktCap,HandleList(1),meanATR,ORIGINAL_MKT_CAP,BASE_RISK_COEFF,AMT_PER_PT);
                lastShortEntryPrice = crtPrice;
                    tradedTimes = 1;
              end
         elseif position > 0
            condAddLong = crtPrice > lastLongEntryPrice + meanATR;
            if condAddLong && tradedTimes <= MAX_TRADED
                  lastLongEntryPrice = newLongTrade(market,code,crtMktCap,HandleList,meanATR,ORIGINAL_MKT_CAP,BASE_RISK_COEFF,AMT_PER_PT);
                  tradedTimes = tradedTimes + 1;
            end
       else  % position < 0
            condAddShort = crtPrice < lastShortEntryPrice - meanATR;
            if condAddShort && tradedTimes <= MAX_TRADED
                lastShortEntryPrice = newShortTrade(market,code,crtMktCap,HandleList,meanATR,ORIGINAL_MKT_CAP,BASE_RISK_COEFF,AMT_PER_PT);
            end
       end
        % position = traderGetAccountPosition(HandleList(i),market,code);
           condCloseOut1 = position > 0 && condBreakShortDown;
        condCloseOut2 = position < 0 && condBreakShortUp;
        condCloseOut3 = position > 0 && crtPrice < (lastLongEntryPrice - NN*meanATR);
        condCloseOut4 = position < 0 && crtPrice > (lastShortEntryPrice + NN*meanATR);
        if (condCloseOut1 || condCloseOut3)
            traderPositionTo(HandleList(1),market,code,0,0,'market','close out due to long');
            lastLongBreakUpSignalLose = false;
        elseif condCloseOut2 || condCloseOut4
            traderPositionTo(HandleList(1),market,code,0,0,'market','close out due to short');
            lastShortBreakUpSignalLose = false;
        end
    end
end
%% 计算下单手数
function [nShare] = calNumShare1(crtMktCap, N, ORIGINAL_MKT_CAP, BASE_ACC_RISK_COEFF, AMT_PER_PT)
      capPercent = crtMktCap / ORIGINAL_MKT_CAP;
      capPercent = min(capPercent, 1);
      capPercent = floor(capPercent * 10) / 10.0;
      capPercent = max(1 - 2*(1 - capPercent), 0);
      accRiskCoeff = BASE_ACC_RISK_COEFF * capPercent;
      % nShare = floor(mktCap * accRiskCoeff / (NN * absVolRange));
      nShare = floor(crtMktCap * accRiskCoeff / (N * AMT_PER_PT));
end
%% Calculte N: 20-day exponenal moving averge of the True Range
function [N] = calUnit(high,low,close,dayToAvg)
    diffHighLow = high(end-dayToAvg+1:end) - low(end-dayToAvg+1:end);
    absDiffTodayHighPrevClose = abs(high(end-dayToAvg+1:end)-close(end-dayToAvg:end-1));
    absDiffTodayLowPrevClose = abs(low(end-dayToAvg+1:end)-close(end-dayToAvg:end-1));
    maxDiff = max(diffHighLow,max(absDiffTodayHighPrevClose,absDiffTodayLowPrevClose));
    N = mean(maxDiff(end-dayToAvg+1:end)); % 20-day average as ATR
end
%% Calculate unit size
function unitSize = calUnitSize(BASE_RISK_COEFF,crtMktCap,meanATR,AMT_PER_PT)
    unitSize = BASE_RISK_COEFF*crtMktCap / meanATR / AMT_PER_PT;
end
function lastLongEntryPrice = newLongTrade(market,code,crtMktCap,HandleList,meanATR,ORIGINAL_MKT_CAP,BASE_ACC_RISK_COEFF,AMT_PER_PT)
    %[~, crtMktCap,~,~,~] = traderGetAccountInfo(HandleList);
    nShare = calNumShare1(crtMktCap,meanATR,ORIGINAL_MKT_CAP,BASE_ACC_RISK_COEFF,AMT_PER_PT);
    orderID = traderDirectBuy(HandleList,market,code,nShare,0,'market','add to buy');
    lastLongEntryPrice = traderOrderFilledPrice(HandleList(1), orderID);
end
function lastShortEntryPrice = newShortTrade(market,code,crtMktCap,HandleList,meanATR,ORIGINAL_MKT_CAP,BASE_ACC_RISK_COEFF,AMT_PER_PT)
    %[~, crtMktCap,~,~,~] = traderGetAccountInfo(HandleList);
    nShare = calNumShare1(crtMktCap,meanATR,ORIGINAL_MKT_CAP,BASE_ACC_RISK_COEFF,AMT_PER_PT);
    orderID = traderDirectSell(HandleList,market,code,nShare,0,'market','add to short');
    %if orderID == 0
        %lastShortEntryPrice = lastShortEntryPrice;
    %else
        lastShortEntryPrice = traderOrderFilledPrice(HandleList(1), orderID);
    %end
end
function [orderID] = newShortTrade2(market,code,crtMktCap,HandleList,meanATR,ORIGINAL_MKT_CAP,BASE_ACC_RISK_COEFF,AMT_PER_PT)
    %[~, crtMktCap,~,~,~] = traderGetAccountInfo(HandleList);
    nShare = calNumShare1(crtMktCap,meanATR,ORIGINAL_MKT_CAP,BASE_ACC_RISK_COEFF,AMT_PER_PT);
    orderID = traderDirectSell(HandleList,market,code,nShare,0,'market','add to short');
end
```

#### 策略运行函数

```matlab
targetList(1).Market  =  'SHFE';
targetList(1).Code  =  'RB0000';
targetList(2).Market  =   'DCE';
targetList(2).Code  = 'JM0000';
n = length(targetList);
N = 1;
accountList(1) = {'StockBackReplay'};
traderRunBacktest('Turtle',@turtleFinal,{20,10,20,55},accountList,targetList(1),'min',30,20150101,20170101,'FWard');
```

*目前AT提供的免费数据权限只到2015年，请修改数据区间之后再进行回测。

---

### 策略示例二 -- 双均线

#### 策略逻辑

此策略逻辑较为简单，仅仅是在短周期均值突破长周期均值时加入一个过滤器（filter）: 昨日短周期均值反向突破昨日的长周期均值

#### 旧版策略函数

```matlab
function twoLines(freq,shortPeriod,longPeriod,shareNum)
    CUTOFF = 1e-3;  % 截断值
    LAGS = 61;      % 缓冲期
    handleList = traderGetHandleList();
    targetList = traderGetTargetList();
    % 读取60分钟周期的close价格
    [~,~,~,~,close,~,~,~] = traderGetKData(targetList(1).Market,targetList(1).Code,'min',freq, 0-LAGS, 0,false,'FWard');
    % 数据长度不足时跳过
    if length(close) CUTOFF;
    condPrevShortDown = ( mean(close(end-longPeriod:end-1)) -  mean(close(end-shortPeriod:end-1)) ) > CUTOFF;
    condCurrentLongUp =  (  mean(close(end-longPeriod+1:end))  -  mean(close(end-shortPeriod+1:end))  )  > CUTOFF;
    condPrevLongDown = ( mean(close(end-shortPeriod:end-1)) -  mean(close(end-longPeriod:end-1))  ) > CUTOFF;
    % 仓位为负时，昨日短周期下穿以及今日短周期上穿买入固定手数
    if marketposition <=0 && condPrevShortDown && condCurrentShortUp
        orderID1 = traderBuy(handleList(1),targetList(1).Market,targetList(1).Code,shareNum,0,'market','buy1');
    % 仓位为正时，昨日长周期下穿以及今日长周期上穿卖出固定手数
    elseif marketposition >= 0 && condCurrentLongUp && condPrevLongDown
        orderID2 = traderSellShort(handleList(1),targetList(1).Market,targetList(1).Code,shareNum,0,'market','sell1');
    end
end
```

#### 旧版策略运行函数

```matlab
% 针对股指期货主力合约进行回测
targetList(1).Market = 'CFFEX';
targetList(1).Code = 'IF0000';
freq = 60; % 分钟数据周期数
longPeriod = 60;
shortPeriod = 5;
NUM_SHARE=1; % 每次下单的手数
traderSetBacktest(1000000,0.000026,0.02,0,1,0,0);
AccountList(1) = {'FutureBackReplay'};
traderRunBacktest('BackTestTwoLines',@twoLines,{freq,shortPeriod,longPeriod,NUM_SHARE},...
  AccountList,targetList,'min',30,20150104,20160704,'FWard');
```

#### 新版策略函数

```matlab
function twoLinesV2(bInit,bDayBegin,cellPara)
    global dataIndex dataLength data
    global longPeriod shortPeriod CUTOFF NUM_SHARE
    global TargetList
    TargetList = traderGetTargetList();
    HandleIdx = 1:length(TargetList);
    if bInit
        % 采用全局变量，从运行函数中读取相关的参数
        dataType = cellPara{1};
        dataFreq = cellPara{2};
        dataLength = cellPara{3};
          CUTOFF = cellPara{4};
        NUM_SHARE = cellPara{5}
        longPeriod = cellPara{6};
          shortPeriod = cellPara{7};
        dataIndex = traderRegKData(dataType,dataFreq);
    elseif bDayBegin
        % 在本日开始时注册数据
          data = traderGetRegKData(dataIndex,dataLength,false);
    else
        % 将多个标的的close价格存储到一个矩阵中，便于向量化处理
          closePrice = data(5:8:end,:);
        % 数据长度不足时，跳过
          if length(closePrice) < dataLength
            return;
        else
            % 计算今日和昨日的长短周期均值
              closeCurrentShortMean = mean(closePrice(:,end-shortPeriod+1:end),2);
              closeCurrentLongMean = mean(closePrice(:,end-longPeriod+1:end),2);
              closePrevShortMean = mean(closePrice(:,end-shortPeriod:end-1),2);
              closePrevLongMean = mean(closePrice(:,end-longPeriod:end-1),2);
            % 四个突破条件，和老版本相同
              condCurrentShortUp = closeCurrentShortMean - closeCurrentLongMean > CUTOFF;
              condCurrentLongUp = closeCurrentLongMean - closeCurrentShortMean > CUTOFF;
              condPrevShortDown = closePrevLongMean - closePrevShortMean > CUTOFF;
              condPrevLongDown = closePrevShortMean - closePrevLongMean > CUTOFF;
            % 读取持仓
              position = traderGetAccountPositionV2(1,(1:length(TargetList))); % 仓位
            % 设置买卖条件
              condBuy = (position <= 0) & condPrevShortDown & condCurrentShortUp;
              condShort = (position >= 0) & condCurrentLongUp & condPrevLongDown;
            % 新版本下，对多个标的下单，输入的iTarget是在TargetList中的序号，而非标的代码
              for iTarget = 1:length(TargetList)
                    if condBuy(iTarget)
                        traderBuyV2(1,iTarget,NUM_SHARE,0,'market','buy');
                    elseif condShort(iTarget)
                        traderSellShortV2(1,iTarget,NUM_SHARE,0,'market','sell');
                  end
            end
        end
    end
end
```

#### 新版策略运行函数

```matlab
% 针对股指期货主力合约进行回测
targetList(1).Market = 'CFFEX';
targetList(1).Code = 'IF0000';
freq = 60; % 分钟数据周期数
longPeriod = 60;
shortPeriod = 5;
NUM_SHARE=1; % 每次下单的手数
traderSetBacktest(1000000,0.000026,0.02,0,1,0,0);
AccountList(1) = {'FutureBackReplay'};
traderRunBacktest('BackTestTwoLines',@twoLines,{freq,shortPeriod,longPeriod,NUM_SHARE},...
  AccountList,targetList,'min',30,20150104,20160704,'FWard');
```

#### 绩效对比

我们采用相同参数，在旧结构和新结构下分别进行回测，结果分別如下：



注：Auto-Trader 于2017年2月推出了新的回测结构，详细内容参见 AT 进阶教程《Auto-Trader 新回测结构介绍》
学习链接：[Auto-Trader 新回测结构介绍](http://www.digquant.com.cn/study.php?mod=course&sub=AT%E9%87%8F%E8%83%BD&aid=51)

---

### 策略示例三 -- Aberration and Bollinger Band

#### 策略逻辑

Aberration和Bollinger Band相结合交易系统是一个趋势跟踪的系统，其核心是根据当前价格与历史价格的平均值和波动水平的关系来进行开平仓操作。当前价格超出历史均价时，我们认为标的即将上涨，而通过设置超出一个标准差的限制，我们可以过滤掉大部分的噪声信号。

#### 旧版策略函数

```matlab
function aberrationAndBollingerBand(freq,LEN,plus,MaxshareNum) %
    CUTOFF = 1e-3; % 截断值
    NUM_SHARE = 1; % 固定买卖手数
    handleList = traderGetHandleList(); % 读取HandleList账户
    targetList = traderGetTargetList(); % 读取TargetList标的
    % 对每个标的循环
    for iTarget=1:length(targetList)
        %　读取仓位
        marketPos = traderGetAccountPosition(handleList(1),targetList(iTarget).Market,targetList(iTarget).Code); 
        % 读取收盘价，注意LEN参数由运行函数传递而来
　　　[~,~,~,~,close,~,~,~] = traderGetKData(targetList(iTarget).Market,targetList(iTarget).Code,'day',1, 0-LEN, 0,false,'FWard');
        % 数据不足时跳过
        if length(close) < LEN+1
             continue;
        end
        closeStd = std(close(end-LEN+1:end)); % 标准差
        closeMean = mean(close(end-LEN+1:end)); % 历史均值
        % closeMean = closeMean(end);  
        condBreakUpperBandToLongOpen = (marketPos == 0) && ...      % 仓位为0时突破上轨时开多仓
            ((close(end)-closeMean) - (plus*closeStd) > CUTOFF);
        condBreakLowerBandToShortOpen =  (marketPos == 0) && ...    % 仓位为0时突破下轨时开空仓
            ((closeMean - close(end)) - (plus*closeStd)  > CUTOFF);
        condBreakUpperBandToShortClose = (marketPos > 0) && ...     % 仓位大于0时收盘价跌破均值则平仓
            (closeMean - close(end)  > CUTOFF) ;
        condBreakLowerBandToLongClose = (marketPos < 0) && ...      % 仓位小于0时收盘价超出均值则平仓
            (close(end) - closeMean  > CUTOFF);
        % 根据以上条件进行相关开平仓操作
        if condBreakUpperBandToLongOpen
traderBuy(handleList(1),targetList(iTarget).Market,targetList(iTarget).Code,NUM_SHARE,0,'market','buy'); 
        elseif condBreakLowerBandToShortOpen 
             traderSellShort(handleList(1),targetList(iTarget).Market,targetList(iTarget).Code,NUM_SHARE,0,'market','sellshort');  
        end
        if  condBreakUpperBandToShortClose
            traderSell(handleList(1),targetList(iTarget).Market,targetList(iTarget).Code,NUM_SHARE,0,'market','sell');
        elseif condBreakLowerBandToLongClose 
traderBuyToCover(handleList(1),targetList(iTarget).Market,targetList(iTarget).Code,NUM_SHARE,0,'market','buytocover');
        end
end
```

#### 旧版策略运行函数

```matlab
codeList = {'AG0000', 'AL0000', 'AU0000','BU0000',...
    'CU0000','FU0000', 'HC0000', 'PB0000', 'RB0000','RU0000'};
for iCode = 1:length(codeList)
    targetList(iCode).Market = 'SHFE';
    targetList(iCode).Code = codeList{iCode};
end
% 设置策略函数中需要的参数
FREQ=1;     % 读取日线数据，周期为1
LEN = 21;   % 需要21天的数据
PLUS = 1;   % 采用1倍的标准差作为过滤
SHARE_NUM = 1; % 固定下单手数为1
% 设置回测参数
traderSetBacktest(100000000,0.000026,0.02,0,1,0,0);
% 设置账号
AccountList(1) = {'FutureBackReplay'};
% 开始回测
traderRunBacktest('Aberration',@aberrationAndBollingerBand,{FREQ,LEN,PLUS,SHARE_NUM},AccountList, targetList,'min',61,20150104,20160704,'FWard');
```

#### 新版策略函数

相对于原始结构，在V2结构中ATrader可以进行更高效的回测，主要体现在回测结构的明晰， 读取数据方式的优化，下单函数的优化。 在新结构中，我们尽量避免HandleList TargetList等的使用。
在以下函数中，我们采用很多向量化的写法，原因是MatLab向量化的速度高于循环写法。虽然循环写法更为直观，但我们鼓励读者采用向量化写法，既可以减小代码量，也可以提升函数运行速度。

```matlab
function aberrationAndBollingerBandV2(bInit,bDayBegin,cellPara)
%% bInit bDayBegin cellPara作为新版回测框架下的固定结构
%　回测时，每个bar都会调用此函数
    % 设置以下全局变量使得在每个bar内可以共用这些数据，以及在不同bar之内进行通信
    global TargetList  
    global dataType dataFreq dataIndex dataLength data
    global CUTOFF DELTA NUM_SHARE
    TargetList = traderGetTargetList();
    % bInit为真，代表运行函数走到本策略所有时间范围内的第一个bar（the very first）
    if bInit
    % 从cellPara中读取相关参数
           dataType = cellPara{1};   % 要调用数据的时间频率。此处为日day
        dataFreq = cellPara{2};   % 时间周期（频率），此处为1
        dataLength = cellPara{3}; % 没有缺失错误的数据长度，此处为60,
        CUTOFF = cellPara{4};     % 截断值
    DELTA = cellPara{5};   　 % 控制布林带宽度
        NUM_SHARE = cellPara{6};  % 固定下单手数
        dataIndex = traderRegKData(dataType,dataFreq); % 注册数据，返回数据的序号
    % bDayBegin为真，代表为本日的第一个bar    
    elseif bDayBegin
        % 在本日的第一个bar读取数据，将data设为全局变量，使得在else部分可以用到此数据
        data = traderGetRegKData(dataIndex,dataLength,false); 
    else
        closePrice = data(5:8:end,:); % 收盘价处于第五行，对于多个标的，每8行对应一个标的
        closeMean = mean(closePrice,2); % 对多个标的同时取平均，closeMean是一个列向量
        closeStd = std(closePrice,0,2); % 多个标的的标准差，注意查看matlab std函数
        % 将开平仓条件写为矩阵形式
    % 判断击穿上轨：当日收盘价>过去dataLength长度内收盘价均值+一倍的标准差
        % 注意closePrice closeMean closeStd均是列向量，得到的condition也是一个列向量
        condBreakUpperBandToLongOpen = ...
          closePrice(:,end) - closeMean - DELTA*closeStd > CUTOFF;
        % 击穿下轨：反手开仓
        condBreakLowerBandToShortOpen = ...
          closeMean - closePrice(:,end) - DELTA*closeStd > CUTOFF;
        % 多仓时平仓条件
        condBreakUpperBandToShortClose = ...
          closeMean - closePrice(:,end) > CUTOFF;
        % 空仓时平仓条件
        condBreakLowerBandToLongClose = ...
          closePrice(:,end) - closeMean > CUTOFF;
        % 对于每个标的循环
        for iTarget = 1:length(TargetList)
            % 不补齐数据的时候，数据长度不足则直接跳过
            if length(closePrice(iTarget,:)) < dataLength
                continue;
            end
            % 读取标的仓位
            position = traderGetAccountPositionV2(1,iTarget);
                % 仓位为0时判断是否符合开仓条件
            if position == 0
                if condBreakUpperBandToLongOpen(iTarget)
                    % 符合开多仓条件时以市价单（market）买入NUM_SHARE手
                    traderBuyV2(1,iTarget,NUM_SHARE,0,'market','Buy to open');
                elseif condBreakLowerBandToShortOpen(iTarget)
                    % 符合开空仓条件时以市价单（market）空NUM_SHARE手
                    traderSellShortV2(1,iTarget,NUM_SHARE,0,'market','Sell to open');
                end
            % 仓位大于0,判断是否需要平仓
            elseif position > 0 && condBreakUpperBandToShortClose(iTarget)
                traderDirectSellV2(1,iTarget,NUM_SHARE,0,'market','Sell to close');
            % 仓位小于0,判断是否需要平仓
            elseif position < 0 && condBreakLowerBandToLongClose(iTarget)
                traderDirectBuyV2(1,iTarget,NUM_SHARE,0,'market','Buy to close');
            end    
        end
    end
end
```

#### 新版策略运行函数

```matlab
codeList = {'AG0000', 'AL0000', 'AU0000','BU0000',...
    'CU0000','FU0000', 'HC0000', 'PB0000', 'RB0000','RU0000'};
for iCode = 1:length(codeList)
    targetList(iCode).Market = 'SHFE';
    targetList(iCode).Code = codeList{iCode};
end
% 设置策略函数中需要的参数
FREQ=1;     % 读取日线数据，周期为1
LEN = 21;   % 需要21天的数据
PLUS = 1;   % 采用1倍的标准差作为过滤
SHARE_NUM = 1; % 固定下单手数为1
% 设置回测参数
traderSetBacktest(100000000,0.000026,0.02,0,1,0,0);
% 设置账号
AccountList(1) = {'FutureBackReplay'};
% 开始回测
traderRunBacktestV2('Aberration',@aberrationAndBollingerBandV2WithComment,{FREQ,LEN,PLUS,SHARE_NUM},AccountList, targetList,'min',61,20150104,20160704,'FWard');
```

#### 绩效对比

我们采用相同参数，在旧结构和新结构下分别进行回测，结果分別如下：



注：Auto-Trader 于2017年2月推出了新的回测结构，详细内容参见 AT 进阶教程《Auto-Trader 新回测结构介绍》
学习链接：[Auto-Trader 新回测结构介绍](http://www.digquant.com.cn/study.php?mod=course&sub=AT%E9%87%8F%E8%83%BD&aid=51)

---

### 如何识别优秀的量化交易策略

**什么是量化交易？**

量化交易是指以先进的数学模型替代人为的主观判断，是严格按照计算机算法程序给出的买卖决策进行的证券交易。

量化交易包括多种具体方法，在投资品种选择、投资时机选择、股指期货套利、商品期货套利、统计套利和算法交易等领域得到广泛应用。

 

**哪里可以找到策略思想？**

当你缺少交易实战经验，又刚刚准备编写自己的策略时，往往会像无头苍蝇，乱走乱窜。这时候你需要借鉴其他已经比较成熟的投资策略思想，这些思想可以从金融投资方面的书籍、报纸杂志、主流媒体网站、学术论文、交易员论坛和博客等地方获得。除了以上渠道之外，还经常通过以下方式学习和获得交易策略：

1、各大券商的研究报告。

这是一个非常好的学习资料来源，各大券商会有各种量化策略报告，包括金融工程报告、策略研究报告、衍生品报告等。这些报告中的一部分是以非常严谨的方式做的研究，得出结论的可靠程度是很高的，比如在WIND或者ifind金融终端里面打开金融工程这个专栏翻看报告，一些在量化研究里面做的很优秀的如国泰君安、海通这些大券商的报告是非常值得阅读的。

2、量化社区

国内的量化投资火起来后，量化社区发展壮大的速度非常快，目前人气比较高的国内社区有Atrader社区、优矿等，这上面汇集了不少矿工分享和讨论量化交易策略。其实国外的量化社区更丰富，如果英文足够好，去Bing或者Google一下就找到了。

 

**如何认识交易策略**

下面这张图是从Autotrader截的一个策略回测图。光看图走势，该策略是远胜于基准的。但它对你来说一定是个好策略吗？恐怕不能仅仅依靠看图来下结论。

![策略分析](https://www.digquant.com.cn/data/attachment/portal/201703/08/181730wbffqbwb8oysvnsn.png)

我们还需要从各种收益指标或者各种维度来说明，收益指标比如年化收益率、最大回撤、Sharpe比率、Calmar比率等等，当然其他维度包括进攻防御的情况、持续盈利的情况等。关于具体的指标说明，会在另一篇文章《投资策略业绩评估》详细说明。

 

**什么更宝贵，策略本身还是甄别策略的能力？**

那些你认为是秘密的策略多半早已为他人所知，一项策略真正的独有价值和值得保密的地方是你自己的窍门和所进行的变形，而绝不是基础版。对于量化交易研究者而言，**真正困难的地方并不是缺乏交易理念，而是缺乏甄别策略的能力**。这种甄别能力需要我们判断一项策略是否适合自己的实际情况和交易目标（比方说大基金用的策略要求资金容量大，这可能会以牺牲收益率为代价，但是小资金完全可以用大资金没法使用的更高收益率的策略），需要在花费大量时间进行回测之前就能判断出策略是否可行。

 

**寻找适合自己的策略需要考虑哪些主要因素？**

1、交易时间。自己是否有时间进行日间交易？如果没有，可能需要考虑隔夜持仓的交易策略。

2、编程水平。你只会Excel还是可以写Matlab、Python、Java、C或者C++这些语言？如果只会Excel，可能做的交易策略会比用其他编程语言能做的交易策略简单一些。如果会matlab，推荐使用深圳数字动能开发的Auto-trader，如果用Python可使用优矿、米匡等平台。

3、资金规模。小的资金规模能够交易的股票数量少，同时也会限制对冲策略的规模，这都会影响交易策略的选择。

4、收益目标。你的收益目标需要综合考虑持有期和收益持续性之间的关系。

 

**识别貌似可行的策略及其陷阱**

当一个看上去不错的策略呈现在你面前的时候，如何去评价这个策略？这就是本篇文章的重点：识别貌似可行的策略及其陷阱。投资者可以使用这些方法快速评价拟投资产品所使用策略的好坏，量化交易爱好者也可以在进行严格的策略回测之前进行一次省时省力的评估。

1、**策略与基准相比收益如何？收益的持续性如何？**这个问题主要需要回答策略能否跑赢基准和是否有够高的稳定性。

2、挫跌多深、多久？其实也就是**回撤情况，以及回撤的恢复时间**。

如果一项策略近期正在亏钱，它就正在经历挫跌。时刻t的挫跌被定义为：当前净值（假定期间内未发生任何赎回或注资）与t时刻或之前的净值曲线最大值之差。“最大回撤”是净值曲线最大值与之后的净值曲线最小值之差。净值的最大值又被称为“高水位线”。“最大回撤恢复时间”是指净值重返亏损前的水平所花费的最长时间。探究这个问题的意义在于搞清楚：在投资组合清盘或策略结束之前，你能承受多深和多久的挫跌？是20%和3个月，还是10%和1个月？

3、交易成本对策略的影响。

这包括两方面，一方面是因为证券买卖都会发生**手续费**，交易越频繁，成本对策略的盈利的侵蚀就越多。另外一方面是**流动性成本**，当你以市场价格买卖证券的时候，需要支付买卖价差。如果你用限价指令买卖证券，确实可以避免流动性成本，但是却要承担机会成本，因为你可能买不到或者卖不出去。

4、数据有无存活偏差？

股票价格的历史数据库往往不包括由于破产、退市、兼并或者收购而消失的股票，因为**回测数据库中只有幸存者**，所以会存在所谓的存活偏差。使用有存活偏差的数据进行回测是很危险的，因为这样会夸大策略的历史业绩。

5、策略的业绩如何随着时间的变化而变化？

这是一个很重要的问题，因为有很多策略早些年的业绩要远远好于现在，在出色的多年累计业绩之中，早些年或者某些年的贡献特别突出，我们应当对这种非常隐蔽的误导提高警惕，这背后主要有两方面的原因：一方面是**数据的存活偏差导致，回测回溯的越早，消失的股票也越多，偏差就越大**。另外一方面是**金融市场随着制度变化或者交易者的构成的变化会在底层生态上面存在“状态转换”**，因此可能出现在之前某段时间内该策略表现特别好但是后来表现平平的情况。考虑到这两方面的原因，我们应当重点关注某个策略近几年的表现。

6、策略是否存在过度优化拟合？

参数进行过度的优化，令策略历史业绩看上去非常棒，这会产生什么问题呢？其本质是经过过度优化之后呈现的数据模式已经远远偏离真实世界，使得模型与过去发生但是未来不会再重现的任何偶然历史事件吻合，其结果就是该策略的未来业绩与回测结果截然不同。一般而言，**策略的规则越多，模型的参数越多，就越有可能发生数据迁就偏差**。用通俗的话说，如果用一个集所有你喜欢的女星之优点的美女作为模板去找老婆，能找到才怪。

 

**最重要的一点：深刻认识盈亏同源**

在这里还想特别强调一个事情，即天下没有完美的策略。如果一个策略是整体来看是赚钱的并且你打算使用，你就要忍受他的缺点，如果你无法忍受缺点，那你就不要用这个策略，或者不要买使用这个策略的产品，因为盈亏同源。

任何一个策略，都无法做到百分之百盈利，亏损是策略的一个不可分割的部分。用更为通俗的话来说，你的盈利和你的亏损的本源是一致的，这同样的本源带来了收益也同时带来了亏损，如果你试图躲开亏损，那你必然也同时躲开了盈利。只有正确深刻地认识到这一点，你才有可能**以正确的态度面对策略中的亏损、正确的评估最大挫跌和最长挫跌自己是否可以忍受，只有正确地认识了亏损，你才有可能稳定和持续地盈利**。

---

### 投资策略业绩评估

**一、收益率的度量**

对于一个策略的评价，投资收益是一个很简单但也很重要的概念，即最初的本金能带来多少收益，这里的收益是广义的，包括现金流入和资产升值。例如，对股票来说，总收益就是红利加上资本利得。收益率最简单的计算方法是将期初期末的资产价格变动收益(资本收益)加上投资期限内的红利、利息及其它收入，再除以期初本金，即：

![收益](http://www.atrader.com.cn/data/attachment/forum/201702/20/150111po8uvysorr1rvro7.png)

其中期初价格是 ![img](http://www.atrader.com.cn/data/attachment/forum/201702/20/150215mh58v12ss7748u68.png) ，期末价格是 ![img](http://www.atrader.com.cn/data/attachment/forum/201702/20/150244q2mcbtb3xamttrk3.png) ，该期红利或股息是 ![img](http://www.atrader.com.cn/data/attachment/forum/201702/20/150316icowe2ahhwtabs7o.png) 。

1、货币加权收益率

对投资策略业绩的评价通常需要考察1年以上的时间，对收益率的分析一般考察月收益率或每日收益率。在一个策略回测当中，一般都只需要知道初始资金，中间的资金不会流入流出，计算收益率比较简单。但在实际的操作里，策略通常会追加资金或抽回资金，在计算组合的收益率时需要考虑这个问题。

例如，一组资产在季度初的市场价值为 10000 万人民币，恰好在季度结束之前，顾客向投资管理人提供了 500 万人民币的资金，随后测定的该季度末资产的市场价值为 10300 万人民币。如果不考虑增加的 500 万人民币，则报告收益率 为 3%＝(¥10300 万-¥10000 万)／¥10000 万。但这是不正确的，因为期末 10300 万人民币市场价值中有 500 万人民币与经理人员的经营活动无关。如果将增加的 500 万人民币资金纳入考虑之中，则较为准确的季度收益率为 -2%＝[(¥10300 万-¥500 万)-¥10000 万]／¥10000 万。

如果这种资金的增减不是发生在期初或期末, 收益率的计算就会遇到麻烦，在这种情况下，计算资产收益率的方法之一是计算资产的货币加权收益率(或者内在收益率)。例如，如果前面例子中的 500 万人民币是在季度之中交给投资经理人的，则货币加权收益率是则求出下列方程中 r 的解：

![img](http://www.atrader.com.cn/data/attachment/forum/201702/20/150634l82e58zfjrb25y99.png)

方程 r 的解为：r＝-0.98%，该收益率为半季收益率，将其换算成季度收益率为：

![img](http://www.atrader.com.cn/data/attachment/forum/201702/20/150718mtzbfb8deedzvzjn.png)

2、时间加权收益率

度量货币变动发生在期初和期末之间的资产收益率的另一种方法是计算时间加权收益率。这种方法需要利用每一次现金流动刚发生之前的证券资产的市场价值。

在前面的例子中，我们假定在该季度中资产的市场价值为 9600 万人民币，顾客追加 500 万人民币货市投入后，资产的市场价值为 10100 元( 9600 万人民币+ 500 万人民币)。在这种情形下，前半个季度的收益率为 -4%＝( ¥9600 万-¥10000 万)/¥10000 万；后半个季度的收益举为 1.98%＝( ¥10300 万-¥10100 万)/¥10100 万，下面将这两个半季收益率转换为季度收益率为：-2.1%＝[(1-0.04)(1+0.0198)] -1。

前面的分析集中在季度收益率的计算上、如果要把季度收益率转换为年度收益率，设 4 个季度的收益率分别为 ![img](http://www.atrader.com.cn/data/attachment/forum/201702/20/150904s98pipbh681msbzh.png) 则年度收益率为

![img](http://www.atrader.com.cn/data/attachment/forum/201702/20/150936wdmqg3zg6qfdkz6s.png)

一般而言，货币加权收益率法对于评价资产经营成果是不可取的，支持这—结论的理由在于货币加权收益率要受到现金流动(投资人增加或撤回货币)的规模和时机的强烈影响，而对这些因素管理人员是无法加以控制的，所以收益率并不只是管理人员经营能力的体现。

**二、重要的风险调整业绩指标**

评价投资策略的经营效果并不是仅仅比较收益率就行了，由于投资策略的预期收益要受风险因素的影响，因此，业绩测度的含义不仅是计算投资策略的平均收益率，还要考虑其所承受的风险状况，在同一风险水平上的收益率数据才具有可比性。一个简单的调整方法是将投资策略或投资基金按风险分类，然后比较各自的收益率。实际中投资基金常常进行这样的比较来说明其管理资产的能力。但是，这种比较得出的排名并不十分可靠。譬如，相同类型的基金经理有的关注某些股票，有的关注另一些股票，他们的业绩可能就缺乏可比性。因此，需要更精确的风险调整方法。

1、收益风险指标的测度

收益波动率（收益标准差）：假设在评价期间内有T个观察期(例如，当以四年期间内的季度性数据作为考查对象时，于是T＝16)，并且令t期内的收益率为 ![img](http://www.atrader.com.cn/data/attachment/forum/201702/21/113607ucghsz8qxm3q84f4.png) ，则投资策略的平均收益率 ![img](http://www.atrader.com.cn/data/attachment/forum/201702/21/114130mlq5x7sq2soxso77.png) 可以很容易地计算出风险的测度：

![img](http://www.atrader.com.cn/data/attachment/forum/201702/21/114230tnzfry7x4y3nr4fn.png)

事后标准差也可以计算得：

![img](http://www.atrader.com.cn/data/attachment/forum/201702/21/114457zlfahi1zaf002aab.png)

该标准差值可以被看作是投资策略在整个评价期内的总风险之和，可以与其他投资策略的标准差直接地进行比较。

市场风险：资产的收益率也可以与那些市场组合的替代品如沪深300进行比较，以确定在评价期内投资策略的事后 ![img](http://www.atrader.com.cn/data/attachment/forum/201702/21/114752byat4ay8j0t40vtl.png)。令资产在t期内的超额收益率为 ![img](http://www.atrader.com.cn/data/attachment/forum/201702/21/114826xf9m3f8f3kqvj9f8.png) ，沪深300的收益率为 ![img](http://www.atrader.com.cn/data/attachment/forum/201702/21/114909bkcbjol63bwwcyzh.png) ，则沪深300在t期内的超额收益率为![img](http://www.atrader.com.cn/data/attachment/forum/201702/21/114937r8g30158403z31fz.png) ，我们可按下面的方法计算值：

![img](http://www.atrader.com.cn/data/attachment/forum/201702/21/115041gukll9uisqyitq8a.png)

该 ![img](http://www.atrader.com.cn/data/attachment/forum/201702/21/115146jgngaya04v06hvfy.png) 值可以当作该资产在评价期内系统风险的总和，可以直接地与其他资产的值进行比较。

​    最大回撤率：在选定周期内任一历史时点往后推，投资策略的净值走到最低点时的收益率回撤幅度的最大值。最大回撤用来描述买入产品后可能出现的最糟糕的情况。最大回撤是一个重要的风险指标，对于对冲基金和数量化策略交易，该指标比波动率还重要。

2、风险调整收益的几种测度方法

（1）夏普测度(Sharpe’s measure)

它的内容是用投资策略的长期平均超额收益除以这个时期收益的标准差，它测度了对总波动性的回报，与我们在前面介绍的报酬波动性比率是一致的，由于在测度期无风险利率是变化的，所以要用样本的平均值。因此有

![img](http://www.atrader.com.cn/data/attachment/forum/201702/22/105359dojt9bejjbeaitji.png)

夏普测度的含义就是每单位总风险资产获得的超额报酬。夏普测度越大，说明单位风险的获利能力越高，从而投资业绩越好。

（2）特雷纳测度(Treynor’smeasure)

它与夏普测度指标只差一点，夏普指标中超额收益除的是全部风险，而这里除的是系统风险。它的含义是非系统风险可以通过分散化消除，因此，对于充分分散化的投资策略来说，它的超额收益应该是系统风险的函数。它的计算公式为

![img](http://www.atrader.com.cn/data/attachment/forum/201702/22/105443r8z556hatttjpjaj.png)

足够分散化的组合根据特雷纳业绩指数的排序与根据夏普测度的排序相同或类似，而不够分散化的组合的特雷纳业绩指数排序高于夏普业绩指数的排序。                                                      

​    以上两种测度因为度量的是每单位风险所带来的收益，所以通常被称做单位风险收益法。

（3）詹森测度(Jensen’s measure)

这是建立在CAPM模型测算基础上的投资策略的平均收益，它用到了投资策略的贝塔值和平均市场收益，其结果即为投资策略的阿尔法值。它的计算公式为

![img](http://www.atrader.com.cn/data/attachment/forum/201702/22/105538dpxr6zx3mzuu6c3c.png)

上式实际上是用同时期基金或投资策略所实际实现的报酬率减去其期望报酬率得出差异报酬率 (或称风险调整报酬率)，所以也被称做差异报酬率法。当 ![img](http://www.atrader.com.cn/data/attachment/forum/201702/22/105705a4wzqh4bds0fffmt.png) 值显著为正时，表明被评价组合与市场相比较有优越表现；当 ![img](http://www.atrader.com.cn/data/attachment/forum/201702/22/105714twwnazzwwaa7wwp7.png) 值显著为负时，表明被评价组合的表现与市场相比整体表现较差。

（4）信息比率(information ratio)

这是用投资策略的阿尔法值除以其非系统风险，它测算的是每单位非系统风险所带来的非常规收益。它的计算公式为

![img](http://www.atrader.com.cn/data/attachment/forum/201702/22/105748qv9v911rlvwvwo14.png)

从形式上看，詹森测度是估价比率的一部分，要计算估价比率，先要计算出詹森测度。这4种指标各有特点，由于考虑的因素不同，因此计算出的结果也不同。

（5）Calmar比率

这个比率测量的是收益与最大回撤之间的关系，公式是：

![img](http://www.atrader.com.cn/data/attachment/forum/201702/22/105836zcssa6km6sjr1m6a.png)

这个值越大越好，也就是承担同样的回撤风险所得到收益越高，或者获得同样的收益，承担较小的回撤风险。





