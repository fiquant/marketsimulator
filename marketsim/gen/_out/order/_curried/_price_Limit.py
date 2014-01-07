from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import types
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "Limit"])
class price_Limit(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
    """ 
    def __init__(self, side = None, volume = None):
        from marketsim.gen._out.side._Sell import Sell
        from marketsim.gen._out._constant import constant
        self.side = side if side is not None else Sell()
        self.volume = volume if volume is not None else constant(1.0)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunction[Side]
        ,
        'volume' : IFunction[float]
    }
    def __repr__(self):
        return "price_Limit(%(side)s, %(volume)s)" % self.__dict__
    
    def __call__(self, price = None):
        from marketsim.gen._out._constant import constant
        from marketsim.gen._out.order._Limit import Limit
        price = price if price is not None else constant(100.0)
        side = self.side
        volume = self.volume
        return Limit(side, price, volume)
    
