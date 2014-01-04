from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import types
from marketsim import Side
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import types
from marketsim import Side
@registry.expose(["Order", "StopLoss"])
class side_price_StopLoss(IFunction[IFunction[IOrderGenerator, IFunction[float]], types.IFunction[Side]
]):
    """ 
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import side_price_Limit
        self.maxloss = maxloss if maxloss is not None else const(0.1)
        self.proto = proto if proto is not None else side_price_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IObservable[float],
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], types.IFunction[Side]
        ]
    }
    def __repr__(self):
        return "side_price_StopLoss(%(maxloss)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        maxloss = self.maxloss
        proto = self.proto
        return price_StopLoss(maxloss, proto(side))
    
from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
@registry.expose(["Order", "StopLoss"])
class price_StopLoss(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import price_Limit
        self.maxloss = maxloss if maxloss is not None else const(0.1)
        self.proto = proto if proto is not None else price_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IObservable[float],
        'proto' : IFunction[IOrderGenerator, IFunction[float]]
    }
    def __repr__(self):
        return "price_StopLoss(%(maxloss)s, %(proto)s)" % self.__dict__
    
    def __call__(self, price = None):
        maxloss = self.maxloss
        proto = self.proto
        return StopLoss(maxloss, proto(price))
    
from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "StopLoss"])
class sideprice_StopLoss(IFunction[IOrderGenerator, types.IFunction[Side],IFunction[float]

]):
    """ 
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import sideprice_Limit
        self.maxloss = maxloss if maxloss is not None else const(0.1)
        self.proto = proto if proto is not None else sideprice_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IObservable[float],
        'proto' : IFunction[IOrderGenerator, types.IFunction[Side],IFunction[float]
        
        ]
    }
    def __repr__(self):
        return "sideprice_StopLoss(%(maxloss)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,price = None):
        maxloss = self.maxloss
        proto = self.proto
        return StopLoss(maxloss, proto(side,price))
    
from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
@registry.expose(["Order", "StopLoss"])
class side_StopLoss(IFunction[IOrderGenerator, types.IFunction[Side]
]):
    """ 
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import side_Limit
        self.maxloss = maxloss if maxloss is not None else const(0.1)
        self.proto = proto if proto is not None else side_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IObservable[float],
        'proto' : IFunction[IOrderGenerator, types.IFunction[Side]
        ]
    }
    def __repr__(self):
        return "side_StopLoss(%(maxloss)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        maxloss = self.maxloss
        proto = self.proto
        return StopLoss(maxloss, proto(side))
    
from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
@registry.expose(["Order", "StopLoss"])
class volume_StopLoss(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._Limit import volume_Limit
        self.maxloss = maxloss if maxloss is not None else const(0.1)
        self.proto = proto if proto is not None else volume_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IObservable[float],
        'proto' : IFunction[IOrderGenerator, IFunction[float]]
    }
    def __repr__(self):
        return "volume_StopLoss(%(maxloss)s, %(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        maxloss = self.maxloss
        proto = self.proto
        return StopLoss(maxloss, proto(volume))
    
from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import IObservable
from marketsim import Order
@registry.expose(["Order", "StopLoss"])
class StopLoss(IOrderGenerator, Observable[Order]):
    """ 
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out.order._Limit import Limit
        from marketsim import event
        from marketsim import types
        Observable[Order].__init__(self)
        self.maxloss = maxloss if maxloss is not None else const(0.1)
        if isinstance(maxloss, types.IEvent):
            event.subscribe(self.maxloss, self.fire, self)
        self.proto = proto if proto is not None else Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IObservable[float],
        'proto' : IObservable[Order]
        
    }
    def __repr__(self):
        return "StopLoss(%(maxloss)s, %(proto)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.stoploss import Order_Impl
        maxloss = self.maxloss()
        if maxloss is None: return None
        
        proto = self.proto()
        if proto is None: return None
        
        return Order_Impl(maxloss, proto)
    

