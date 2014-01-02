from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import IObservable
from marketsim import Order
@registry.expose(["Order", "Iceberg"])
class Iceberg(IOrderGenerator, Observable[Order]):
    """ 
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out.order._Limit import Limit
        from marketsim import event
        from marketsim import types
        Observable[Order].__init__(self)
        self.lotSize = lotSize if lotSize is not None else const(10.0)
        if isinstance(lotSize, types.IEvent):
            event.subscribe(self.lotSize, self.fire, self)
        self.proto = proto if proto is not None else Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IObservable[float],
        'proto' : IObservable[Order]
        
    }
    def __repr__(self):
        return "Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.iceberg import Iceberg_Impl
        lotSize = self.lotSize()
        if lotSize is None: return None
        
        proto = self.proto()
        if proto is None: return None
        
        return Iceberg_Impl(lotSize, proto)
    


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
@registry.expose(["Order", "Iceberg"])
@sig((IFunction[Side],)
, IOrderGenerator)
class side_Iceberg(object):
    """ 
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import side_Limit
        self.lotSize = lotSize if lotSize is not None else const(10.0)
        self.proto = proto if proto is not None else side_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IObservable[float],
        'proto' : meta.function((IFunction[Side],)
        , IOrderGenerator)
    }
    def __repr__(self):
        return "side_Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        lotSize = self.lotSize
        proto = self.proto
        return Iceberg(self.lotSize, self.proto(side))
    

from marketsim import registry
from marketsim import IFunction
from marketsim.types import sig
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IFunction
from marketsim import meta
from marketsim import IOrderGenerator
@registry.expose(["Order", "Iceberg"])
@sig((IFunction[float],), IOrderGenerator)
class volume_Iceberg(object):
    """ 
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import volume_Limit
        self.lotSize = lotSize if lotSize is not None else const(10.0)
        self.proto = proto if proto is not None else volume_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IObservable[float],
        'proto' : meta.function((IFunction[float],), IOrderGenerator)
    }
    def __repr__(self):
        return "volume_Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        lotSize = self.lotSize
        proto = self.proto
        return Iceberg(self.lotSize, self.proto(volume))
    

from marketsim import registry
from marketsim import IFunction
from marketsim.types import sig
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IFunction
from marketsim import meta
from marketsim import IOrderGenerator
@registry.expose(["Order", "Iceberg"])
@sig((IFunction[float],), IOrderGenerator)
class price_Iceberg(object):
    """ 
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import price_Limit
        self.lotSize = lotSize if lotSize is not None else const(10.0)
        self.proto = proto if proto is not None else price_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IObservable[float],
        'proto' : meta.function((IFunction[float],), IOrderGenerator)
    }
    def __repr__(self):
        return "price_Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, price = None):
        lotSize = self.lotSize
        proto = self.proto
        return Iceberg(self.lotSize, self.proto(price))
    

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
@registry.expose(["Order", "Iceberg"])
@sig((IFunction[Side],IFunction[float],)

, IOrderGenerator)
class sideprice_Iceberg(object):
    """ 
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import sideprice_Limit
        self.lotSize = lotSize if lotSize is not None else const(10.0)
        self.proto = proto if proto is not None else sideprice_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IObservable[float],
        'proto' : meta.function((IFunction[Side],IFunction[float],)
        
        , IOrderGenerator)
    }
    def __repr__(self):
        return "sideprice_Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,price = None):
        lotSize = self.lotSize
        proto = self.proto
        return Iceberg(self.lotSize, self.proto(side,price))
    

