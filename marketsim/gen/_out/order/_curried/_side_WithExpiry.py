from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
from marketsim.gen._out._ifunction import IFunctionfloat
@registry.expose(["Order", "WithExpiry"])
class side_WithExpiry_FloatSideIObservableIOrder(IFunctionIObservableIOrderIFunctionSide):
    """ 
     WithExpiry orders can be viewed as ImmediateOrCancel orders
     where cancel order is sent not immediately but after some delay
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._side_limit import side_Limit_FloatFloat as _order__curried_side_Limit_FloatFloat
        from marketsim import rtti
        self.expiry = expiry if expiry is not None else _constant_Float(10.0)
        self.proto = proto if proto is not None else _order__curried_side_Limit_FloatFloat()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IFunctionfloat,
        'proto' : IFunctionIObservableIOrderIFunctionSide
    }
    def __repr__(self):
        return "WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.order._withexpiry import WithExpiry
        side = side if side is not None else _side_Sell_()
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(expiry, proto(side))
    
def side_WithExpiry(expiry = None,proto = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
    from marketsim import rtti
    if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
        if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSide):
            return side_WithExpiry_FloatSideIObservableIOrder(expiry,proto)
    raise Exception('Cannot find suitable overload for side_WithExpiry('+str(expiry) +':'+ str(type(expiry))+','+str(proto) +':'+ str(type(proto))+')')
