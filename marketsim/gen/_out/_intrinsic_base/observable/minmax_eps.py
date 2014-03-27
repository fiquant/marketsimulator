class MinEpsilon_Base(object):
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @property
    def epsilon(self):
        return self.__epsilon
    
    @epsilon.setter
    def epsilon(self, value):
        self.__epsilon = value
    
class MaxEpsilon_Base(object):
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @property
    def epsilon(self):
        return self.__epsilon
    
    @epsilon.setter
    def epsilon(self, value):
        self.__epsilon = value
    
