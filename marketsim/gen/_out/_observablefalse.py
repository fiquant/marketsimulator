from marketsim import registry
from marketsim.gen._out._observable import Observablebool
from marketsim.gen._intrinsic._constant import _False_Impl
@registry.expose(["Basic", "observableFalse"])
class observableFalse_(Observablebool,_False_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim.gen._out._observable import Observablebool
        from marketsim import rtti
        Observablebool.__init__(self)
        
        rtti.check_fields(self)
        _False_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "False" % self.__dict__
    
def observableFalse(): 
    from marketsim import rtti
    return observableFalse_()
    raise Exception('Cannot find suitable overload for observableFalse('++')')
