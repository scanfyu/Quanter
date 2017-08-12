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

1.1 实数和虚数

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















