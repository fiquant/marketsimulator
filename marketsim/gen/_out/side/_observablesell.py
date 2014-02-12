from marketsim import registry
from marketsim import Side
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.side import _Sell_Impl
@registry.expose(["Side", "observableSell"])
class observableSell_(Observable[Side],_Sell_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim import rtti
        Observable[Side].__init__(self)
        
        rtti.check_fields(self)
        _Sell_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "observableSell" % self.__dict__
    
def observableSell(): 
    from marketsim import rtti
    return observableSell_()
    raise Exception('Cannot find suitable overload for observableSell('++')')
