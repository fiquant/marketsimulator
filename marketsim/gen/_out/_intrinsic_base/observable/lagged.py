class Lagged_Base(object):
    def get_source(self):
        return self.__source
    
    def set_source(self, value):
        self.__source = value
    
    source = property(get_source, set_source)
    def get_timeframe(self):
        return self.__timeframe
    
    def set_timeframe(self, value):
        self.__timeframe = value
    
    timeframe = property(get_timeframe, set_timeframe)
