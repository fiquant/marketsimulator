from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IOrderGenerator
@registry.expose(["Order", "WithExpiry"])
class WithExpiry(IOrderGenerator, Observable[Order]):
    """ 
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out.order._Limit import Limit as _order_Limit
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        Observable[Order].__init__(self)
        self.expiry = expiry if expiry is not None else _constant(10.0)
        if isinstance(expiry, types.IEvent):
            event.subscribe(self.expiry, self.fire, self)
        self.proto = proto if proto is not None else _order_Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IFunction[float],
        'proto' : IOrderGenerator
    }
    def __repr__(self):
        return "WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.with_expiry import Order_Impl
        expiry = self.expiry()
        if expiry is None: return None
        
        proto = self.proto()
        if proto is None: return None
        
        return Order_Impl(expiry, proto)
    
