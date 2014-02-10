from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "Limit"])
class volume_Limit_SideIFunctionFloat(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self, side = None, price = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell
        from marketsim.gen._out._constant import constant_Float as _constant
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
        return "Limit(%(side)s, %(price)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim.gen._out.order._limit import Limit
        volume = volume if volume is not None else _constant(1.0)
        side = self.side
        price = self.price
        return Limit(side, price, volume)
    
def volume_Limit(side = None,price = None): 
    from marketsim import Side
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunction[Side]):
        if price is None or rtti.can_be_casted(price, IFunction[float]):
            return volume_Limit_SideIFunctionFloat(side,price)
    raise Exception("Cannot find suitable overload")
