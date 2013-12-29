from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import Order
@registry.expose(["Order", "ImmediateOrCancel"])
class ImmediateOrCancel(IOrderGenerator, Observable[Order]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out.order._Limit import Limit
        from marketsim import event
        from marketsim import types
        Observable[Order].__init__(self)
        self.proto = proto if proto is not None else Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IObservable[Order]
        
    }
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.ioc import ImmediateOrCancel_Impl
        proto = self.proto()
        if proto is None: return None
        
        return ImmediateOrCancel_Impl(proto)
    

