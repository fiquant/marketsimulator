from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import float
from marketsim import IFunction
@registry.expose(["Order", "WithExpiry"])
class volume_WithExpiry_IFunctionFloatFloatIOrderGenerator(IFunction[IOrderGenerator,IFunction[float]]):
    """ 
     WithExpiry orders can be viewed as ImmediateOrCancel orders
     where cancel order is sent not immediately but after some delay
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._volume_limit import volume_Limit_SideIFunctionFloat as _order__curried_volume_Limit_SideIFunctionFloat
        from marketsim import rtti
        self.expiry = expiry if expiry is not None else _constant_Float(10.0)
        self.proto = proto if proto is not None else _order__curried_volume_Limit_SideIFunctionFloat()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IFunction[float],
        'proto' : IFunction[IOrderGenerator, IFunction[float]]
    }
    def __repr__(self):
        return "WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._withexpiry import WithExpiry
        volume = volume if volume is not None else _constant_Float(1.0)
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(expiry, proto(volume))
    
def volume_WithExpiry(expiry = None,proto = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import rtti
    if expiry is None or rtti.can_be_casted(expiry, IFunction[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
            return volume_WithExpiry_IFunctionFloatFloatIOrderGenerator(expiry,proto)
    raise Exception('Cannot find suitable overload for volume_WithExpiry('+str(expiry)+','+str(proto)+')')
