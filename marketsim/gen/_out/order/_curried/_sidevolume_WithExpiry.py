from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction import IFunctionfloat
@registry.expose(["Order", "WithExpiry"])
class sidevolume_WithExpiry_FloatSideFloatIObservableIOrder(IFunctionIObservableIOrderIFunctionSideIFunctionfloat):
    """ 
     WithExpiry orders can be viewed as ImmediateOrCancel orders
     where cancel order is sent not immediately but after some delay
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._sidevolume_limit import sidevolume_Limit_Float as _order__curried_sidevolume_Limit_Float
        from marketsim import rtti
        self.expiry = expiry if expiry is not None else _constant_Float(10.0)
        self.proto = proto if proto is not None else _order__curried_sidevolume_Limit_Float()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IFunctionfloat,
        'proto' : IFunctionIObservableIOrderIFunctionSideIFunctionfloat
    }
    def __repr__(self):
        return "WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._withexpiry import WithExpiry
        side = side if side is not None else _side_Sell_()
        volume = volume if volume is not None else _constant_Float(1.0)
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(expiry, proto(side,volume))
    
def sidevolume_WithExpiry(expiry = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSideIFunctionfloat
    from marketsim import rtti
    if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSideIFunctionfloat):
            return sidevolume_WithExpiry_FloatSideFloatIObservableIOrder(expiry,proto)
    raise Exception('Cannot find suitable overload for sidevolume_WithExpiry('+str(expiry) +':'+ str(type(expiry))+','+str(proto) +':'+ str(type(proto))+')')
