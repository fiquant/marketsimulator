from marketsim import registry
from marketsim import float
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import float
from marketsim import IFunction
from marketsim import float
from marketsim import context
@registry.expose(["Basic", "Max"])
class Max_Optional__IFunction__Float____Optional__IFunction__Float__(Observable[float]):
    """  If *x* or/and *y* are observables, *Min* is also observable
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import float
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.x = x if x is not None else _constant()
        self.y = y if y is not None else _constant()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'y' : IFunction[float]
    }
    def __repr__(self):
        return "max{%(x)s, %(y)s}" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.ops._Condition_Float import Condition_Float as _ops_Condition_Float
        from marketsim.gen._out.ops._Greater import Greater as _ops_Greater
        return _ops_Condition_Float(_ops_Greater(self.x,self.y),self.x,self.y)
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
Max = Max_Optional__IFunction__Float____Optional__IFunction__Float__
