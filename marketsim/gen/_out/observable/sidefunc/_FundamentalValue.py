from marketsim import registry
from marketsim import Side
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IOrderBook
from marketsim import context
@registry.expose(["Side function", "FundamentalValue"])
class FundamentalValue(Observable[Side]):
    """ 
    """ 
    def __init__(self, fv = None, book = None):
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        from marketsim import _
        from marketsim import event
        Observable[Side].__init__(self)
        self.fv = fv if fv is not None else constant(200.0)
        self.book = book if book is not None else OfTrader()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'fv' : IFunction,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "Fv_{%(fv)s}(%(book)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.side._Sell import Sell
        from marketsim.gen._out.side._Buy import Buy
        from marketsim.gen._out.side._Nothing import Nothing
        from marketsim.gen._out.observable.orderbook._AskPrice import AskPrice
        from marketsim.gen._out.observable.orderbook._BidPrice import BidPrice
        return (BidPrice(self.book)>self.fv)[Sell(), (AskPrice(self.book)<self.fv)[Buy(), Nothing()]]
        
        
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
