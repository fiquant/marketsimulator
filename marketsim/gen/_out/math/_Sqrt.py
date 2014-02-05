from marketsim import registry
from marketsim import float
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import float
@registry.expose(["Log/Pow", "Sqrt"])
class Sqrt_Optional__IFunction__Float__(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import float
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        Observable[float].__init__(self)
        self.x = x if x is not None else _constant(1.0)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float]
    }
    def __repr__(self):
        return "\\sqrt{%(x)s}" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        import math
        x = self.x()
        if x is None: return None
        return math.sqrt(x)
    
Sqrt = Sqrt_Optional__IFunction__Float__
