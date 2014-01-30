from marketsim import registry
from marketsim.gen._intrinsic.strategy.basic import _Empty_Impl
@registry.expose(["Strategy", "Empty"])
class Empty(_Empty_Impl):
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
    
