class Quote_Base(object):
    def get_ticker(self):
        return self.__ticker
    
    def set_ticker(self, value):
        self.__ticker = value
    
    ticker = property(get_ticker, set_ticker)
    def get_start(self):
        return self.__start
    
    def set_start(self, value):
        self.__start = value
    
    start = property(get_start, set_start)
    def get_end(self):
        return self.__end
    
    def set_end(self, value):
        self.__end = value
    
    end = property(get_end, set_end)
