class PendingVolume_Base(object):
    def get_trader(self):
        return self._back_trader
    
    def set_trader(self, value):
        self._back_trader = value
        self.on_trader_set(value)
    
    trader = property(get_trader, set_trader)
    def on_trader_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class Balance_Base(object):
    def get_trader(self):
        return self._back_trader
    
    def set_trader(self, value):
        self._back_trader = value
        self.on_trader_set(value)
    
    trader = property(get_trader, set_trader)
    def on_trader_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
class Position_Base(object):
    def get_trader(self):
        return self._back_trader
    
    def set_trader(self, value):
        self._back_trader = value
        self.on_trader_set(value)
    
    trader = property(get_trader, set_trader)
    def on_trader_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
    def reset(self):
        pass
    
