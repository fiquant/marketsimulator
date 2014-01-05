from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import IObservable
from marketsim import Order
@registry.expose(["Order", "WithExpiry"])
class WithExpiry(IOrderGenerator, Observable[Order]):
    """ 
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out.order._Limit import Limit
        from marketsim import event
        from marketsim import types
        Observable[Order].__init__(self)
        self.expiry = expiry if expiry is not None else const(10.0)
        if isinstance(expiry, types.IEvent):
            event.subscribe(self.expiry, self.fire, self)
        self.proto = proto if proto is not None else Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IObservable[float],
        'proto' : IObservable[Order]
        
    }
    def __repr__(self):
        return "WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.with_expiry import WithExpiry_Impl
        expiry = self.expiry()
        if expiry is None: return None
        
        proto = self.proto()
        if proto is None: return None
        
        return WithExpiry_Impl(expiry, proto)
    

