from marketsim import registry
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Order", "FloatingPrice"])
class volume_price_FloatingPrice(



IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
    """ 
    """ 
    def __init__(self, floatingPrice = None, proto = None):
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.order._curried._volume_price_Limit import volume_price_Limit as _order__curried_volume_price_Limit
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
        return "volume_price_FloatingPrice(%(floatingPrice)s, %(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out.order._curried._price_FloatingPrice import price_FloatingPrice
        floatingPrice = self.floatingPrice
        proto = self.proto
        return price_FloatingPrice(floatingPrice, proto(volume))
    
