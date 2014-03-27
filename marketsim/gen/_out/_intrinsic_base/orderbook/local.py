class Local_Base(object):
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def tickSize(self):
        return self.__tickSize
    
    @tickSize.setter
    def tickSize(self, value):
        self.__tickSize = value
    
    @property
    def _digitsToShow(self):
        return self.___digitsToShow
    
    @_digitsToShow.setter
    def _digitsToShow(self, value):
        self.___digitsToShow = value
    
    @property
    def timeseries(self):
        return self.__timeseries
    
    @timeseries.setter
    def timeseries(self, value):
        self.__timeseries = value
    
