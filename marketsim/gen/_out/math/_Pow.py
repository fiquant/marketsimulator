# generated with class generator.python.mathops$Import
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Log/Pow", "Pow"])
class Pow_FloatFloat(Observablefloat):
    """ **Return *x* raised to the power *y*.**
    
    
     Exceptional cases follow Annex F of the C99 standard as far as possible.
     In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
     even when *x* is a zero or a NaN.
     If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
     ``pow(x, y)`` is undefined, and raises ``ValueError``.
    
    Parameters are:
    
    **base**
    
    **power**
    """ 
    def __init__(self, base = None, power = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.base = base if base is not None else deref_opt(_constant_Float(1.0))
        self.power = power if power is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'base' : IFunctionfloat,
        'power' : IFunctionfloat
    }
    
    
    
    
    
    
    def __repr__(self):
        return "%(base)s^{%(power)s}" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.base.bind_ex(self._ctx_ex)
        self.power.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.base.reset_ex(generation)
        self.power.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, *args, **kwargs):
        import math
        base = self.base()
        if base is None: return None
        power = self.power()
        if power is None: return None
        return math.pow(base, power)
    
def Pow(base = None,power = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if base is None or rtti.can_be_casted(base, IFunctionfloat):
        if power is None or rtti.can_be_casted(power, IFunctionfloat):
            return Pow_FloatFloat(base,power)
    raise Exception('Cannot find suitable overload for Pow('+str(base) +':'+ str(type(base))+','+str(power) +':'+ str(type(power))+')')
