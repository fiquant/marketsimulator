from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Order", "Limit"])
class sideprice_Limit(IFunction[IOrderGenerator, IFunction[Side],IFunction[float]

]):
    """ 
    """ 
    def __init__(self, volume = None):
        from marketsim.gen._out._constant import constant
        self.volume = volume if volume is not None else constant(1.0)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'volume' : IFunction[float]
    }
    def __repr__(self):
        return "sideprice_Limit(%(volume)s)" % self.__dict__
    
    def __call__(self, side = None,price = None):
        from marketsim.gen._out.side._Sell import Sell
        from marketsim.gen._out._constant import constant
        from marketsim.gen._out.order._Limit import Limit
        side = side if side is not None else Sell()
        price = price if price is not None else constant(100.0)
        volume = self.volume
        return Limit(side, price, volume)
    
