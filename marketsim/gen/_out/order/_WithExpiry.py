from marketsim.ops._all import Observable
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim import registry
@registry.expose(["Order", "WithExpiry"])
class WithExpiry_FloatIObservableIOrder(Observable[IOrder],IObservableIOrder):
    """ 
     WithExpiry orders can be viewed as ImmediateOrCancel orders
     where cancel order is sent not immediately but after some delay
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim.gen._out.order._limit import Limit_SideFloatFloat as _order_Limit_SideFloatFloat
        from marketsim.ops._all import Observable
        from marketsim.gen._out._iorder import IOrder
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import event
        Observable[IOrder].__init__(self)
        self.expiry = expiry if expiry is not None else _constant_Float(10.0)
        
        self.proto = proto if proto is not None else _order_Limit_SideFloatFloat()
        event.subscribe(self.proto, self.fire, self)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IFunctionfloat,
        'proto' : IObservableIOrder
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
    
def WithExpiry(expiry = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._iorder import IOrder
    from marketsim.gen._out._iobservable import IObservableIOrder
    from marketsim import rtti
    if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IObservableIOrder):
            return WithExpiry_FloatIObservableIOrder(expiry,proto)
    raise Exception('Cannot find suitable overload for WithExpiry('+str(expiry) +':'+ str(type(expiry))+','+str(proto) +':'+ str(type(proto))+')')
