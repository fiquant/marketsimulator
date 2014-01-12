from marketsim import registry
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "ImmediateOrCancel"])
class sidevolume_price_ImmediateOrCancel(





IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side],IFunction[float]]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._sidevolume_price_Limit import sidevolume_price_Limit as _order__curried_sidevolume_price_Limit
        self.proto = proto if proto is not None else _order__curried_sidevolume_price_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side],IFunction[float]
        
        ]
    }
    def __repr__(self):
        return "sidevolume_price_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.order._curried._price_ImmediateOrCancel import price_ImmediateOrCancel
        proto = self.proto
        return price_ImmediateOrCancel(proto(side,volume))
    
