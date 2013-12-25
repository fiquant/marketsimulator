from marketsim import registry
from marketsim.ops._function import Function
from marketsim import IObservable_Float
from marketsim.gen._out.observable.EW._Avg import Avg
from marketsim.gen._out.observable._UpMovements import UpMovements
from marketsim.gen._out.observable.EW._Avg import Avg
from marketsim.gen._out.observable._DownMovements import DownMovements
from marketsim import context
@registry.expose(["RSI", "Raw"])
class Raw(Function[float]):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None, alpha = None):
        from marketsim.gen._out.observable.orderbook._MidPrice import MidPrice
        self.source = source if source is not None else MidPrice()
        self.timeframe = timeframe if timeframe is not None else 10.0
        self.alpha = alpha if alpha is not None else 0.015
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable_Float,
        'timeframe' : float,
        'alpha' : float
    }
    def __repr__(self):
        return "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return Avg(UpMovements(self.source,self.timeframe),self.alpha)/Avg(DownMovements(self.source,self.timeframe),self.alpha)
    
    
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
