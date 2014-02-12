from marketsim import registry
from marketsim import Side
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.side import _Buy_Impl
@registry.expose(["Side", "observableBuy"])
class observableBuy_(Observable[Side],_Buy_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim import rtti
        Observable[Side].__init__(self)
        
        rtti.check_fields(self)
        _Buy_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "observableBuy" % self.__dict__
    
def observableBuy(): 
    from marketsim import rtti
    return observableBuy_()
    raise Exception('Cannot find suitable overload for observableBuy('++')')
