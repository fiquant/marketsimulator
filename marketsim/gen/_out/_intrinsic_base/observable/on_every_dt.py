class OnEveryDt_Base(object):
    def get_x(self):
        return self.__x
    
    def set_x(self, value):
        self.__x = value
    
    x = property(get_x, set_x)
    def get_dt(self):
        return self.__dt
    
    def set_dt(self, value):
        self.__dt = value
    
    dt = property(get_dt, set_dt)
