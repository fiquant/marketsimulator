from marketsim import registry
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._intrinsic.side import Buy_Impl
@registry.expose(["Side", "observableBuy"])
class observableBuy_(ObservableSide,Buy_Impl):
    """ Observable always equal to Buy side
    
    """ 
    def __init__(self):
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import rtti
        ObservableSide.__init__(self)
        
        rtti.check_fields(self)
        Buy_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    def __repr__(self):
        return "observableBuy" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
def observableBuy(): 
    from marketsim import rtti
    return observableBuy_()
    raise Exception('Cannot find suitable overload for observableBuy('++')')
