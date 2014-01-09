from marketsim import registry
from marketsim.ops._function import Function
from marketsim import Side
from marketsim import IOrderBook
from marketsim.gen._out.observable.sidefunc._Signal import Signal
from marketsim.gen._out.observable.EW._Avg import Avg
from marketsim.gen._out.observable.orderbook._MidPrice import MidPrice
from marketsim.gen._out.observable.EW._Avg import Avg
from marketsim.gen._out.observable.orderbook._MidPrice import MidPrice
from marketsim import context
@registry.expose(["Side function", "CrossingAverages"])
class CrossingAverages(Function[Side]):
    """ 
    """ 
    def __init__(self, alpha_1 = None, alpha_2 = None, threshold = None, book = None):
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        self.alpha_1 = alpha_1 if alpha_1 is not None else 0.015
        self.alpha_2 = alpha_2 if alpha_2 is not None else 0.15
        self.threshold = threshold if threshold is not None else 0.0
        self.book = book if book is not None else OfTrader()
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha_1' : float,
        'alpha_2' : float,
        'threshold' : float,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "CrossingAverages(%(alpha_1)s, %(alpha_2)s, %(threshold)s, %(book)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return Signal(Avg(MidPrice(self.book),self.alpha_1)-Avg(MidPrice(self.book),self.alpha_2),self.threshold)
    
    
    
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
