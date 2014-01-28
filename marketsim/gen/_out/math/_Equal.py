from marketsim import registry
from marketsim.gen._intrinsic.ops import _Equal_Impl
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Basic", "Equal"])
class Equal(_Equal_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        self.x = x if x is not None else _constant(1.0)
        self.y = y if y is not None else _constant(1.0)
        rtti.check_fields(self)
        _Equal_Impl.__init__(self)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        if isinstance(y, types.IEvent):
            event.subscribe(self.y, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'y' : IFunction[float]
    }
    def __repr__(self):
        return "({%(x)s}=={%(y)s})" % self.__dict__
    
