# generated with class generator.python.intrinsic_function$Import
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
    
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self._ctx_ex)
                else:
                    v.bind_ex(self._ctx_ex)
        
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def Proxy(): 
    from marketsim import rtti
    return Proxy_()
    raise Exception('Cannot find suitable overload for Proxy('++')')
