class SingleAsset_Base(object):
    def get_orderBook(self):
        return self.__orderBook
    
    def set_orderBook(self, value):
        self.__orderBook = value
    
    orderBook = property(get_orderBook, set_orderBook)
    def get_strategy(self):
        return self.__strategy
    
    def set_strategy(self, value):
        self.__strategy = value
    
    strategy = property(get_strategy, set_strategy)
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
    
    name = property(get_name, set_name)
    def get_amount(self):
        return self.__amount
    
    def set_amount(self, value):
        self.__amount = value
    
    amount = property(get_amount, set_amount)
    def get_PnL(self):
        return self.__PnL
    
    def set_PnL(self, value):
        self.__PnL = value
    
    PnL = property(get_PnL, set_PnL)
    def get_timeseries(self):
        return self.__timeseries
    
    def set_timeseries(self, value):
        self.__timeseries = value
    
    timeseries = property(get_timeseries, set_timeseries)
class MultiAsset_Base(object):
    def get_traders(self):
        return self.__traders
    
    def set_traders(self, value):
        self.__traders = value
    
    traders = property(get_traders, set_traders)
    def get_strategy(self):
        return self.__strategy
    
    def set_strategy(self, value):
        self.__strategy = value
    
    strategy = property(get_strategy, set_strategy)
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
    
    name = property(get_name, set_name)
    def get_PnL(self):
        return self.__PnL
    
    def set_PnL(self, value):
        self.__PnL = value
    
    PnL = property(get_PnL, set_PnL)
    def get_timeseries(self):
        return self.__timeseries
    
    def set_timeseries(self, value):
        self.__timeseries = value
    
    timeseries = property(get_timeseries, set_timeseries)
