from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IOrderBook
from marketsim import IFunction
from marketsim import context
@registry.expose(["Asset's", "NaiveCumulativePrice"])
class NaiveCumulativePrice(Observable[float]):
    """ 
    """ 
    def __init__(self, book = None, depth = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        from marketsim.gen._out._constant import constant
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.book = book if book is not None else OfTrader()
        self.depth = depth if depth is not None else constant()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'depth' : IFunction
    }
    def __repr__(self):
        return "NaiveCumulativePrice(%(book)s, %(depth)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable._Observable import Observable
        from marketsim.gen._out.observable.orderbook._AskPrice import AskPrice
        from marketsim.gen._out.observable.orderbook._BidPrice import BidPrice
        from marketsim.gen._out._const import const
        from marketsim.gen._out._const import const
        from marketsim.gen._out._const import const
        return Observable((self.depth<const(0.0))[self.depth*AskPrice(self.book), (self.depth>const(0.0))[self.depth*BidPrice(self.book), const(0.0)]])
        
        
        
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
