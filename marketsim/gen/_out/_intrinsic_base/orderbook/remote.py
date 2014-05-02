class Remote_Base(object):
    def get_orderbook(self):
        return self._back_orderbook
    
    def set_orderbook(self, value):
        self._back_orderbook = value
        self.on_orderbook_set(value)
    
    orderbook = property(get_orderbook, set_orderbook)
    def on_orderbook_set(self, value):
        pass
    
    def get_link(self):
        return self._back_link
    
    def set_link(self, value):
        self._back_link = value
        self.on_link_set(value)
    
    link = property(get_link, set_link)
    def on_link_set(self, value):
        pass
    
    def get_timeseries(self):
        return self._back_timeseries
    
    def set_timeseries(self, value):
        self._back_timeseries = value
        self.on_timeseries_set(value)
    
    timeseries = property(get_timeseries, set_timeseries)
    def on_timeseries_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class Queue_Base(object):
    def get_queue(self):
        return self._back_queue
    
    def set_queue(self, value):
        self._back_queue = value
        self.on_queue_set(value)
    
    queue = property(get_queue, set_queue)
    def on_queue_set(self, value):
        pass
    
    def get_book(self):
        return self._back_book
    
    def set_book(self, value):
        self._back_book = value
        self.on_book_set(value)
    
    book = property(get_book, set_book)
    def on_book_set(self, value):
        pass
    
    def get_link(self):
        return self._back_link
    
    def set_link(self, value):
        self._back_link = value
        self.on_link_set(value)
    
    link = property(get_link, set_link)
    def on_link_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
