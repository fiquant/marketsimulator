from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "price_Limit"])
class sidevolume_price_Limit_(IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side],IFunction[float]]):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "price_Limit" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._curried._price_limit import price_Limit
        side = side if side is not None else _side_Sell_()
        volume = volume if volume is not None else _constant_Float(1.0)
        
        return price_Limit(side, volume)
    
def sidevolume_price_Limit(): 
    from marketsim import rtti
    return sidevolume_price_Limit_()
    raise Exception('Cannot find suitable overload for sidevolume_price_Limit('++')')
