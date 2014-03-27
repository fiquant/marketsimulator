class Generic_Base(object):
    @property
    def orderFactory(self):
        return self.__orderFactory
    
    @orderFactory.setter
    def orderFactory(self, value):
        self.__orderFactory = value
    
    @property
    def eventGen(self):
        return self.__eventGen
    
    @eventGen.setter
    def eventGen(self, value):
        self.__eventGen = value
    
