# generated with class generator.python.order_factory_on_proto$PartialFactory
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat import IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "WithExpiry"])
class sideprice_WithExpiry_SideFloatIObservableIOrderFloat(IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat):
    """ **Factory creating WithExpiry orders**
    
    
     WithExpiry orders can be viewed as ImmediateOrCancel orders
     where cancel order is sent not immediately but after some delay
    
    Parameters are:
    
    **proto**
    	 underlying orders to create 
    
    **expiry**
    	 expiration period for orders 
    """ 
    def __init__(self, proto = None, expiry = None):
        from marketsim.gen._out.order._curried._sideprice_limit import sideprice_Limit_Float as _order__curried_sideprice_Limit_Float
        from marketsim import deref_opt
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else deref_opt(_order__curried_sideprice_Limit_Float())
        self.expiry = expiry if expiry is not None else deref_opt(_constant_Float(10.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat,
        'expiry' : IFunctionfloat
    }
    
    
    
    
    def __repr__(self):
        return "WithExpiry(%(proto)s, %(expiry)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if getattr(self, '_processing_ex', False):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        self.proto.bind_ex(self._ctx_ex)
        self.expiry.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self._processing_ex = False
    
    def __call__(self, side = None,price = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import deref_opt
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._withexpiry import WithExpiry
        side = side if side is not None else deref_opt(_side_Sell_())
        price = price if price is not None else deref_opt(_constant_Float(100.0))
        proto = self.proto
        expiry = self.expiry
        return WithExpiry(proto(side,price), expiry)
    
def sideprice_WithExpiry(proto = None,expiry = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat import IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat):
        if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
            return sideprice_WithExpiry_SideFloatIObservableIOrderFloat(proto,expiry)
    raise Exception('Cannot find suitable overload for sideprice_WithExpiry('+str(proto) +':'+ str(type(proto))+','+str(expiry) +':'+ str(type(expiry))+')')
