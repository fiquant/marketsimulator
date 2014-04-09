from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside import IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "price_WithExpiry"])
class side_price_WithExpiry_SideFloatIObservableIOrderFloat(IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide):
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
        from marketsim.gen._out.order._curried._side_price_limit import side_price_Limit_Float as _order__curried_side_price_Limit_Float
        from marketsim import deref_opt
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else deref_opt(_order__curried_side_price_Limit_Float())
        self.expiry = expiry if expiry is not None else deref_opt(_constant_Float(10.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide,
        'expiry' : IFunctionfloat
    }
    
    
    
    
    def __repr__(self):
        return "price_WithExpiry(%(proto)s, %(expiry)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim import deref_opt
        from marketsim.gen._out.order._curried._price_withexpiry import price_WithExpiry
        side = side if side is not None else deref_opt(_side_Sell_())
        proto = self.proto
        expiry = self.expiry
        return price_WithExpiry(proto(side), expiry)
    
def side_price_WithExpiry(proto = None,expiry = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionside import IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionSide):
        if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
            return side_price_WithExpiry_SideFloatIObservableIOrderFloat(proto,expiry)
    raise Exception('Cannot find suitable overload for side_price_WithExpiry('+str(proto) +':'+ str(type(proto))+','+str(expiry) +':'+ str(type(expiry))+')')
