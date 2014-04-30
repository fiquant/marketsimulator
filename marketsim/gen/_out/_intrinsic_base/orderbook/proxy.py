class Asks_Base(object):
    def get_book(self):
        return self._back_book
    
    def set_book(self, value):
        self._back_book = value
        self.on_book_set(value)
    
    book = property(get_book, set_book)
    def on_book_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class Queue_Base(object):
    def get_book(self):
        return self._back_book
    
    def set_book(self, value):
        self._back_book = value
        self.on_book_set(value)
    
    book = property(get_book, set_book)
    def on_book_set(self, value):
        pass
    
    def get_side(self):
        return self._back_side
    
    def set_side(self, value):
        self._back_side = value
        self.on_side_set(value)
    
    side = property(get_side, set_side)
    def on_side_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class Bids_Base(object):
    def get_book(self):
        return self._back_book
    
    def set_book(self, value):
        self._back_book = value
        self.on_book_set(value)
    
    book = property(get_book, set_book)
    def on_book_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
