from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import types
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "Market"])
class Market(IOrderGenerator, Observable[Order]):
    """ 
    """ 
    def __init__(self, side = None, volume = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out.side._Sell import Sell
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out._constant import constant
        from marketsim import event
        from marketsim import types
        Observable[Order].__init__(self)
        self.side = side if side is not None else Sell()
        if isinstance(side, types.IEvent):
            event.subscribe(self.side, self.fire, self)
        self.volume = volume if volume is not None else constant(1.0)
        if isinstance(volume, types.IEvent):
            event.subscribe(self.volume, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : types.IFunction[Side]
        ,
        'volume' : IFunction[float]
    }
    def __repr__(self):
        return "Market(%(side)s, %(volume)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.market import Market_Impl
        side = self.side()
        if side is None: return None
        
        volume = self.volume()
        if volume is None: return None
        if abs(volume) < 1: return None
        volume = int(volume)
        return Market_Impl(side, volume)
    
from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IFunction
@registry.expose(["Order", "MarketSigned"])
class MarketSigned(IOrderGenerator, Observable[Order]):
    """ 
    """ 
    def __init__(self, signedVolume = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant
        from marketsim import event
        from marketsim import types
        Observable[Order].__init__(self)
        self.signedVolume = signedVolume if signedVolume is not None else constant(1.0)
        if isinstance(signedVolume, types.IEvent):
            event.subscribe(self.signedVolume, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'signedVolume' : IFunction[float]
    }
    def __repr__(self):
        return "Market(%(side)s, %(volume)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.market import Market_Impl
        signedVolume = self.signedVolume()
        if signedVolume is None: return None
        side = Side.Buy if signedVolume > 0 else Side.Sell
        volume = abs(signedVolume)
        if abs(volume) < 1: return None
        volume = int(volume)
        return Market_Impl(side, volume)
    
