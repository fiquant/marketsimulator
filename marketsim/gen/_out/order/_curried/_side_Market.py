from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
@registry.expose(["Order", "Market"])
class side_Market(IFunction[IOrderGenerator, IFunction[Side]]):
    """ 
      Market order intructs buy or sell given volume immediately
    """ 
    def __init__(self, volume = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        self.volume = volume if volume is not None else _constant(1.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'volume' : IFunction[float]
    }
    def __repr__(self):
        return "side_Market(%(volume)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out.order._Market import Market
        side = side if side is not None else _side_Sell()
        volume = self.volume
        return Market(side, volume)
    
