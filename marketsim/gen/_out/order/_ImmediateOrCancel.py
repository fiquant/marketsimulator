from marketsim import registry
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IOrderGenerator
@registry.expose(["Order", "ImmediateOrCancel"])
class ImmediateOrCancel_IOrderGenerator(Observable[Order],IOrderGenerator):
    """ 
      Immediate-Or-Cancel order sends an underlying order to the market and
      immediately sends a cancel request for it.
      It allows to combine market and limit order behaviour:
      the order is either executed immediately
      at price equal or better than given one
      either it is cancelled (and consequently never stored in the order queue).
    """ 
    def __init__(self, proto = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.order._limit import Limit_SideIFunctionFloatIFunctionFloat as _order_Limit
        from marketsim import event
        from marketsim import Order
        Observable[Order].__init__(self)
        self.proto = proto if proto is not None else _order_Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IOrderGenerator
    }
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.ioc import Order_Impl
        proto = self.proto()
        if proto is None: return None
        
        return Order_Impl(proto)
    
def ImmediateOrCancel(proto = None): 
    from marketsim import IOrderGenerator
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IOrderGenerator):
        return ImmediateOrCancel_IOrderGenerator(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto)+')')
