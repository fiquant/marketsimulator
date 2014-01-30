from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
@registry.expose(["Order", "Market"])
class volume_Market(IFunction[IOrderGenerator, IFunction[float]]):""" 
      Market order intructs buy or sell given volume immediately
    """ 
    def __init__(self, side = None):from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim import rtti
        self.side = side if side is not None else _side_Sell()
        rtti.check_fields(self)
    
    @property
    def label(self):return repr(self)
    
    _properties = {'side' : IFunction[Side]
        
    }
    def __repr__(self):return "volume_Market(%(side)s)" % self.__dict__
    
    def __call__(self, volume = None):from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._Market import Market
        volume = volume if volume is not None else _constant(1.0)
        side = self.side
        return Market(side, volume)
    
