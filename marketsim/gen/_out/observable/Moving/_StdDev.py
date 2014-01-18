from marketsim import registry
from marketsim.ops._function import Function
from marketsim import IObservable
from marketsim.gen._out.mathops._Sqrt import Sqrt as _mathops_Sqrt
from marketsim.gen._out.observable.Moving._Var import Var as _observable_Moving_Var
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev(Function[float]):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._const import const as _const
        self.source = source if source is not None else _const()
        self.timeframe = timeframe if timeframe is not None else 100.0
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'timeframe' : float
    }
    def __repr__(self):
        return "\\sqrt{\\sigma^2_{n=%(timeframe)s}(%(source)s)}" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _mathops_Sqrt(_observable_Moving_Var(self.source))
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
