class Asks_Base(object):
    def get_book(self):
        return self.__book
    
    def set_book(self, value):
        self.__book = value
    
    book = property(get_book, set_book)
class Queue_Base(object):
    def get_book(self):
        return self.__book
    
    def set_book(self, value):
        self.__book = value
    
    book = property(get_book, set_book)
    def get_side(self):
        return self.__side
    
    def set_side(self, value):
        self.__side = value
    
    side = property(get_side, set_side)
class Bids_Base(object):
    def get_book(self):
        return self.__book
    
    def set_book(self, value):
        self.__book = value
    
    book = property(get_book, set_book)
