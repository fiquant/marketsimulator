from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import float
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
@registry.expose(["Order", "Limit"])
class price_Limit(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self, side = None, volume = None):
        from marketsim import IOrderGenerator
        from marketsim import IFunction
        from marketsim import float
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        IFunction[IOrderGenerator, IFunction[float]].__init__(self)
        self.side = side if side is not None else _side_Sell()
        self.volume = volume if volume is not None else _constant(1.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunction[Side],
        'volume' : IFunction[float]
    }
    def __repr__(self):
        return "Limit(%(side)s, %(volume)s)" % self.__dict__
    
    def __call__(self, price = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._Limit import Limit
        price = price if price is not None else _constant(100.0)
        side = self.side
        volume = self.volume
        return Limit(side, price, volume)
    
price_Limit = price_Limit
