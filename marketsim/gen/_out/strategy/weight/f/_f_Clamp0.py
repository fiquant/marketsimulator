from marketsim import registry
from marketsim import IFunction
from marketsim import float
@registry.expose(["Strategy", "f_Clamp0"])
class f_Clamp0_(IFunction[IFunction[float], IFunction[float]]):
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
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim.gen._out.strategy.weight._clamp0 import Clamp0_IFunctionFloat as _strategy_weight_Clamp0
        f = f if f is not None else _constant(1.0)
        
        return _strategy_weight_Clamp0(f)
    
def f_Clamp0(): 
    from marketsim import rtti
    return f_Clamp0_()
    raise Exception('Cannot find suitable overload for f_Clamp0('++')')
