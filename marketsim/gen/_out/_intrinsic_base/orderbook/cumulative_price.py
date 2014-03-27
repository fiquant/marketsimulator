class CumulativePrice_Base(object):
    @property
    def book(self):
        return self.__book
    
    @book.setter
    def book(self, value):
        self.__book = value
    
    @property
    def depth(self):
        return self.__depth
    
    @depth.setter
    def depth(self, value):
        self.__depth = value
    
