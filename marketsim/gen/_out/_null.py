from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._intrinsic._constant import Null_Impl
@registry.expose(["Basic", "null"])
class null_(IFunctionfloat,Null_Impl):
    """ Trivial observable always returning *undefined* or *None* value
    
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        Null_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    def __repr__(self):
        return "null" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
def null(): 
    from marketsim import rtti
    return null_()
    raise Exception('Cannot find suitable overload for null('++')')
