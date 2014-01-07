from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import types
from marketsim import Side
@registry.expose(["Order", "Market"])
class volume_Market(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
    """ 
    def __init__(self, side = None):
        from marketsim.gen._out.side._Sell import Sell
        self.side = side if side is not None else Sell()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunction[Side]
        
    }
    def __repr__(self):
        return "volume_Market(%(side)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant
        from marketsim.gen._out.order._Market import Market
        volume = volume if volume is not None else constant(1.0)
        side = self.side
        return Market(side, volume)
    
