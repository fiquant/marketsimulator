from marketsim import registry
from marketsim.gen._intrinsic.ops import _Negate_Impl
from marketsim import IFunction
from marketsim import float
@registry.expose(["Ops", "Negate"])
class Negate_Optional__IFunction__Float__(_Negate_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        self.x = x if x is not None else _constant(1.0)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        rtti.check_fields(self)
        _Negate_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float]
    }
    def __repr__(self):
        return "-%(x)s" % self.__dict__
    
Negate = Negate_Optional__IFunction__Float__
