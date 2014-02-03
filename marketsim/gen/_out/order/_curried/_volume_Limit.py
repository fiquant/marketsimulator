from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import float
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
@registry.expose(["Order", "Limit"])
class volume_Limit(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self, side = None, price = None):
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        self.side = side if side is not None else _side_Sell()
        self.price = price if price is not None else _constant(100.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunction[Side],
        'price' : IFunction[float]
    }
    def __repr__(self):
        return "volume_Limit(%(side)s, %(price)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._Limit import Limit
        volume = volume if volume is not None else _constant(1.0)
        side = self.side
        price = self.price
        return Limit(side, price, volume)
    
