from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._intrinsic.strategy.basic import Empty_Impl
@registry.expose(["Strategy", "Empty"])
class Empty_(ISingleAssetStrategy,Empty_Impl):
    """ Empty strategy doing nothing
    
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        Empty_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    def __repr__(self):
        return "Empty" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
def Empty(): 
    from marketsim import rtti
    return Empty_()
    raise Exception('Cannot find suitable overload for Empty('++')')
