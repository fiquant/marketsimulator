class Suspendable_Base(object):
    def get_inner(self):
        return self.__inner
    
    def set_inner(self, value):
        self.__inner = value
    
    inner = property(get_inner, set_inner)
    def get_predicate(self):
        return self.__predicate
    
    def set_predicate(self, value):
        self.__predicate = value
    
    predicate = property(get_predicate, set_predicate)
