class Constant_Base(object):
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
class Null_Base(object):
    pass
class False_Base(object):
    pass
class True_Base(object):
    pass
