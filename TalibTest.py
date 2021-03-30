import tushare as ts
import pandas as pd
import numpy as np
import talib
from numpy.core.numeric import NaN

class TalibTest:
    def __init__(self):
        return

    def getStockInfoFromTushare(self):
        startDate   = '20190101'    # start query date
        endDate     = '20201231'    # end query date

        tsCode = self.GetTsCode()    # Get query ts_code

        ts.set_token('79cfeef7606afc45b9676ddcf9937471802ae79224210f48c6a28536')
        pro = ts.pro_api()

        df = pro.daily(ts_code = tsCode,start_date = startDate,end_date = endDate)
        if(df is not None):
            print("Get data from Tushare, over !")
        # get a new dataframe of MA3 and MA7
        df['MA5'] = NaN


        df['MA5'] = talib.SMA(df['close'],5)
        print(df)

        df2 = df.tail(2)
        print(df2)

        return

    def GetTsCode(self):
        return '000001.SZ'


if __name__ == '__main__':
    print('main function start')
    test = TalibTest()
    test.getStockInfoFromTushare()


    


