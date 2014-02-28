from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_ifunctionfloat import IFunctionIFunctionfloat_from_IFunctionfloat
@registry.expose(["Strategy", "f_Clamp0"])
class f_Clamp0_(IFunctionIFunctionfloat_from_IFunctionfloat):
    """ 
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
        return "f_Clamp0" % self.__dict__
    
    def __call__(self, f = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import call
        from marketsim.gen._out.strategy.weight._clamp0 import Clamp0_Float as _strategy_weight_Clamp0_Float
        f = f if f is not None else call(_constant_Float,1.0)
        
        return _strategy_weight_Clamp0_Float(f)
    
def f_Clamp0(): 
    from marketsim import rtti
    return f_Clamp0_()
    raise Exception('Cannot find suitable overload for f_Clamp0('++')')
