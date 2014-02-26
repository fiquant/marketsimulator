from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionsideifunctionfloat import IFunctionIObservableIOrderIFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Order", "WithExpiry"])
class sideprice_WithExpiry_SideFloatIObservableIOrderFloat(IFunctionIObservableIOrderIFunctionSideIFunctionfloat):
    """ 
     WithExpiry orders can be viewed as ImmediateOrCancel orders
     where cancel order is sent not immediately but after some delay
    """ 
    def __init__(self, proto = None, expiry = None):
        from marketsim.gen._out.order._curried._sideprice_limit import sideprice_Limit_Float as _order__curried_sideprice_Limit_Float
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_sideprice_Limit_Float()
        self.expiry = expiry if expiry is not None else _constant_Float(10.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunctionIObservableIOrderIFunctionSideIFunctionfloat,
        'expiry' : IFunctionfloat
    }
    def __repr__(self):
        return "WithExpiry(%(proto)s, %(expiry)s)" % self.__dict__
    
    def __call__(self, side = None,price = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._withexpiry import WithExpiry
        side = side if side is not None else _side_Sell_()
        price = price if price is not None else _constant_Float(100.0)
        proto = self.proto
        expiry = self.expiry
        return WithExpiry(proto(side,price), expiry)
    
def sideprice_WithExpiry(proto = None,expiry = None): 
    from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionsideifunctionfloat import IFunctionIObservableIOrderIFunctionSideIFunctionfloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIObservableIOrderIFunctionSideIFunctionfloat):
        if expiry is None or rtti.can_be_casted(expiry, IFunctionfloat):
            return sideprice_WithExpiry_SideFloatIObservableIOrderFloat(proto,expiry)
    raise Exception('Cannot find suitable overload for sideprice_WithExpiry('+str(proto) +':'+ str(type(proto))+','+str(expiry) +':'+ str(type(expiry))+')')
