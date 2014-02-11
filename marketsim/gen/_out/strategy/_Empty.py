from marketsim import registry
from marketsim.gen._intrinsic.strategy.basic import _Empty_Impl
@registry.expose(["Strategy", "Empty"])
class Empty_(_Empty_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        _Empty_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "Empty" % self.__dict__
    
def Empty(): 
    from marketsim import rtti
    return Empty_()
    raise Exception('Cannot find suitable overload for Empty('++')')
