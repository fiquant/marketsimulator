from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "WithExpiry"])
class sidevolume_WithExpiry(IFunction[IOrderGenerator,IFunction[Side]
,IFunction[float]]):
    """ 
     WithExpiry orders can be viewed as ImmediateOrCancel orders
     where cancel order is sent not immediately but after some delay
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._curried._sidevolume_Limit import sidevolume_Limit as _order__curried_sidevolume_Limit
        from marketsim import rtti
        self.expiry = expiry if expiry is not None else _constant(10.0)
        self.proto = proto if proto is not None else _order__curried_sidevolume_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IFunction[float],
        'proto' : IFunction[IOrderGenerator, IFunction[Side],IFunction[float]]
    }
    def __repr__(self):
        return "WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._WithExpiry import WithExpiry
        side = side if side is not None else _side_Sell()
        volume = volume if volume is not None else _constant(1.0)
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(expiry, proto(side,volume))
    
