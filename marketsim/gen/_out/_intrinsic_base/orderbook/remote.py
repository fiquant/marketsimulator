class Remote_Base(object):
    def get_orderbook(self):
        return self.__orderbook
    
    def set_orderbook(self, value):
        self.__orderbook = value
    
    orderbook = property(get_orderbook, set_orderbook)
    def get_link(self):
        return self.__link
    
    def set_link(self, value):
        self.__link = value
    
    link = property(get_link, set_link)
    def get_timeseries(self):
        return self.__timeseries
    
    def set_timeseries(self, value):
        self.__timeseries = value
    
    timeseries = property(get_timeseries, set_timeseries)
