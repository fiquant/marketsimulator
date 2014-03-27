class Array_Base(object):
    def get_strategies(self):
        return self.__strategies
    
    def set_strategies(self, value):
        self.__strategies = value
    
    strategies = property(get_strategies, set_strategies)
class Combine_Base(object):
    def get_A(self):
        return self.__A
    
    def set_A(self, value):
        self.__A = value
    
    A = property(get_A, set_A)
    def get_B(self):
        return self.__B
    
    def set_B(self, value):
        self.__B = value
    
    B = property(get_B, set_B)
