from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import types
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "Limit"])
class volume_Limit(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
    """ 
    def __init__(self, side = None, price = None):
        from marketsim.gen._out.side._Sell import Sell
        from marketsim.gen._out._constant import constant
        self.side = side if side is not None else Sell()
        self.price = price if price is not None else constant(100.0)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunction[Side]
        ,
        'price' : IFunction[float]
    }
    def __repr__(self):
        return "volume_Limit(%(side)s, %(price)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant
        from marketsim.gen._out.order._Limit import Limit
        volume = volume if volume is not None else constant(1.0)
        side = self.side
        price = self.price
        return Limit(side, price, volume)
    
