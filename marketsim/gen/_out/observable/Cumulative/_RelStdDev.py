from marketsim import registry
from marketsim.ops._function import Function
from marketsim import IObservable
from marketsim.gen._out.observable.Cumulative._Avg import Avg
from marketsim.gen._out.observable.Cumulative._StdDev import StdDev
from marketsim import context
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev(Function[float]):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const
        self.source = source if source is not None else const()
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable
    }
    def __repr__(self):
        return "RSD_{cumul}_{%(source)s}" % self.__dict__
    
    _internals = ['impl']
    @property
    def attributes(self):
        return {}
    
    def getImpl(self):
        return (self.source-Avg(self.source))/StdDev(self.source)
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
