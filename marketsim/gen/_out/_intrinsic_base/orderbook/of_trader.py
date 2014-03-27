class Proxy_Base(object):
    pass
class OfTrader_Base(object):
    def get_Trader(self):
        return self.__Trader
    
    def set_Trader(self, value):
        self.__Trader = value
    
    Trader = property(get_Trader, set_Trader)
