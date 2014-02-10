from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "price_FloatingPrice"])
class volume_price_FloatingPrice_IObservableFloatFloatFloatIOrderGenerator(IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
    """ 
      Floating price order is initialized by an order having a price and an observable that generates new prices.
      When the observable value changes the order is cancelled and
      a new order with new price is created and sent to the order book.
    """ 
    def __init__(self, floatingPrice = None, proto = None):
        from marketsim.gen._out._const import const_Float as _const
        from marketsim.gen._out.order._curried._volume_price_limit import volume_price_Limit_Side as _order__curried_volume_price_Limit
        from marketsim import rtti
        self.floatingPrice = floatingPrice if floatingPrice is not None else _const(10.0)
        self.proto = proto if proto is not None else _order__curried_volume_price_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'floatingPrice' : IObservable[float],
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[float]]
    }
    def __repr__(self):
        return "price_FloatingPrice(%(floatingPrice)s, %(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim.gen._out.order._curried._price_floatingprice import price_FloatingPrice
        volume = volume if volume is not None else _constant(1.0)
        floatingPrice = self.floatingPrice
        proto = self.proto
        return price_FloatingPrice(floatingPrice, proto(volume))
    
def volume_price_FloatingPrice(floatingPrice = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IOrderGenerator
    if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservable[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
            return volume_price_FloatingPrice_IObservableFloatFloatFloatIOrderGenerator(floatingPrice,proto)
    raise Exception("Cannot find suitable overload")
