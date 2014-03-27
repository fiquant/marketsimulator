class Identity_Base(object):
    @property
    def array(self):
        return self.__array
    
    @array.setter
    def array(self, value):
        self.__array = value
    
class Score_Base(object):
    @property
    def trader(self):
        return self.__trader
    
    @trader.setter
    def trader(self, value):
        self.__trader = value
    
class ChooseTheBest_Base(object):
    @property
    def array(self):
        return self.__array
    
    @array.setter
    def array(self, value):
        self.__array = value
    
