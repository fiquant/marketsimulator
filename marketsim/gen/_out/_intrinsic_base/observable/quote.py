class Quote_Base(object):
    @property
    def ticker(self):
        return self.__ticker
    
    @ticker.setter
    def ticker(self, value):
        self.__ticker = value
    
    @property
    def start(self):
        return self.__start
    
    @start.setter
    def start(self, value):
        self.__start = value
    
    @property
    def end(self):
        return self.__end
    
    @end.setter
    def end(self, value):
        self.__end = value
    
