from marketsim import IObservable
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import context
from marketsim import float
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_Optional__IObservable__Float__(Function[float]):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const as _const
        from marketsim import rtti
        self.source = source if source is not None else _const()
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float]
    }
    def __repr__(self):
        return "RSD_{cumul}(%(source)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.ops._Div import Div as _ops_Div
        from marketsim.gen._out.ops._Sub import Sub as _ops_Sub
        from marketsim.gen._out.math.Cumulative._Avg import Avg as _math_Cumulative_Avg
        from marketsim.gen._out.math.Cumulative._StdDev import StdDev as _math_Cumulative_StdDev
        return _ops_Div(_ops_Sub(self.source,_math_Cumulative_Avg(self.source)),_math_Cumulative_StdDev(self.source))
    
def RelStdDev(source = None): 
    return RelStdDev_Optional__IObservable__Float__(source)
