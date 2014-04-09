from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_ifunctionfloat import IFunctionIFunctionfloat_from_IFunctionfloat
@registry.expose(["Strategy", "f_IdentityF"])
class f_IdentityF_(IFunctionIFunctionfloat_from_IFunctionfloat):
    """ **identity scaling = f(x)**
    
    
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
        return "f_IdentityF" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def __call__(self, f = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim.gen._out.strategy.weight._identityf import IdentityF_Float as _strategy_weight_IdentityF_Float
        f = f if f is not None else deref_opt(_constant_Float(1.0))
        
        return _strategy_weight_IdentityF_Float(f)
    
def f_IdentityF(): 
    from marketsim import rtti
    return f_IdentityF_()
    raise Exception('Cannot find suitable overload for f_IdentityF('++')')
