class LastPrice_Base(object):
    @property
    def queue(self):
        return self.__queue
    
    @queue.setter
    def queue(self, value):
        self.__queue = value
    
