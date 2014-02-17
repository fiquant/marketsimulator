from marketsim import registry
from marketsim import Side
from marketsim import IFunction
from marketsim.gen._intrinsic.side import _None_Impl
@registry.expose(["Side", "Nothing"])
class Nothing_(IFunction[Side],_None_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        _None_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "Nothing" % self.__dict__
    
def Nothing(): 
    from marketsim import rtti
    return Nothing_()
    raise Exception('Cannot find suitable overload for Nothing('++')')
