class SingleAsset_Base(object):
    @property
    def orderBook(self):
        return self.__orderBook
    
    @orderBook.setter
    def orderBook(self, value):
        self.__orderBook = value
    
    @property
    def strategy(self):
        return self.__strategy
    
    @strategy.setter
    def strategy(self, value):
        self.__strategy = value
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, value):
        self.__amount = value
    
    @property
    def PnL(self):
        return self.__PnL
    
    @PnL.setter
    def PnL(self, value):
        self.__PnL = value
    
    @property
    def timeseries(self):
        return self.__timeseries
    
    @timeseries.setter
    def timeseries(self, value):
        self.__timeseries = value
    
class MultiAsset_Base(object):
    @property
    def traders(self):
        return self.__traders
    
    @traders.setter
    def traders(self, value):
        self.__traders = value
    
    @property
    def strategy(self):
        return self.__strategy
    
    @strategy.setter
    def strategy(self, value):
        self.__strategy = value
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def PnL(self):
        return self.__PnL
    
    @PnL.setter
    def PnL(self, value):
        self.__PnL = value
    
    @property
    def timeseries(self):
        return self.__timeseries
    
    @timeseries.setter
    def timeseries(self, value):
        self.__timeseries = value
    
