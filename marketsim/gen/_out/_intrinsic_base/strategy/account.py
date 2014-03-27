class Account_Base(object):
    @property
    def inner(self):
        return self.__inner
    
    @inner.setter
    def inner(self, value):
        self.__inner = value
    
class VirtualMarket_Base(object):
    @property
    def inner(self):
        return self.__inner
    
    @inner.setter
    def inner(self, value):
        self.__inner = value
    
