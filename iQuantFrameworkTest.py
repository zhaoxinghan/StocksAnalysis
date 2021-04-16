from FakeQuant import FakeQuant
import numpy as np
import tushare as ts
import pandas as pd
import talib



class iQuantFrameworkTest:
    ContextInfo = None

    def __init__(self):
        ContextInfo = FakeQuant()

    def init(ContextInfo):
        ContextInfo.s = ContextInfo.get_sector('00300.SH')
        # 设定股票池为沪深300
        ContextInfo.set_universe(ContextInfo.s)
        # 策略运行天数
        ContextInfo.day = 0
        # 持仓情况
        ContextInfo.holdings = {i:0 for i in ContextInfo.s}
        # 资金权重
        ContextInfo.weight = [0.1]* 10
        # 买入点
        ContextInfo.buypoint = {}
        # 可用资金
        ContextInfo.money = ContextInfo.capital
        # 策略盈利
        ContextInfo.profit = 0
        # 设置交易账户
        ContextInfo.accountID = 'testS'
        # 策略运行天数的要求
        ContextInfo.runDate = 30

    # 2.====================周期循环================
    def handlebar(ContextInfo):
        # 策略运行天数要求大于runDate天
        d = ContextInfo.barpos
        if d < ContextInfo.runDate:
            nowDate = timetag_to_datetime(ContextInfo.get_bar_timetag(d),'%Y%m%d')
            return
        # 获取股票池中过去3日的收盘价数据
        price = ContextInfo.get_history_data(3,'1d','close',3)
        # 对股票池最近三日的数据进行初步筛选
