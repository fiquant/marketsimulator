class CumulativePrice_Base(object):
    def get_book(self):
        return self.__book
    
    def set_book(self, value):
        self.__book = value
    
    book = property(get_book, set_book)
    def get_depth(self):
        return self.__depth
    
    def set_depth(self, value):
        self.__depth = value
    
    depth = property(get_depth, set_depth)
