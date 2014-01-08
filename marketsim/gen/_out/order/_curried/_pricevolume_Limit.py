from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
@registry.expose(["Order", "Limit"])
class pricevolume_Limit(IFunction[IOrderGenerator, IFunction[float],IFunction[float]
]):
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
        return "pricevolume_Limit(%(side)s)" % self.__dict__
    
    def __call__(self, price = None,volume = None):
        from marketsim.gen._out._constant import constant
        from marketsim.gen._out._constant import constant
        from marketsim.gen._out.order._Limit import Limit
        price = price if price is not None else constant(100.0)
        volume = volume if volume is not None else constant(1.0)
        side = self.side
        return Limit(side, price, volume)
    
