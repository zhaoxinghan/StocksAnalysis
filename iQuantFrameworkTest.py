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
        stocks_list = ['600050.SH']