from marketsim import registry
from marketsim.ops._function import Function
from marketsim import IFunction
from marketsim.gen._out.math._Max import Max as _math_Max
from marketsim.gen._out._constant import constant as _constant
from marketsim import context
@registry.expose(["Strategy", "Clamp0"])
class Clamp0(Function[float]):
    """ 
    """ 
    def __init__(self, f = None):
        from marketsim.gen._out._constant import constant as _constant
        self.f = f if f is not None else _constant()
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'f' : IFunction[float]
    }
    def __repr__(self):
        return "Clamp0(%(f)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _math_Max(_constant(0),self.f)+1
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
