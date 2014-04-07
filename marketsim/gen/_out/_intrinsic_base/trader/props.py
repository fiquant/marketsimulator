class PendingVolume_Base(object):
    def get_trader(self):
        return self.__trader
    
    def set_trader(self, value):
        self.__trader = value
    
    trader = property(get_trader, set_trader)
class Balance_Base(object):
    def get_trader(self):
        return self.__trader
    
    def set_trader(self, value):
        self.__trader = value
    
    trader = property(get_trader, set_trader)
class Position_Base(object):
    def get_trader(self):
        return self.__trader
    
    def set_trader(self, value):
        self.__trader = value
    
    trader = property(get_trader, set_trader)
