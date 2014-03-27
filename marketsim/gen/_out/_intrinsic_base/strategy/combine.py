class Array_Base(object):
    @property
    def strategies(self):
        return self.__strategies
    
    @strategies.setter
    def strategies(self, value):
        self.__strategies = value
    
class Combine_Base(object):
    @property
    def A(self):
        return self.__A
    
    @A.setter
    def A(self, value):
        self.__A = value
    
    @property
    def B(self):
        return self.__B
    
    @B.setter
    def B(self, value):
        self.__B = value
    
