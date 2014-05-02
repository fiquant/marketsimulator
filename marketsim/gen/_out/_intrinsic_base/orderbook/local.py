class Local_Base(object):
    def get_name(self):
        return self._back_name
    
    def set_name(self, value):
        self._back_name = value
        self.on_name_set(value)
    
    name = property(get_name, set_name)
    def on_name_set(self, value):
        pass
    
    def get_tickSize(self):
        return self._back_tickSize
    
    def set_tickSize(self, value):
        self._back_tickSize = value
        self.on_tickSize_set(value)
    
    tickSize = property(get_tickSize, set_tickSize)
    def on_tickSize_set(self, value):
        pass
    
    def get__digitsToShow(self):
        return self._back__digitsToShow
    
    def set__digitsToShow(self, value):
        self._back__digitsToShow = value
        self.on__digitsToShow_set(value)
    
    _digitsToShow = property(get__digitsToShow, set__digitsToShow)
    def on__digitsToShow_set(self, value):
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
    
class Asks_Base(object):
    def get_tickSize(self):
        return self._back_tickSize
    
    def set_tickSize(self, value):
        self._back_tickSize = value
        self.on_tickSize_set(value)
    
    tickSize = property(get_tickSize, set_tickSize)
    def on_tickSize_set(self, value):
        pass
    
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
    
class Bids_Base(object):
    def get_tickSize(self):
        return self._back_tickSize
    
    def set_tickSize(self, value):
        self._back_tickSize = value
        self.on_tickSize_set(value)
    
    tickSize = property(get_tickSize, set_tickSize)
    def on_tickSize_set(self, value):
        pass
    
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
    
