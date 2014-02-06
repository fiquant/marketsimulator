from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.ops import _Greater_Impl
from marketsim import IFunction
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "Greater"])
class Greater_Optional__IFunction__Float____Optional__IFunction__Float__(Observable[bool],_Greater_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import bool
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._constant import constant as _constant
        Observable[bool].__init__(self)
        self.x = x if x is not None else _constant(1.0)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else _constant(1.0)
        if isinstance(y, types.IEvent):
            event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _Greater_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'y' : IFunction[float]
    }
    def __repr__(self):
        return "({%(x)s}>{%(y)s})" % self.__dict__
    
def Greater(x = None,y = None): 
    return Greater_Optional__IFunction__Float____Optional__IFunction__Float__(x,y)
