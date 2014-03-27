class Local_Base(object):
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
    
    name = property(get_name, set_name)
    def get_tickSize(self):
        return self.__tickSize
    
    def set_tickSize(self, value):
        self.__tickSize = value
    
    tickSize = property(get_tickSize, set_tickSize)
    def get__digitsToShow(self):
        return self.___digitsToShow
    
    def set__digitsToShow(self, value):
        self.___digitsToShow = value
    
    _digitsToShow = property(get__digitsToShow, set__digitsToShow)
    def get_timeseries(self):
        return self.__timeseries
    
    def set_timeseries(self, value):
        self.__timeseries = value
    
    timeseries = property(get_timeseries, set_timeseries)
