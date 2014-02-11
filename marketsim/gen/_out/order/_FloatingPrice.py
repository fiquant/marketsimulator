from marketsim import IFunction
from marketsim.gen._intrinsic.order.meta.floating_price import Factory_Impl
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "FloatingPrice"])
class FloatingPrice_IObservableFloatFloatIOrderGenerator(Factory_Impl,IOrderGenerator):
    """ 
      Floating price order is initialized by an order having a price and an observable that generates new prices.
      When the observable value changes the order is cancelled and
      a new order with new price is created and sent to the order book.
    """ 
    def __init__(self, floatingPrice = None, proto = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const_Float as _const
        from marketsim import rtti
        from marketsim.gen._out.order._curried._price_limit import price_Limit_SideIFunctionFloat as _order__curried_price_Limit
        from marketsim import event
        from marketsim import Order
        Observable[Order].__init__(self)
        self.floatingPrice = floatingPrice if floatingPrice is not None else _const(10.0)
        if isinstance(floatingPrice, types.IEvent):
            event.subscribe(self.floatingPrice, self.fire, self)
        self.proto = proto if proto is not None else _order__curried_price_Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'floatingPrice' : IObservable[float],
        'proto' : IFunction[IOrderGenerator,IFunction[float]]
    }
    def __repr__(self):
        return "FloatingPrice(%(floatingPrice)s, %(proto)s)" % self.__dict__
    
    
def FloatingPrice(floatingPrice = None,proto = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IOrderGenerator
    if floatingPrice is None or rtti.can_be_casted(floatingPrice, IObservable[float]):
        if proto is None or rtti.can_be_casted(proto, IFunction[IOrderGenerator,IFunction[float]]):
            return FloatingPrice_IObservableFloatFloatIOrderGenerator(floatingPrice,proto)
    raise Exception('Cannot find suitable overload for FloatingPrice('+str(floatingPrice)+','+str(proto)+')')
