from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionlistoffloatlistoffloat import IFunctionIFunctionlistOffloatlistOffloat
@registry.expose(["Strategy", "array_IdentityL"])
class array_IdentityL_(IFunctionIFunctionlistOffloatlistOffloat):
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
        return "array_IdentityL" % self.__dict__
    
    def __call__(self, array = None):
        from marketsim.gen._out.strategy.weight._identityl import IdentityL_ListFloat as _strategy_weight_IdentityL_ListFloat
        array = array if array is not None else []
        
        return _strategy_weight_IdentityL_ListFloat(array)
    
def array_IdentityL(): 
    from marketsim import rtti
    return array_IdentityL_()
    raise Exception('Cannot find suitable overload for array_IdentityL('++')')
