from marketsim import registry
from marketsim import IOrderGenerator
from marketsim.gen._intrinsic.order.meta.peg import Factory_Impl
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
@registry.expose(["Order", "Peg"])
class Peg(IOrderGenerator, Factory_Impl):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._intrinsic.order.meta.peg import Factory_Impl
        from marketsim.gen._out.order._curried._price_Limit import price_Limit as _order__curried_price_Limit
        from marketsim import event
        from marketsim import types
        Factory_Impl.__init__(self)
        self.proto = proto if proto is not None else _order__curried_price_Limit()
        if isinstance(proto, types.IEvent):
            event.subscribe(self.proto, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator,IFunction[float]]
        
        
    }
    def __repr__(self):
        return "Peg(%(proto)s)" % self.__dict__
    
    

