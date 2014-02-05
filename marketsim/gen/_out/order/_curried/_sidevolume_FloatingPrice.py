from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import IFunction
from marketsim import float
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IObservable
from marketsim import float
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import float
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
@registry.expose(["Order", "FloatingPrice"])
class sidevolume_FloatingPrice(IFunction[IOrderGenerator,IFunction[Side]
,IFunction[float]]):
    """ 
      Floating price order is initialized by an order having a price and an observable that generates new prices.
      When the observable value changes the order is cancelled and
      a new order with new price is created and sent to the order book.
    """ 
    def __init__(self, floatingPrice = None, proto = None):
        from marketsim import IOrderGenerator
        from marketsim import Side
        from marketsim import IFunction
        from marketsim import float
        from marketsim import IFunction
        from marketsim import IFunction
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.order._curried._sidevolume_price_Limit import sidevolume_price_Limit as _order__curried_sidevolume_price_Limit
        from marketsim import rtti
        IFunction[IOrderGenerator,IFunction[Side]
        ,IFunction[float]].__init__(self)
        self.floatingPrice = floatingPrice if floatingPrice is not None else _const(10.0)
        self.proto = proto if proto is not None else _order__curried_sidevolume_price_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'floatingPrice' : IObservable[float],
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side],IFunction[float]]
    }
    def __repr__(self):
        return "FloatingPrice(%(floatingPrice)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.order._FloatingPrice import FloatingPrice
        floatingPrice = self.floatingPrice
        proto = self.proto
        return FloatingPrice(floatingPrice, proto(side,volume))
    
sidevolume_FloatingPrice = sidevolume_FloatingPrice
