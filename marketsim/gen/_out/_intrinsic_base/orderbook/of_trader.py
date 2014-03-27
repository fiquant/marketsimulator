class Proxy_Base(object):
    pass
class OfTrader_Base(object):
    @property
    def Trader(self):
        return self.__Trader
    
    @Trader.setter
    def Trader(self, value):
        self.__Trader = value
    
