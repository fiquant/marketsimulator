from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import IObservable
from marketsim import Order
@registry.expose(["Order", "WithExpiry"])
class WithExpiry(IOrderGenerator, Observable[Order]):
    """ 
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out.order._Limit import Limit
        from marketsim import event
        from marketsim import types
        Observable[Order].__init__(self)
        self.expiry = expiry if expiry is not None else const(10.0)
        if isinstance(expiry, types.IEvent):
            event.subscribe(self.expiry, self.fire, self)
        self.proto = proto if proto is not None else Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IObservable[float],
        'proto' : IObservable[Order]
        
    }
    def __repr__(self):
        return "WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.with_expiry import WithExpiry_Impl
        expiry = self.expiry()
        if expiry is None: return None
        
        proto = self.proto()
        if proto is None: return None
        
        return WithExpiry_Impl(expiry, proto)
    


from marketsim import registry
from marketsim import IFunction
from marketsim import Side
from marketsim.types import sig
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IFunction
from marketsim import Side
from marketsim import meta
from marketsim import IOrderGenerator
@registry.expose(["Order", "WithExpiry"])
@sig((IFunction[Side],)
, IOrderGenerator)
class side_WithExpiry(object):
    """ 
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import side_Limit
        self.expiry = expiry if expiry is not None else const(10.0)
        self.proto = proto if proto is not None else side_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IObservable[float],
        'proto' : meta.function((IFunction[Side],)
        , IOrderGenerator)
    }
    def __repr__(self):
        return "side_WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(self.expiry, self.proto(side))
    

from marketsim import registry
from marketsim import IFunction
from marketsim.types import sig
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IFunction
from marketsim import meta
from marketsim import IOrderGenerator
@registry.expose(["Order", "WithExpiry"])
@sig((IFunction[float],), IOrderGenerator)
class volume_WithExpiry(object):
    """ 
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import volume_Limit
        self.expiry = expiry if expiry is not None else const(10.0)
        self.proto = proto if proto is not None else volume_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IObservable[float],
        'proto' : meta.function((IFunction[float],), IOrderGenerator)
    }
    def __repr__(self):
        return "volume_WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(self.expiry, self.proto(volume))
    

from marketsim import registry
from marketsim import IFunction
from marketsim.types import sig
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IFunction
from marketsim import meta
from marketsim import IOrderGenerator
@registry.expose(["Order", "WithExpiry"])
@sig((IFunction[float],), IOrderGenerator)
class price_WithExpiry(object):
    """ 
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import price_Limit
        self.expiry = expiry if expiry is not None else const(10.0)
        self.proto = proto if proto is not None else price_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IObservable[float],
        'proto' : meta.function((IFunction[float],), IOrderGenerator)
    }
    def __repr__(self):
        return "price_WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, price = None):
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(self.expiry, self.proto(price))
    

from marketsim import registry
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim.types import sig
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import meta
from marketsim import IOrderGenerator
@registry.expose(["Order", "WithExpiry"])
@sig((IFunction[Side],IFunction[float],)

, IOrderGenerator)
class sideprice_WithExpiry(object):
    """ 
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import sideprice_Limit
        self.expiry = expiry if expiry is not None else const(10.0)
        self.proto = proto if proto is not None else sideprice_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IObservable[float],
        'proto' : meta.function((IFunction[Side],IFunction[float],)
        
        , IOrderGenerator)
    }
    def __repr__(self):
        return "sideprice_WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,price = None):
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(self.expiry, self.proto(side,price))
    

