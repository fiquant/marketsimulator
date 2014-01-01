from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import Order
@registry.expose(["Order", "ImmediateOrCancel"])
class ImmediateOrCancel(IOrderGenerator, Observable[Order]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out.order._Limit import Limit
        from marketsim import event
        from marketsim import types
        Observable[Order].__init__(self)
        self.proto = proto if proto is not None else Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IObservable[Order]
        
    }
    def __repr__(self):
        return "ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.ioc import Order_Impl
        proto = self.proto()
        if proto is None: return None
        
        return Order_Impl(proto)
    


from marketsim import registry
from marketsim import Side
from marketsim.types import sig
from marketsim import IFunction
from marketsim import Side
from marketsim import meta
from marketsim import IOrderGenerator
@registry.expose(["Order", "ImmediateOrCancel"])
@sig((IFunction[Side],), IOrderGenerator)
class side_ImmediateOrCancel(object):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._Limit import side_Limit
        self.proto = proto if proto is not None else side_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : meta.function((IFunction[Side],), IOrderGenerator)
    }
    def __repr__(self):
        return "side_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        proto = self.proto
        return ImmediateOrCancel(self.proto(side))
    

from marketsim import registry
from marketsim.types import sig
from marketsim import IFunction
from marketsim import meta
from marketsim import IOrderGenerator
@registry.expose(["Order", "ImmediateOrCancel"])
@sig((IFunction[float],), IOrderGenerator)
class volume_ImmediateOrCancel(object):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._Limit import volume_Limit
        self.proto = proto if proto is not None else volume_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : meta.function((IFunction[float],), IOrderGenerator)
    }
    def __repr__(self):
        return "volume_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        proto = self.proto
        return ImmediateOrCancel(self.proto(volume))
    

from marketsim import registry
from marketsim.types import sig
from marketsim import IFunction
from marketsim import meta
from marketsim import IOrderGenerator
@registry.expose(["Order", "ImmediateOrCancel"])
@sig((IFunction[float],), IOrderGenerator)
class price_ImmediateOrCancel(object):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._Limit import price_Limit
        self.proto = proto if proto is not None else price_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : meta.function((IFunction[float],), IOrderGenerator)
    }
    def __repr__(self):
        return "price_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, price = None):
        proto = self.proto
        return ImmediateOrCancel(self.proto(price))
    

