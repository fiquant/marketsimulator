from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
@registry.expose(["Order", "Market"])
class Market(IOrderGenerator, Observable[Order]):
    """ 
      Market order intructs buy or sell given volume immediately
    """ 
    def __init__(self, side = None, volume = None):
        from marketsim import Order
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        Observable[Order].__init__(self)
        self.side = side if side is not None else _side_Sell()
        if isinstance(side, types.IEvent):
            event.subscribe(self.side, self.fire, self)
        self.volume = volume if volume is not None else _constant(1.0)
        if isinstance(volume, types.IEvent):
            event.subscribe(self.volume, self.fire, self)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunction[Side],
        'volume' : IFunction[float]
    }
    def __repr__(self):
        return "Market(%(side)s, %(volume)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.market import Order_Impl
        side = self.side()
        if side is None: return None
        
        volume = self.volume()
        if volume is None: return None
        if abs(volume) < 1: return None
        volume = int(volume)
        return Order_Impl(side, volume)
    
Market = Market
