from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Order", "MarketSigned"])
class MarketSigned(IOrderGenerator, Observable[Order]):
    """ 
      Market order intructs buy or sell given volume immediately
    """ 
    def __init__(self, signedVolume = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        Observable[Order].__init__(self)
        self.signedVolume = signedVolume if signedVolume is not None else _constant(1.0)
        if isinstance(signedVolume, types.IEvent):
            event.subscribe(self.signedVolume, self.fire, self)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'signedVolume' : IFunction[float]
    }
    def __repr__(self):
        return "MarketSigned(%(signedVolume)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim import Side
        from marketsim.gen._intrinsic.order.market import Order_Impl
        signedVolume = self.signedVolume()
        if signedVolume is None: return None
        side = Side.Buy if signedVolume > 0 else Side.Sell
        volume = abs(signedVolume)
        if abs(volume) < 1: return None
        volume = int(volume)
        return Order_Impl(side, volume)
    
