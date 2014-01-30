from marketsim import registry
from marketsim.gen._intrinsic.orderbook.of_trader import _Proxy_Impl
@registry.expose(["Asset", "Proxy"])
class Proxy(_Proxy_Impl):""" 
      May be used only in objects held by orderbooks (so it is normally used in orderbook properties)
    """ 
    def __init__(self):from marketsim import rtti
        
        rtti.check_fields(self)
        _Proxy_Impl.__init__(self)
    
    @property
    def label(self):return repr(self)
    
    _properties = {
    }
    
