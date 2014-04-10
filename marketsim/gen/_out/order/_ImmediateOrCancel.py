from marketsim import registry
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._observable._observableiorder import ObservableIOrder
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
@registry.expose(["Order", "ImmediateOrCancel"])
class ImmediateOrCancel_IObservableIOrder(ObservableIOrder,IObservableIOrder):
    """ **Factory creating Immediate-Or-Cancel orders**
    
    
      Immediate-Or-Cancel order sends an underlying order to the market and
      immediately sends a cancel request for it.
      It allows to combine market and limit order behaviour:
      the order is either executed immediately
      at price equal or better than given one
      either it is cancelled (and consequently never stored in the order queue).
    
    Parameters are:
    
    **proto**
    	 factory for underlying orders 
    """ 
    def __init__(self, proto = None):
        from marketsim import rtti
        from marketsim.gen._out._iorder import IOrder
        from marketsim.gen._out.order._limit import Limit_SideFloatFloat as _order_Limit_SideFloatFloat
        from marketsim.gen._out._observable._observableiorder import ObservableIOrder
        from marketsim import deref_opt
        ObservableIOrder.__init__(self)
        self.proto = proto if proto is not None else deref_opt(_order_Limit_SideFloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IObservableIOrder
    }
    
    
    def on_proto_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'proto', value)
    
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        self.proto.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.ioc import Order_Impl
        proto = self.proto()
        if proto is None: return None
        
        return Order_Impl(proto)
    
def ImmediateOrCancel(proto = None): 
    from marketsim.gen._out._iorder import IOrder
    from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IObservableIOrder):
        return ImmediateOrCancel_IObservableIOrder(proto)
    raise Exception('Cannot find suitable overload for ImmediateOrCancel('+str(proto) +':'+ str(type(proto))+')')
