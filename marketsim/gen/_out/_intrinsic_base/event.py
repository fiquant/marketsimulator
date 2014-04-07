class After_Base(object):
    def get_delay(self):
        return self.__delay
    
    def set_delay(self, value):
        self.__delay = value
    
    delay = property(get_delay, set_delay)
class Every_Base(object):
    def get_intervalFunc(self):
        return self.__intervalFunc
    
    def set_intervalFunc(self, value):
        self.__intervalFunc = value
    
    intervalFunc = property(get_intervalFunc, set_intervalFunc)
