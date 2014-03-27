class Variance_Base(object):
    def get_x(self):
        return self.__x
    
    def set_x(self, value):
        self.__x = value
    
    x = property(get_x, set_x)
