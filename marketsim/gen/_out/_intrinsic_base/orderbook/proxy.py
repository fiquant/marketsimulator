class Asks_Base(object):
    @property
    def book(self):
        return self.__book
    
    @book.setter
    def book(self, value):
        self.__book = value
    
class Queue_Base(object):
    @property
    def book(self):
        return self.__book
    
    @book.setter
    def book(self, value):
        self.__book = value
    
    @property
    def side(self):
        return self.__side
    
    @side.setter
    def side(self, value):
        self.__side = value
    
class Bids_Base(object):
    @property
    def book(self):
        return self.__book
    
    @book.setter
    def book(self, value):
        self.__book = value
    
