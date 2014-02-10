from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "FloatingPrice"])
class sideprice_FloatingPrice_IObservableFloatSideFloatIOrderGenerator(IFunction[IOrderGenerator,IFunction[Side]
,IFunction[float]]):
    """ 
      Floating price order is initialized by an order having a price and an observable that generates new prices.
      When the observable value changes the order is cancelled and
      a new order with new price is created and sent to the order book.
    """ 
    def __init__(self, floatingPrice = None, proto = None):
        from marketsim.gen._out._const import const_Float as _const
        from marketsim.gen._out.order._curried._side_price_limit import side_price_Limit_IFunctionFloat as _order__curried_side_price_Limit
        from marketsim import rtti
        self.floatingPrice = floatingPrice if floatingPrice is not None else _const(10.0)
        self.proto = proto if proto is not None else _order__curried_side_price_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'floatingPrice' : IObservable[float],
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side]]
    }
    def __repr__(self):
        return "FloatingPrice(%(floatingPrice)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell
        from marketsim.gen._out.order._floatingprice import FloatingPrice
        side = side if side is not None else _side_Sell()
        floatingPrice = self.floatingPrice
        proto = self.proto
        return FloatingPrice(floatingPrice, proto(side))
    
def sideprice_FloatingPrice(floatingPrice = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IOrderGenerator
    from marketsim import Side
    if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservable[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]]):
            return sideprice_FloatingPrice_IObservableFloatSideFloatIOrderGenerator(floatingPrice,proto)
    raise Exception("Cannot find suitable overload")
