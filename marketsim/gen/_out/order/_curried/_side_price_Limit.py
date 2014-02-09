from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "price_Limit"])
class price_Limit_SideIFunctionFloat(IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side]]):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
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
        return "price_Limit(%(volume)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out.order._curried._price_Limit import price_Limit
        side = side if side is not None else _side_Sell()
        volume = self.volume
        return price_Limit(side, volume)
    
def side_price_Limit(volume = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if volume is None or rtti.can_be_casted(volume, IFunction[float]):
        return price_Limit_SideIFunctionFloat(volume)
    raise Exception("Cannot find suitable overload")
