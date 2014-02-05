from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim import IObservable
from marketsim import float
from marketsim import float
from marketsim import context
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_Optional__IObservable__Float____Optional__Float_(Function[float]):
    """ 
    """ 
    def __init__(self, source = None, alpha = None):
        from marketsim.gen._out._const import const as _const
        from marketsim import rtti
        self.source = source if source is not None else _const()
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'alpha' : float
    }
    def __repr__(self):
        return "RSD_{\\alpha=%(alpha)s}(%(source)s)" % self.__dict__
    
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
        from marketsim.gen._out.math.EW._Avg import Avg as _math_EW_Avg
        from marketsim.gen._out.math.EW._StdDev import StdDev as _math_EW_StdDev
        return _ops_Div(_ops_Sub(self.source,_math_EW_Avg(self.source,self.alpha)),_math_EW_StdDev(self.source,self.alpha))
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
RelStdDev = RelStdDev_Optional__IObservable__Float____Optional__Float_
