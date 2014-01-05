from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "Market"])
class side_Market(IFunction[IOrderGenerator, types.IFunction[Side]
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
        return "side_Market(%(volume)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._Sell import Sell
        from marketsim.gen._out.order._Market import Market
        side = side if side is not None else Sell()
        volume = self.volume
        return Market(side, volume)
    
