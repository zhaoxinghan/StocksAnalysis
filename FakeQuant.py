from Singleton import Singleton
import tushare as ts


class FakeQuant(Singleton):
    _barpos = 0
    __stocks_list = None

    def __init__(self):
        return

    @property
    def barpos(self):
        self._barpos  = self._barpos +1
        return self._barpos

    def set_universe(self, stocks_list):
        self.__stocks_list = stocks_list
        return
    
    def get_universe(self):
        return self.__stocks_list


if __name__ ==  '__main__':
    context = FakeQuant()
    print(context.barpos)
    print(context.barpos)