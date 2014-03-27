class PendingVolume_Base(object):
    @property
    def trader(self):
        return self.__trader
    
    @trader.setter
    def trader(self, value):
        self.__trader = value
    
class Balance_Base(object):
    @property
    def trader(self):
        return self.__trader
    
    @trader.setter
    def trader(self, value):
        self.__trader = value
    
class Position_Base(object):
    @property
    def trader(self):
        return self.__trader
    
    @trader.setter
    def trader(self, value):
        self.__trader = value
    
