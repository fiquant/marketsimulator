class MinEpsilon_Base(object):
    def get_x(self):
        return self.__x
    
    def set_x(self, value):
        self.__x = value
    
    x = property(get_x, set_x)
    def get_epsilon(self):
        return self.__epsilon
    
    def set_epsilon(self, value):
        self.__epsilon = value
    
    epsilon = property(get_epsilon, set_epsilon)
class MaxEpsilon_Base(object):
    def get_x(self):
        return self.__x
    
    def set_x(self, value):
        self.__x = value
    
    x = property(get_x, set_x)
    def get_epsilon(self):
        return self.__epsilon
    
    def set_epsilon(self, value):
        self.__epsilon = value
    
    epsilon = property(get_epsilon, set_epsilon)
