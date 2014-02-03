from marketsim import registry
from marketsim import Side
from marketsim import Side
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import float
from marketsim import IOrderBook
from marketsim import context
@registry.expose(["Side function", "FundamentalValue"])
class FundamentalValue(Observable[Side]):
    """ 
    """ 
    def __init__(self, fv = None, book = None):
        from marketsim import Side
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        Observable[Side].__init__(self)
        self.fv = fv if fv is not None else _constant(200.0)
        self.book = book if book is not None else _orderbook_OfTrader()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'fv' : IFunction[float],
        'book' : IOrderBook
    }
    def __repr__(self):
        return "FundamentalValue(%(fv)s, %(book)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.orderbook.bid._Price import Price as _orderbook_bid_Price
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out.orderbook.ask._Price import Price as _orderbook_ask_Price
        from marketsim.gen._out.side._Buy import Buy as _side_Buy
        from marketsim.gen._out.side._Nothing import Nothing as _side_Nothing
        return (_orderbook_bid_Price(self.book)>self.fv)[_side_Sell(), (_orderbook_ask_Price(self.book)<self.fv)[_side_Buy(), _side_Nothing()]]
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
