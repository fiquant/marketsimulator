from marketsim import registry
from marketsim.ops._function import Function
from marketsim import IOrderQueue
from marketsim.gen._out.observable.EW._Avg import Avg
from marketsim.gen._out.observable.orderbook._LastTradePrice import LastTradePrice
from marketsim.gen._out.observable.orderbook._LastTradeVolume import LastTradeVolume
from marketsim.gen._out.observable.EW._Avg import Avg
from marketsim.gen._out.observable.orderbook._LastTradeVolume import LastTradeVolume
from marketsim import context
@registry.expose(["Asset's", "WeightedPrice"])
class WeightedPrice(Function[float]):
    """ 
    """ 
    def __init__(self, queue = None, alpha = None):
        from marketsim.gen._out.observable.orderbook._Asks import Asks
        self.queue = queue if queue is not None else Asks()
        self.alpha = alpha if alpha is not None else 0.015
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue,
        'alpha' : float
    }
    def __repr__(self):
        return "Price_{%(alpha)s}^{%(queue)s}" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return Avg(LastTradePrice(self.queue)*LastTradeVolume(self.queue),self.alpha)/Avg(LastTradeVolume(self.queue),self.alpha)
    
    
    
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
