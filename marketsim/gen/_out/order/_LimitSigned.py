from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Order", "LimitSigned"])
class LimitSigned(IOrderGenerator, Observable[Order]):
    """ 
    """ 
    def __init__(self, signedVolume = None, price = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        Observable[Order].__init__(self)
        self.signedVolume = signedVolume if signedVolume is not None else _constant(1.0)
        if isinstance(signedVolume, types.IEvent):
            event.subscribe(self.signedVolume, self.fire, self)
        self.price = price if price is not None else _constant(100.0)
        if isinstance(price, types.IEvent):
            event.subscribe(self.price, self.fire, self)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'signedVolume' : IFunction[float],
        'price' : IFunction[float]
    }
    def __repr__(self):
        return "LimitSigned(%(signedVolume)s, %(price)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim import Side
        from marketsim.gen._intrinsic.order.limit import Order_Impl
        signedVolume = self.signedVolume()
        if signedVolume is None: return None
        side = Side.Buy if signedVolume > 0 else Side.Sell
        volume = abs(signedVolume)
        if abs(volume) < 1: return None
        volume = int(volume)
        price = self.price()
        if price is None: return None
        
        return Order_Impl(side, price, volume)
    
