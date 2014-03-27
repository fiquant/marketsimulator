class Suspendable_Base(object):
    @property
    def inner(self):
        return self.__inner
    
    @inner.setter
    def inner(self, value):
        self.__inner = value
    
    @property
    def predicate(self):
        return self.__predicate
    
    @predicate.setter
    def predicate(self, value):
        self.__predicate = value
    
