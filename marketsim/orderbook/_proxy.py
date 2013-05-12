from marketsim import registry, types, Event

class Base(types.IOrderBook):
    
    def __init__(self):
        self.on_price_changed = Event()
        
    _properties = {}
        
    def reset(self):
        if self._impl:
            self._impl.reset()
        
    def queue(self, side):
        assert self._impl
        return self._impl.queue(side)
    
    def __str__(self):
        return 'Proxy for ' + (self._impl.__str__() if self._impl else '')

    def __repr__(self):
        return self.__str__()
    
    def process(self, order):
        assert self._impl
        self._impl.process(order)
        
    @property
    def bids(self):
        assert self._impl
        return self._impl.bids
    
    @property
    def asks(self):
        assert self._impl
        return self._impl.asks
    
    @property 
    def price(self):
        assert self._impl
        return self._impl.price
    
    @property
    def spread(self):
        assert self._impl
        return self._impl.spread
    
    @property
    def tickSize(self):
        assert self._impl
        return self._impl.tickSize
    
    @tickSize.setter
    def tickSize(self, value):
        assert self._impl
        self._impl.tickSize = value

    def evaluateOrderPrice(self, side, volume):
        assert self._impl
        return self._impl.evaluateOrderPrice(side, volume)

    def evaluateOrderPriceAsync(self, side, volume, callback):
        assert self._impl
        self._impl.evaluateOrderPriceAsync(side, volume, callback)

@registry.expose(['$(OrderBook)'])
class Proxy(Base):
    
    def __init__(self):
        Base.__init__(self)
        self._impl = None
        
    _properties = {}
        
    def bind(self, impl):
        if not self._impl or not impl:
            if self._impl: 
                self._impl.on_price_changed -= self.on_price_changed
            self._impl = impl
            if self._impl:
                self._impl.on_price_changed += self.on_price_changed
        else:
            assert self._impl == impl

class OfTrader(Base):
    
    def __init__(self, trader):
        Base.__init__(self)
        self.trader = trader
        self._alias = ['OfTrader']
        
    _properties = { 'trader': types.ISingleAssetTrader }
    
    @property
    def _impl(self):
        return self.trader.orderBook
