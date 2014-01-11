from marketsim import registry
from marketsim.ops._function import Function
from marketsim import Side
from marketsim import IOrderBook
from marketsim.gen._out.observable.sidefunc._Signal import Signal as _observable_sidefunc_Signal
from marketsim.gen._out._Derivative import Derivative as _Derivative
from marketsim.gen._out.observable.EW._Avg import Avg as _observable_EW_Avg
from marketsim.gen._out.observable.orderbook._MidPrice import MidPrice as _observable_orderbook_MidPrice
from marketsim import context
@registry.expose(["Side function", "TrendFollower"])
class TrendFollower(Function[Side]):
    """ 
    """ 
    def __init__(self, alpha = None, threshold = None, book = None):
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader as _observable_orderbook_OfTrader
        self.alpha = alpha if alpha is not None else 0.015
        self.threshold = threshold if threshold is not None else 0.0
        self.book = book if book is not None else _observable_orderbook_OfTrader()
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
        return _observable_sidefunc_Signal(_Derivative(_observable_EW_Avg(_observable_orderbook_MidPrice(self.book),self.alpha)),self.threshold)
    
    
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
