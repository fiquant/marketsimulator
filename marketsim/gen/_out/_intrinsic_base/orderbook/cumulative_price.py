class CumulativePrice_Base(object):
    def get_book(self):
        return self._back_book
    
    def set_book(self, value):
        self._back_book = value
        self.on_book_set(value)
    
    book = property(get_book, set_book)
    def on_book_set(self, value):
        pass
    
    def get_depth(self):
        return self._back_depth
    
    def set_depth(self, value):
        self._back_depth = value
        self.on_depth_set(value)
    
    depth = property(get_depth, set_depth)
    def on_depth_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
