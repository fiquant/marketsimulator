class Identity_Base(object):
    def get_array(self):
        return self.__array
    
    def set_array(self, value):
        self.__array = value
    
    array = property(get_array, set_array)
class Score_Base(object):
    def get_trader(self):
        return self.__trader
    
    def set_trader(self, value):
        self.__trader = value
    
    trader = property(get_trader, set_trader)
class ChooseTheBest_Base(object):
    def get_array(self):
        return self.__array
    
    def set_array(self, value):
        self.__array = value
    
    array = property(get_array, set_array)
