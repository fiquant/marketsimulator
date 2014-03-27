class RandomWalk_Base(object):
    @property
    def initialValue(self):
        return self.__initialValue
    
    @initialValue.setter
    def initialValue(self, value):
        self.__initialValue = value
    
    @property
    def deltaDistr(self):
        return self.__deltaDistr
    
    @deltaDistr.setter
    def deltaDistr(self, value):
        self.__deltaDistr = value
    
    @property
    def intervalDistr(self):
        return self.__intervalDistr
    
    @intervalDistr.setter
    def intervalDistr(self, value):
        self.__intervalDistr = value
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
