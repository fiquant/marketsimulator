class CandleSticks_Base(object):
    @property
    def source(self):
        return self.__source
    
    @source.setter
    def source(self, value):
        self.__source = value
    
    @property
    def timeframe(self):
        return self.__timeframe
    
    @timeframe.setter
    def timeframe(self, value):
        self.__timeframe = value
    
