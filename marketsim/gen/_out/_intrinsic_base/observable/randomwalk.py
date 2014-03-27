class RandomWalk_Base(object):
    def get_initialValue(self):
        return self.__initialValue
    
    def set_initialValue(self, value):
        self.__initialValue = value
    
    initialValue = property(get_initialValue, set_initialValue)
    def get_deltaDistr(self):
        return self.__deltaDistr
    
    def set_deltaDistr(self, value):
        self.__deltaDistr = value
    
    deltaDistr = property(get_deltaDistr, set_deltaDistr)
    def get_intervalDistr(self):
        return self.__intervalDistr
    
    def set_intervalDistr(self, value):
        self.__intervalDistr = value
    
    intervalDistr = property(get_intervalDistr, set_intervalDistr)
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
    
    name = property(get_name, set_name)
