from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Basic", "IfDefined"])
class IfDefined_Optional__IFunction__Float____Optional__IFunction__Float__(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None, elsePart = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import float
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
        from marketsim.gen._out.ops._NotEqual import NotEqual as _ops_NotEqual
        from marketsim.gen._out._null import null as _null
        return _ops_Condition_Float(_ops_NotEqual(self.x,_null()),self.x,self.elsePart)
    
def IfDefined(x = None,elsePart = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        if elsePart is None or rtti.can_be_casted(elsePart, IFunction[float]):
            return IfDefined_Optional__IFunction__Float____Optional__IFunction__Float__(x,elsePart)
    raise Exception("Cannot find suitable overload")
