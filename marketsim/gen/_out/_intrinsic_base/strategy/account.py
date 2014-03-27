class Account_Base(object):
    def get_inner(self):
        return self.__inner
    
    def set_inner(self, value):
        self.__inner = value
    
    inner = property(get_inner, set_inner)
class VirtualMarket_Base(object):
    def get_inner(self):
        return self.__inner
    
    def set_inner(self, value):
        self.__inner = value
    
    inner = property(get_inner, set_inner)
