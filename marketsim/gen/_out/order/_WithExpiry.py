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
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
@registry.expose(["Order", "WithExpiry"])
class side_WithExpiry(IFunction[IOrderGenerator, IFunction[Side]
]):
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
        'proto' : IFunction[IOrderGenerator, IFunction[Side]
        ]
    }
    def __repr__(self):
        return "side_WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(expiry, proto(side))
    
from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
@registry.expose(["Order", "WithExpiry"])
class volume_WithExpiry(IFunction[IOrderGenerator, IFunction[float]]):
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
        'proto' : IFunction[IOrderGenerator, IFunction[float]]
    }
    def __repr__(self):
        return "volume_WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(expiry, proto(volume))
    
from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
@registry.expose(["Order", "WithExpiry"])
class price_WithExpiry(IFunction[IOrderGenerator, IFunction[float]]):
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
        'proto' : IFunction[IOrderGenerator, IFunction[float]]
    }
    def __repr__(self):
        return "price_WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, price = None):
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(expiry, proto(price))
    
from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "WithExpiry"])
class sideprice_WithExpiry(IFunction[IOrderGenerator, IFunction[Side],IFunction[float]

]):
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
        'proto' : IFunction[IOrderGenerator, IFunction[Side],IFunction[float]
        
        ]
    }
    def __repr__(self):
        return "sideprice_WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,price = None):
        expiry = self.expiry
        proto = self.proto
        return WithExpiry(expiry, proto(side,price))
    
from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
@registry.expose(["Order", "WithExpiry"])
class side_price_WithExpiry(IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side]
]):
    """ 
    """ 
    def __init__(self, expiry = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import side_price_Limit
        self.expiry = expiry if expiry is not None else const(10.0)
        self.proto = proto if proto is not None else side_price_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'expiry' : IObservable[float],
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side]
        ]
    }
    def __repr__(self):
        return "side_price_WithExpiry(%(expiry)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        expiry = self.expiry
        proto = self.proto
        return price_WithExpiry(expiry, proto(side))
    

