from marketsim import registry
from marketsim.gen._intrinsic.ops import _Negate_Impl
from marketsim import IFunction
@registry.expose(["Ops", "Negate"])
class Negate(_Negate_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        from marketsim import event
        from marketsim import types
        self.x = x if x is not None else _constant(1.0)
        rtti.check_fields(self)
        _Negate_Impl.__init__(self)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float]
    }
    def __repr__(self):
        return "-%(x)s" % self.__dict__
    
