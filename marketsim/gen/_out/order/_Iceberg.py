from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import IOrderGenerator
@registry.expose(["Order", "Iceberg"])
class Iceberg(IOrderGenerator, Observable[Order]):
    """ 
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const as _const
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out.order._Limit import Limit as _order_Limit
        from marketsim import event
        from marketsim import types
        Observable[Order].__init__(self)
        self.lotSize = lotSize if lotSize is not None else _const(10.0)
        if isinstance(lotSize, types.IEvent):
            event.subscribe(self.lotSize, self.fire, self)
        self.proto = proto if proto is not None else _order_Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IObservable[float],
        'proto' : IOrderGenerator
    }
    def __repr__(self):
        return "Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.iceberg import Order_Impl
        lotSize = self.lotSize()
        if lotSize is None: return None
        
        proto = self.proto()
        if proto is None: return None
        
        return Order_Impl(lotSize, proto)
    

