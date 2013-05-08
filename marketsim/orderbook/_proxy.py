from marketsim import registry

@registry.expose('$(OrderBook)')
class Proxy(object):
    
    def __init__(self):
        self._impl = None
        
    _properties = {}
        
    def bind(self, impl):
        if self._impl and impl:
            assert self._impl == impl
        self._impl = impl
    
    @property    
    def impl(self):
        assert self._impl
        return self._impl

    @property
    def on_price_changed(self):
        return self.impl.on_price_changed
        
    def reset(self):
        self.impl.reset()
        
    def queue(self, side):
        return self.impl.queue(side)
    
    def __str__(self):
        return self.impl.__str__()

    def __repr__(self):
        return self.impl.__repr__()
    
    def process(self, order):
        self.impl.process(order)
        
    @property
    def bids(self):
        return self.impl.bids
    
    @property
    def asks(self):
        return self.impl.asks
    
    @property 
    def price(self):
        return self.impl.price
    
    @property
    def spread(self):
        return self.impl.spread
    
    @property
    def tickSize(self):
        return self.impl.tickSize
    
    @tickSize.setter
    def tickSize(self, value):
        self.tickSize = value
