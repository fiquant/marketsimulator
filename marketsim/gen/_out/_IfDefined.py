from marketsim import registry
from marketsim import float
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import float
from marketsim import IFunction
from marketsim import float
from marketsim import context
@registry.expose(["Basic", "IfDefined"])
class IfDefined_Optional__IFunction__Float____Optional__IFunction__Float__(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None, elsePart = None):
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
        self.elsePart = elsePart if elsePart is not None else _constant()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'elsePart' : IFunction[float]
    }
    def __repr__(self):
        return "If def(%(x)s) else %(elsePart)s" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.ops._Condition_Float import Condition_Float as _ops_Condition_Float
        from marketsim.gen._out.ops._NotEqual import NotEqual as _ops_NotEqual
        from marketsim.gen._out._null import null as _null
        return _ops_Condition_Float(_ops_NotEqual(self.x,_null()),self.x,self.elsePart)
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
IfDefined = IfDefined_Optional__IFunction__Float____Optional__IFunction__Float__
