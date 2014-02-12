from marketsim import registry
from marketsim import bool
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic._constant import _False_Impl
@registry.expose(["Basic", "observableFalse"])
class observableFalse_(Observable[bool],_False_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim import bool
        from marketsim.ops._all import Observable
        from marketsim import rtti
        Observable[bool].__init__(self)
        
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
