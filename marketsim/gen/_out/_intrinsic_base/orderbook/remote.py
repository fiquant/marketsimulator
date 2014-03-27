class Remote_Base(object):
    @property
    def orderbook(self):
        return self.__orderbook
    
    @orderbook.setter
    def orderbook(self, value):
        self.__orderbook = value
    
    @property
    def link(self):
        return self.__link
    
    @link.setter
    def link(self, value):
        self.__link = value
    
    @property
    def timeseries(self):
        return self.__timeseries
    
    @timeseries.setter
    def timeseries(self, value):
        self.__timeseries = value
    
