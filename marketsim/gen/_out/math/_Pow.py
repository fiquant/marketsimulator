from marketsim import registry
from marketsim.gen._out._observable import Observablefloat
from marketsim.gen._out._ifunction import IFunctionfloat
@registry.expose(["Log/Pow", "Pow"])
class Pow_FloatFloat(Observablefloat):
    """ 
     Exceptional cases follow Annex F of the C99 standard as far as possible.
     In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
     even when *x* is a zero or a NaN.
     If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
     ``pow(x, y)`` is undefined, and raises ``ValueError``.
    """ 
    def __init__(self, base = None, power = None):
        from marketsim.gen._out._observable import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.base = base if base is not None else _constant_Float(1.0)
        
        self.power = power if power is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'base' : IFunctionfloat,
        'power' : IFunctionfloat
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
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if base is None or rtti.can_be_casted(base, IFunctionfloat):
        if power is None or rtti.can_be_casted(power, IFunctionfloat):
            return Pow_FloatFloat(base,power)
    raise Exception('Cannot find suitable overload for Pow('+str(base) +':'+ str(type(base))+','+str(power) +':'+ str(type(power))+')')
