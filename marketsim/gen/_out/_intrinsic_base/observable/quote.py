class Quote_Base(object):
    def get_ticker(self):
        return self._back_ticker
    
    def set_ticker(self, value):
        self._back_ticker = value
        self.on_ticker_set(value)
    
    ticker = property(get_ticker, set_ticker)
    def on_ticker_set(self, value):
        pass
    
    def get_start(self):
        return self._back_start
    
    def set_start(self, value):
        self._back_start = value
        self.on_start_set(value)
    
    start = property(get_start, set_start)
    def on_start_set(self, value):
        pass
    
    def get_end(self):
        return self._back_end
    
    def set_end(self, value):
        self._back_end = value
        self.on_end_set(value)
    
    end = property(get_end, set_end)
    def on_end_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
