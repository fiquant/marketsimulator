from marketsim import registry
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._intrinsic.orderbook.of_trader import Proxy_Impl
@registry.expose(["Asset", "Proxy"])
class Proxy_(IOrderBook,Proxy_Impl):
    """ **Phantom orderbook that is used to refer to the current order book**
    
    
      May be used only in objects held by orderbooks (so it is normally used in orderbook properties)
    
    Parameters are:
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        Proxy_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        delattr(self, '_processing_ex')
    
def Proxy(): 
    from marketsim import rtti
    return Proxy_()
    raise Exception('Cannot find suitable overload for Proxy('++')')
