from marketsim import registry
from marketsim.ops._function import Function
from marketsim import IFunction
from marketsim.gen._out.math._Atan import Atan as _math_Atan
from marketsim.gen._out.math._Pow import Pow as _math_Pow
from marketsim.gen._out._constant import constant as _constant
from marketsim import context
@registry.expose(["Strategy", "AtanPow"])
class AtanPow(Function[float]):
    """ 
    """ 
    def __init__(self, f = None, base = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        self.f = f if f is not None else _constant()
        self.base = base if base is not None else 1.002
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'f' : IFunction[float],
        'base' : float
    }
    def __repr__(self):
        return "AtanPow(%(f)s, %(base)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _math_Atan(_math_Pow(_constant(self.base),self.f))
    
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
