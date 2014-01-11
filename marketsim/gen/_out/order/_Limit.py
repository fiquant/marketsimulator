from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Order", "Limit"])
class Limit(IOrderGenerator, Observable[Order]):
    """ 
    """ 
    def __init__(self, side = None, price = None, volume = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import types
        Observable[Order].__init__(self)
        self.side = side if side is not None else _side_Sell()
        if isinstance(side, types.IEvent):
            event.subscribe(self.side, self.fire, self)
        self.price = price if price is not None else _constant(100.0)
        if isinstance(price, types.IEvent):
            event.subscribe(self.price, self.fire, self)
        self.volume = volume if volume is not None else _constant(1.0)
        if isinstance(volume, types.IEvent):
            event.subscribe(self.volume, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunction[Side]
        ,
        'price' : IFunction[float],
        'volume' : IFunction[float]
    }
    def __repr__(self):
        return "Limit(%(side)s, %(price)s, %(volume)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.limit import Order_Impl
        side = self.side()
        if side is None: return None
        
        price = self.price()
        if price is None: return None
        
        volume = self.volume()
        if volume is None: return None
        if abs(volume) < 1: return None
        volume = int(volume)
        return Order_Impl(side, price, volume)
    
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
        Observable[Order].__init__(self)
        self.signedVolume = signedVolume if signedVolume is not None else _constant(1.0)
        if isinstance(signedVolume, types.IEvent):
            event.subscribe(self.signedVolume, self.fire, self)
        self.price = price if price is not None else _constant(100.0)
        if isinstance(price, types.IEvent):
            event.subscribe(self.price, self.fire, self)
    
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
    

