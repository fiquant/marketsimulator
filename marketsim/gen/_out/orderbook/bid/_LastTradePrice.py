from marketsim import registry
from marketsim import Price
from marketsim.ops._all import Observable
from marketsim import IOrderBook
from marketsim import context
@registry.expose(["Asset", "LastTradePrice"])
class LastTradePrice(Observable[Price]):""" 
    """ 
    def __init__(self, book = None):from marketsim import Price
        from marketsim.ops._all import Observable
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        Observable[Price].__init__(self)
        self.book = book if book is not None else _orderbook_OfTrader()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):return repr(self)
    
    _properties = {'book' : IOrderBook
    }
    def __repr__(self):return "LastTrade(Bid^{%(book)s})" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):from marketsim.gen._out.orderbook._LastTradePrice import LastTradePrice as _orderbook_LastTradePrice
        from marketsim.gen._out.orderbook._Bids import Bids as _orderbook_Bids
        return _orderbook_LastTradePrice(_orderbook_Bids(self.book))
        
    
    def bind(self, ctx):self._ctx = ctx.clone()
    
    def reset(self):self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):return self.impl()
    
