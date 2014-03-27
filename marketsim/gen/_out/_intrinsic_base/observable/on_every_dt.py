class OnEveryDt_Base(object):
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @property
    def dt(self):
        return self.__dt
    
    @dt.setter
    def dt(self, value):
        self.__dt = value
    
