from marketsim import registry
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
@registry.expose(["Order", "WithExpiry"])
class price_WithExpiry(

IFunction[IOrderGenerator,IFunction[float]]):
    """ 
     WithExpiry orders can be viewed as ImmediateOrCancel orders
     where cancel order is sent not immediately but after some delay
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._curried._price_Limit import price_Limit as _order__curried_price_Limit
        from marketsim import rtti
        self.expiry = expiry if expiry is not None else _constant(10.0)
        self.proto = proto if proto is not None else _order__curried_price_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IFunction[float],
        'proto' : IFunction[IOrderGenerator, IFunction[float]]
    }
    def __repr__(self):
        return "price_WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, price = None):
        from marketsim.gen._out.order._WithExpiry import WithExpiry
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(expiry, proto(price))
    
