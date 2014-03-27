from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionlistoffloat_from_listoffloat import IFunctionIFunctionlistOffloat_from_listOffloat
@registry.expose(["Strategy", "array_IdentityL"])
class array_IdentityL_(IFunctionIFunctionlistOffloat_from_listOffloat):
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
        return "array_IdentityL" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
    def __call__(self, array = None):
        from marketsim.gen._out.strategy.weight._identityl import IdentityL_ListFloat as _strategy_weight_IdentityL_ListFloat
        array = array if array is not None else []
        
        return _strategy_weight_IdentityL_ListFloat(array)
    
def array_IdentityL(): 
    from marketsim import rtti
    return array_IdentityL_()
    raise Exception('Cannot find suitable overload for array_IdentityL('++')')
