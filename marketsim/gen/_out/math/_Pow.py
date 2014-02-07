from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IFunction
@registry.expose(["Log/Pow", "Pow"])
class Pow_IFunctionFloatIFunctionFloat(Observable[float]):
    """ 
     Exceptional cases follow Annex F of the C99 standard as far as possible.
     In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
     even when *x* is a zero or a NaN.
     If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
     ``pow(x, y)`` is undefined, and raises ``ValueError``.
    """ 
    def __init__(self, base = None, power = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import float
        Observable[float].__init__(self)
        self.base = base if base is not None else _constant(1.0)
        if isinstance(base, types.IEvent):
            event.subscribe(self.base, self.fire, self)
        self.power = power if power is not None else _constant(1.0)
        if isinstance(power, types.IEvent):
            event.subscribe(self.power, self.fire, self)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'base' : IFunction[float],
        'power' : IFunction[float]
    }
    def __repr__(self):
        return "%(base)s^{%(power)s}" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        import math
        base = self.base()
        if base is None: return None
        power = self.power()
        if power is None: return None
        return math.pow(base, power)
    
def Pow(base = None,power = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if base is None or rtti.can_be_casted(base, IFunction[float]):
        if power is None or rtti.can_be_casted(power, IFunction[float]):
            return Pow_IFunctionFloatIFunctionFloat(base,power)
    raise Exception("Cannot find suitable overload")
