from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorderifunctionfloatifunctionfloat import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "price_WithExpiry"])
class volume_price_WithExpiry_FloatFloatIObservableIOrderFloat(IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat):
    """ 
     WithExpiry orders can be viewed as ImmediateOrCancel orders
     where cancel order is sent not immediately but after some delay
    """ 
    def __init__(self, proto = None, expiry = None):
        from marketsim.gen._out.order._curried._volume_price_limit import volume_price_Limit_Side as _order__curried_volume_price_Limit_Side
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_volume_price_Limit_Side()
        self.expiry = expiry if expiry is not None else _constant_Float(10.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat,
        'expiry' : IFunctionfloat
    }
    def __repr__(self):
        return "price_WithExpiry(%(proto)s, %(expiry)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._price_withexpiry import price_WithExpiry
        volume = volume if volume is not None else _constant_Float(1.0)
        proto = self.proto
        expiry = self.expiry
        return price_WithExpiry(proto(volume), expiry)
    
def volume_price_WithExpiry(proto = None,expiry = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorderifunctionfloatifunctionfloat import IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrderIFunctionfloatIFunctionfloat):
        if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
            return volume_price_WithExpiry_FloatFloatIObservableIOrderFloat(proto,expiry)
    raise Exception('Cannot find suitable overload for volume_price_WithExpiry('+str(proto) +':'+ str(type(proto))+','+str(expiry) +':'+ str(type(expiry))+')')
