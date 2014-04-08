def identityL(): 
    from marketsim.gen._out.strategy.weight.array._array_identityl import array_IdentityL_ as _strategy_weight_array_array_IdentityL_
    from marketsim import rtti
    return _strategy_weight_array_array_IdentityL_()
    raise Exception('Cannot find suitable overload for identityL('++')')
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionlistoffloat import IFunctionlistOffloat
from marketsim.gen._intrinsic.strategy.weight import Identity_Impl
from marketsim import listOf
@registry.expose(["Strategy", "IdentityL"])
class IdentityL_ListFloat(IFunctionlistOffloat,Identity_Impl):
    """ Identity function for an array of floats
    
    """ 
    def __init__(self, array = None):
        from marketsim import rtti
        self.array = array if array is not None else []
        rtti.check_fields(self)
        Identity_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'array' : listOf(float)
    }
    
    
    def __repr__(self):
        return "IdentityL(%(array)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
def IdentityL(array = None): 
    from marketsim import listOf
    from marketsim import rtti
    if array is None or rtti.can_be_casted(array, listOf(float)):
        return IdentityL_ListFloat(array)
    raise Exception('Cannot find suitable overload for IdentityL('+str(array) +':'+ str(type(array))+')')
