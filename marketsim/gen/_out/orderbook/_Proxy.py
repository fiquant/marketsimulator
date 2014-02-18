from marketsim import registry
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._intrinsic.orderbook.of_trader import _Proxy_Impl
@registry.expose(["Asset", "Proxy"])
class Proxy_(IOrderBook,_Proxy_Impl):
    """ 
      May be used only in objects held by orderbooks (so it is normally used in orderbook properties)
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        _Proxy_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
def Proxy(): 
    from marketsim import rtti
    return Proxy_()
    raise Exception('Cannot find suitable overload for Proxy('++')')
