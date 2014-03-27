class TickSize_Base(object):
    @property
    def book(self):
        return self.__book
    
    @book.setter
    def book(self, value):
        self.__book = value
    
class BestPrice_Base(object):
    @property
    def queue(self):
        return self.__queue
    
    @queue.setter
    def queue(self, value):
        self.__queue = value
    
