from marketsim import registry, types, Event, prop, bind, context, Side

from marketsim.trader._proxy import SingleProxy

class Base(types.IOrderBook):
    
    _properties = {}
        
    def __getattr__(self, name):
        if name[0:2] != '__' and self._impl:
            return getattr(self._impl, name)
        else:
            raise AttributeError
    
    def __str__(self):
        return 'Proxy for ' + (self._impl.__str__() if self._impl else '')

    def __repr__(self):
        return self.__str__()
    
class Queue(types.IOrderQueue):
    
    _properties = { 'orderbook' : types.IOrderBook, 
                    'side'      : types.Side }
    
    def __init__(self, orderbook, side):
        self.orderbook = orderbook
        self.side = side 
        
    @property
    def _impl(self):
        try:
            return self.orderbook.queue(self.side)
        except AttributeError:
            return None
        
    def __getattr__(self, name):
        if name[0:2] != '__' and self._impl:
            return getattr(self._impl, name)
        else:
            raise AttributeError
    
    def __str__(self):
        return 'Proxy for ' + (self._impl.__str__() if self._impl else '')

    def __repr__(self):
        return self.__str__()

@registry.expose(["Queue's", "Asks"], args = (None,))    
def Asks(orderbook = None):
    if orderbook is None: orderbook = OfTrader()
    return Queue(orderbook, Side.Sell)

@registry.expose(["Queue's", "Bids"], args = (None,))    
def Bids(orderbook):
    if orderbook is None: orderbook = OfTrader()
    return Queue(orderbook, Side.Buy)
    
@registry.expose(['$(OrderBook)'])
class Proxy(Base):
    
    def __init__(self):
        self._impl = None
        Base.__init__(self)
        
    _properties = {}
        
    @property
    def label(self):
        return self._impl.label if self._impl else '$(OrderBook)'    
            
    def bind(self, ctx):
        assert self._impl is None
        self._impl = ctx.orderbook

class OfTrader(Base):
    
    def __init__(self, Trader = None):
        if Trader is None:
            Trader = SingleProxy()
        self._alias = ["$(TraderAsset)"] if type(Trader) == SingleProxy else ['OfTrader']
        Base.__init__(self)
        self.Trader = Trader

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
