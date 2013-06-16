from marketsim import registry, types, Event, trader, prop, bind

class Base(types.IOrderBook):
    
    def __init__(self):
        self.on_price_changed = Event()
        self.on_ask_changed = Event()
        self.on_bid_changed = Event()
        
    _properties = {}
        
    def __getattr__(self, name):
        if self._impl:
            return getattr(self._impl, name)
        else:
            raise AttributeError
    
    def __str__(self):
        return 'Proxy for ' + (self._impl.__str__() if self._impl else '')

    def __repr__(self):
        return self.__str__()
    

@registry.expose(['$(OrderBook)'])
class Proxy(Base):
    
    def __init__(self):
        self._impl = None
        Base.__init__(self)
        
    _properties = {}
        
    @property
    def label(self):
        return self._impl.label if self._impl else '$(OrderBook)'    
            
    def bind(self, context):
        assert self._impl is None
        self._impl = context.orderbook
        self._impl.on_price_changed += self.on_price_changed.fire
        self._impl.on_ask_changed += self.on_ask_changed.fire
        self._impl.on_bid_changed += self.on_bid_changed.fire

class OfTrader(Base):
    
    def __init__(self, Trader = None):
        if Trader is None:
            Trader = trader.SASM_Proxy()
        self._alias = ["$(TraderAsset)"] if type(Trader) == trader.SASM_Proxy else ['OfTrader']
        Base.__init__(self)
        self.Trader = Trader

    def bind(self, context): # it is ugly hack; proper dependency tracking should be introduced
        context.trader.orderBook.on_price_changed += self.on_price_changed.fire
        context.trader.orderBook.on_ask_changed += self.on_ask_changed.fire
        context.trader.orderBook.on_bid_changed += self.on_bid_changed.fire
        
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
        try:
            return self.Trader.orderBook
        except AttributeError:
            return None
