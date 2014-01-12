from marketsim import registry
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "FloatingPrice"])
class sidevolume_FloatingPrice(



IFunction[IOrderGenerator,IFunction[Side],IFunction[float]]):
    """ 
    """ 
    def __init__(self, floatingPrice = None, proto = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._curried._sidevolume_price_Limit import sidevolume_price_Limit as _order__curried_sidevolume_price_Limit
        self.floatingPrice = floatingPrice if floatingPrice is not None else _constant(10.0)
        self.proto = proto if proto is not None else _order__curried_sidevolume_price_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'floatingPrice' : IFunction[float],
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side],IFunction[float]
        
        ]
    }
    def __repr__(self):
        return "sidevolume_FloatingPrice(%(floatingPrice)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.order._FloatingPrice import FloatingPrice
        floatingPrice = self.floatingPrice
        proto = self.proto
        return FloatingPrice(floatingPrice, proto(side,volume))
    
