class Constant_Base(object):
    def get_x(self):
        return self.__x
    
    def set_x(self, value):
        self.__x = value
    
    x = property(get_x, set_x)
class Null_Base(object):
    pass
class False_Base(object):
    pass
class True_Base(object):
    pass
