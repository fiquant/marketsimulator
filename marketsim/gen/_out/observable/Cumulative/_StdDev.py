from marketsim import registry
from marketsim.ops._function import Function
from marketsim import IObservable
from marketsim.gen._out.mathops._Sqrt import Sqrt as _mathops_Sqrt
from marketsim.gen._out.observable.Cumulative._Var import Var as _observable_Cumulative_Var
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev(Function[float]):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const as _const
        self.source = source if source is not None else _const()
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float]
    }
    def __repr__(self):
        return "\\sqrt{\\sigma^2_{cumul}_{%(source)s}}" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _mathops_Sqrt(_observable_Cumulative_Var(self.source))
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
