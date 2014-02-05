from marketsim import registry
from marketsim import float
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import float
from marketsim import context
@registry.expose(["Log/Pow", "Sqr"])
class Sqr_Optional__IFunction__Float__(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import float
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.x = x if x is not None else _constant()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float]
    }
    def __repr__(self):
        return "{%(x)s}^2" % self.__dict__
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.ops._Mul import Mul as _ops_Mul
        return _ops_Mul(self.x,self.x)
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
Sqr = Sqr_Optional__IFunction__Float__
