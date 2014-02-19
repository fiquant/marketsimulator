from marketsim import registry
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable import ObservableSide
from marketsim.gen._intrinsic.side import _Sell_Impl
@registry.expose(["Side", "observableSell"])
class observableSell_(ObservableSide,_Sell_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._observable import ObservableSide
        from marketsim import rtti
        ObservableSide.__init__(self)
        
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
