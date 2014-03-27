class LastTradeVolume_Base(object):
    @property
    def queue(self):
        return self.__queue
    
    @queue.setter
    def queue(self, value):
        self.__queue = value
    
class LastTradePrice_Base(object):
    @property
    def queue(self):
        return self.__queue
    
    @queue.setter
    def queue(self, value):
        self.__queue = value
    
