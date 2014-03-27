class After_Base(object):
    @property
    def delay(self):
        return self.__delay
    
    @delay.setter
    def delay(self, value):
        self.__delay = value
    
class Every_Base(object):
    @property
    def intervalFunc(self):
        return self.__intervalFunc
    
    @intervalFunc.setter
    def intervalFunc(self, value):
        self.__intervalFunc = value
    
