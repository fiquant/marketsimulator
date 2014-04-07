class TickSize_Base(object):
    def get_book(self):
        return self.__book
    
    def set_book(self, value):
        self.__book = value
    
    book = property(get_book, set_book)
class BestPrice_Base(object):
    def get_queue(self):
        return self.__queue
    
    def set_queue(self, value):
        self.__queue = value
    
    queue = property(get_queue, set_queue)
