from marketsim import registry
from marketsim import IOrderGenerator
from marketsim.gen._intrinsic.order.meta.floating_price import Factory_Impl
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
@registry.expose(["Order", "FloatingPrice"])
class FloatingPrice(IOrderGenerator, Factory_Impl):
    """ 
    """ 
    def __init__(self, floatingPrice = None, proto = None):
        from marketsim.gen._intrinsic.order.meta.floating_price import Factory_Impl
        from marketsim.gen._out._constant import constant
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out.order._curried._price_Limit import price_Limit
        from marketsim import event
        from marketsim import types
        Factory_Impl.__init__(self)
        self.floatingPrice = floatingPrice if floatingPrice is not None else constant(10.0)
        if isinstance(floatingPrice, types.IEvent):
            event.subscribe(self.floatingPrice, self.fire, self)
        self.proto = proto if proto is not None else price_Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'floatingPrice' : IFunction[float],
        'proto' : IFunction[IOrderGenerator,IFunction[float]]
        
        
    }
    def __repr__(self):
        return "FloatingPrice(%(floatingPrice)s, %(proto)s)" % self.__dict__
    
    

