from marketsim import registry
from marketsim.ops._function import Function
from marketsim import Side
from marketsim import IOrderBook
from marketsim.gen._out.observable.sidefunc._Signal import Signal
from marketsim.gen._out._Derivative import Derivative
from marketsim.gen._out.observable.EW._Avg import Avg
from marketsim.gen._out.observable.orderbook._MidPrice import MidPrice
from marketsim import context
@registry.expose(["Side function", "TrendFollower"])
class TrendFollower(Function[Side]):
    """ 
    """ 
    def __init__(self, alpha = None, threshold = None, book = None):
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        self.alpha = alpha if alpha is not None else 0.015
        self.threshold = threshold if threshold is not None else 0.0
        self.book = book if book is not None else OfTrader()
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float,
        'threshold' : float,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "TrendFollower(%(alpha)s, %(threshold)s, %(book)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return Signal(Derivative(Avg(MidPrice(self.book),self.alpha)),self.threshold)
    
    
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
