from marketsim import registry
from marketsim import IFunction
from marketsim import float
@registry.expose(["Strategy", "f_IdentityF"])
class f_IdentityF_(IFunction[IFunction[float], IFunction[float]]):
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
        return "f_IdentityF" % self.__dict__
    
    def __call__(self, f = None):
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim.gen._out.strategy.weight._identityf import IdentityF_IFunctionFloat as _strategy_weight_IdentityF
        f = f if f is not None else _constant(1.0)
        
        return _strategy_weight_IdentityF(f)
    
def f_IdentityF(): 
    from marketsim import rtti
    return f_IdentityF_()
    raise Exception('Cannot find suitable overload for f_IdentityF('++')')
