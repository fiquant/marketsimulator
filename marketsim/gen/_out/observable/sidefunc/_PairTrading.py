from marketsim import registry
from marketsim import Side
from marketsim.ops._all import Observable
from marketsim import IOrderBook
from marketsim import IFunction_float
from marketsim import IOrderBook
from marketsim import context
@registry.expose(["Side function", "PairTrading"])
class PairTrading(Observable[Side]):
    """ 
    """ 
    def __init__(self, dependee = None, factor = None, book = None):
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        from marketsim.gen._out._constant import constant
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        from marketsim import _
        from marketsim import event
        Observable[Side].__init__(self)
        self.dependee = dependee if dependee is not None else OfTrader()
        self.factor = factor if factor is not None else constant(1.0)
        self.book = book if book is not None else OfTrader()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'dependee' : IOrderBook,
        'factor' : IFunction_float,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "Pt_{%(factor)s*%(dependee)s}(%(book)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable.sidefunc._FundamentalValue import FundamentalValue
        from marketsim.gen._out.observable.orderbook._MidPrice import MidPrice
        return FundamentalValue(MidPrice(self.dependee)*self.factor,self.book)
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
