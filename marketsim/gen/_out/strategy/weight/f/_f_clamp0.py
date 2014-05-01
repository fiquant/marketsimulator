# generated with class generator.python.curried$after_typing$Curried
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_ifunctionfloat import IFunctionIFunctionfloat_from_IFunctionfloat
@registry.expose(["Strategy", "f_Clamp0"])
class f_Clamp0_(IFunctionIFunctionfloat_from_IFunctionfloat):
    """ **scaling function = max(0, f(x)) + 1**
    
    
    Parameters are:
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    def __repr__(self):
        return "f_Clamp0" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, f = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim.gen._out.strategy.weight._clamp0 import Clamp0_Float as _strategy_weight_Clamp0_Float
        f = f if f is not None else deref_opt(_constant_Float(1.0))
        
        return _strategy_weight_Clamp0_Float(f)
    
def f_Clamp0(): 
    from marketsim import rtti
    return f_Clamp0_()
    raise Exception('Cannot find suitable overload for f_Clamp0('++')')
