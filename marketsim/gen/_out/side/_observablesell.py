from marketsim import registry
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._intrinsic.side import Sell_Impl
@registry.expose(["Side", "observableSell"])
class observableSell_(ObservableSide,Sell_Impl):
    """ Observable always equal to Sell side
    
    """ 
    def __init__(self):
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import rtti
        ObservableSide.__init__(self)
        
        rtti.check_fields(self)
        Sell_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    def __repr__(self):
        return "observableSell" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
def observableSell(): 
    from marketsim import rtti
    return observableSell_()
    raise Exception('Cannot find suitable overload for observableSell('++')')
