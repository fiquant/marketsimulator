from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IOrderQueue
from marketsim import IFunction
from marketsim import context
@registry.expose(["Asset's", "SafeSidePrice"])
class SafeSidePrice(Observable[float]):
    """ 
    """ 
    def __init__(self, queue = None, defaultValue = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out.observable.orderbook._Asks import Asks
        from marketsim.gen._out._constant import constant
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.queue = queue if queue is not None else Asks()
        self.defaultValue = defaultValue if defaultValue is not None else constant(100.0)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue,
        'defaultValue' : IFunction[float]
    }
    def __repr__(self):
        return "SafeSidePrice^{%(queue)s}" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable._Observable import Observable
        from marketsim.gen._out._IfDefined import IfDefined
        from marketsim.gen._out.observable.orderbook._BestPrice import BestPrice
        from marketsim.gen._out._IfDefined import IfDefined
        from marketsim.gen._out.observable.orderbook._LastPrice import LastPrice
        return Observable(IfDefined(BestPrice(self.queue),IfDefined(LastPrice(self.queue),self.defaultValue)))
        
        
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
