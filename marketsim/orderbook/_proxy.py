from marketsim import registry, types, Event, trader, prop, bind

class Base(types.IOrderBook):
    
    def __init__(self):
        self.on_price_changed = Event()
        
    _properties = {}
        
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
        
    @property
    def _digitsToShow(self):
        assert self._impl
        return self._impl._digitsToShow
    
    def getVolumePrices(self, side, volumes):
        assert self._impl
        return self._impl.queue(side).getVolumePrices(volumes)


@registry.expose(['$(OrderBook)'])
class Proxy(Base):
    
    def __init__(self):
        Base.__init__(self)
        self._impl = None
        
    _properties = {}
        
    @property
    def label(self):
        return self._impl.label if self._impl else '$(OrderBook)'    
            
    def bind(self, context):
        assert self._impl is None
        self._impl = context.orderbook
        self._impl.on_price_changed += self.on_price_changed.fire

class OfTrader(Base):
    
    def __init__(self, Trader = None):
        if Trader is None:
            Trader = trader.SASM_Proxy()
        self._alias = ["$(TraderAsset)"] if type(Trader) == trader.SASM_Proxy else ['OfTrader']
        Base.__init__(self)
        self.Trader = Trader

    def bind(self, context): # it is ugly hack; proper dependency tracking should be introduced
        context.trader.orderBook.on_price_changed += self.on_price_changed.fire
        
    @property
    def label(self):
        return self._impl.label if self._impl else self._alias[0]
            
        
    """
        self.orderBook = aTrader.orderBook
        OnPropertyChanged(self.trader, 'orderBook', Method(self, '_onBookChanged'))
        
    def _onBookChanged(self, newval):
        print "OfTrader order book changed: " + repr(self.orderBook) + ' --> ' + repr(newval)
        self.orderBook = newval
    """
        
    _properties = { 'Trader': types.ISingleAssetTrader }
    
    @property
    def _impl(self):
        return self.Trader.orderBook
