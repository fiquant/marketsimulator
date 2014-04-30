class Proxy_Base(object):
    pass
    def bind_impl(self, ctx):
        pass
    
class OfTrader_Base(object):
    def get_Trader(self):
        return self._back_Trader
    
    def set_Trader(self, value):
        self._back_Trader = value
        self.on_Trader_set(value)
    
    Trader = property(get_Trader, set_Trader)
    def on_Trader_set(self, value):
        pass
    
    def bind_impl(self, ctx):
        pass
    
