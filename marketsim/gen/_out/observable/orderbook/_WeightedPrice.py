from marketsim import registry
from marketsim.ops._all import Observable
from marketsim import IOrderQueue
from marketsim import float
from marketsim import context
@registry.expose(["Orderbook", "WeightedPrice"])
class WeightedPrice(Observable[float]):
    """ 
    """ 
    def __init__(self, queue = None, alpha = None):
        from marketsim.gen._out.observable.orderbook._Asks import Asks
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.queue = queue if queue is not None else Asks()
        self.alpha = alpha if alpha is not None else 0.015
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
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
    @property
    def attributes(self):
        return {}
    
    def getImpl(self):
        from marketsim.gen._out.observable._EWMA import EWMA
        from marketsim.gen._out.observable.orderbook._LastTradePrice import LastTradePrice
        from marketsim.gen._out.observable.orderbook._LastTradeVolume import LastTradeVolume
        from marketsim.gen._out.observable._EWMA import EWMA
        from marketsim.gen._out.observable.orderbook._LastTradeVolume import LastTradeVolume
        return EWMA(LastTradePrice(self.queue)*LastTradeVolume(self.queue),self.alpha)/EWMA(LastTradeVolume(self.queue),self.alpha)
        
        
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
