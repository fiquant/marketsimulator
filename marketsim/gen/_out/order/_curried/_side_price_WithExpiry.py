from marketsim import registry
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
@registry.expose(["Order", "WithExpiry"])
class side_price_WithExpiry(




IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]]):
    """ 
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.order._curried._side_price_Limit import side_price_Limit as _order__curried_side_price_Limit
        self.expiry = expiry if expiry is not None else _const(10.0)
        self.proto = proto if proto is not None else _order__curried_side_price_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IObservable[float],
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side]
        ]
    }
    def __repr__(self):
        return "side_price_WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.order._curried._price_WithExpiry import price_WithExpiry
        expiry = self.expiry
        proto = self.proto
        return price_WithExpiry(expiry, proto(side))
    
