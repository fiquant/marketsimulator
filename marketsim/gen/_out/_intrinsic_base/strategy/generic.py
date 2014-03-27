class Generic_Base(object):
    def get_orderFactory(self):
        return self.__orderFactory
    
    def set_orderFactory(self, value):
        self.__orderFactory = value
    
    orderFactory = property(get_orderFactory, set_orderFactory)
    def get_eventGen(self):
        return self.__eventGen
    
    def set_eventGen(self, value):
        self.__eventGen = value
    
    eventGen = property(get_eventGen, set_eventGen)
