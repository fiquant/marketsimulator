from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "WithExpiry"])
class side_WithExpiry_SideIObservableIOrderFloat(IFunctionIObservableIOrderIFunctionSide):
    """ 
     WithExpiry orders can be viewed as ImmediateOrCancel orders
     where cancel order is sent not immediately but after some delay
    """ 
    def __init__(self, proto = None, expiry = None):
        from marketsim.gen._out.order._curried._side_limit import side_Limit_FloatFloat as _order__curried_side_Limit_FloatFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_side_Limit_FloatFloat()
        self.expiry = expiry if expiry is not None else _constant_Float(10.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrderIFunctionSide,
        'expiry' : IFunctionfloat
    }
    def __repr__(self):
        return "WithExpiry(%(proto)s, %(expiry)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.order._withexpiry import WithExpiry
        side = side if side is not None else _side_Sell_()
        proto = self.proto
        expiry = self.expiry
        return WithExpiry(proto(side), expiry)
    
def side_WithExpiry(proto = None,expiry = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSide):
        if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
            return side_WithExpiry_SideIObservableIOrderFloat(proto,expiry)
    raise Exception('Cannot find suitable overload for side_WithExpiry('+str(proto) +':'+ str(type(proto))+','+str(expiry) +':'+ str(type(expiry))+')')
