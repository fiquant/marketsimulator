from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim import IFunction
from marketsim import float
from marketsim import context
@registry.expose(["Strategy", "IdentityF"])
class IdentityF_Optional__IFunction__Float__(Function[float]):
    """ 
    """ 
    def __init__(self, f = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        self.f = f if f is not None else _constant()
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'f' : IFunction[float]
    }
    def __repr__(self):
        return "IdentityF(%(f)s)" % self.__dict__
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        return self.f
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
IdentityF = IdentityF_Optional__IFunction__Float__
