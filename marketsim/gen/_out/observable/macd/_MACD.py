from marketsim import registry
from marketsim.ops._function import Function
from marketsim import IObservable
from marketsim.gen._out.observable.EW._Avg import Avg
from marketsim.gen._out.observable.EW._Avg import Avg
from marketsim import context
@registry.expose(["MACD", "MACD"])
class MACD(Function[float]):
    """ 
    """ 
    def __init__(self, x = None, slow = None, fast = None):
        from marketsim.gen._out.observable.orderbook._MidPrice import MidPrice
        self.x = x if x is not None else MidPrice()
        self.slow = slow if slow is not None else 26.0
        self.fast = fast if fast is not None else 12.0
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable,
        'slow' : float,
        'fast' : float
    }
    def __repr__(self):
        return "MACD_{%(fast)s}^{%(slow)s}(%(x)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return Avg(self.x,2.0/(self.fast+1))-Avg(self.x,2.0/(self.slow+1))
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
