from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "Limit"])
class sidevolume_Limit_IFunctionFloat(IFunction[IOrderGenerator, IFunction[Side],IFunction[float]]):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self, price = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.price = price if price is not None else _constant_Float(100.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'price' : IFunction[float]
    }
    def __repr__(self):
        return "Limit(%(price)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.order._limit import Limit
        side = side if side is not None else _side_Sell_()
        volume = volume if volume is not None else _constant_Float(1.0)
        price = self.price
        return Limit(side, price, volume)
    
def sidevolume_Limit(price = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if price is None or rtti.can_be_casted(price, IFunction[float]):
        return sidevolume_Limit_IFunctionFloat(price)
    raise Exception('Cannot find suitable overload for sidevolume_Limit('+str(price)+')')
