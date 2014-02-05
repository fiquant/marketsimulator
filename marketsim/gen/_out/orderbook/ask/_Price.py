from marketsim import registry
from marketsim import Price
from marketsim import Price
from marketsim.ops._all import Observable
from marketsim import IOrderBook
from marketsim import context
@registry.expose(["Asset", "Price"])
class Price_Optional__IOrderBook_(Observable[Price]):
    """ 
    """ 
    def __init__(self, book = None):
        from marketsim import Price
        from marketsim import Price
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
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook
    }
    def __repr__(self):
        return "Ask_{%(book)s}" % self.__dict__
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.orderbook._BestPrice import BestPrice as _orderbook_BestPrice
        from marketsim.gen._out.orderbook._Asks import Asks as _orderbook_Asks
        return _orderbook_BestPrice(_orderbook_Asks(self.book))
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
Price = Price_Optional__IOrderBook_
