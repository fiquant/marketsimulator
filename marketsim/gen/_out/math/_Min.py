from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Basic", "Min"])
class Min_Optional__IFunction__Float____Optional__IFunction__Float__(Observable[float]):
    """  If *x* or/and *y* are observables, *Min* is also observable
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import float
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
        return "min{%(x)s, %(y)s}" % self.__dict__
    
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
        from marketsim.gen._out.ops._Condition_Float import Condition_Float as _ops_Condition_Float
        from marketsim.gen._out.ops._Less import Less as _ops_Less
        return _ops_Condition_Float(_ops_Less(self.x,self.y),self.x,self.y)
    
def Min(x = None,y = None): 
    return Min_Optional__IFunction__Float____Optional__IFunction__Float__(x,y)
