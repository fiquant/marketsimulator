from marketsim import registry
from marketsim.gen._intrinsic.strategy.arbitrage import _Arbitrage_Impl
@registry.expose(["Strategy", "Arbitrage"])
class Arbitrage(_Arbitrage_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        _Arbitrage_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "Arbitrage" % self.__dict__
    
