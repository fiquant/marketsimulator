from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import float
from marketsim import IFunction
from marketsim import float
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "Limit"])
class volume_price_Limit(IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[float]]):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self, side = None):
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim import rtti
        self.side = side if side is not None else _side_Sell()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunction[Side]
    }
    def __repr__(self):
        return "Limit(%(side)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._curried._price_Limit import price_Limit
        volume = volume if volume is not None else _constant(1.0)
        side = self.side
        return price_Limit(side, volume)
    
volume_price_Limit = volume_price_Limit
