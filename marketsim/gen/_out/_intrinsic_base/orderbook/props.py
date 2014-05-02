class TickSize_Base(object):
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
    
class BestPrice_Base(object):
    def get_queue(self):
        return self._back_queue
    
    def set_queue(self, value):
        self._back_queue = value
        self.on_queue_set(value)
    
    queue = property(get_queue, set_queue)
    def on_queue_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
