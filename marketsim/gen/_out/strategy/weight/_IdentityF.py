from marketsim import IFunction
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "IdentityF"])
class IdentityF_IFunctionFloat(Function[float]):
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
        return self.f
    
def IdentityF(f = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if f is None or rtti.can_be_casted(f, IFunction[float]):
        return IdentityF_IFunctionFloat(f)
    raise Exception("Cannot find suitable overload")
