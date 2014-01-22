from marketsim import registry
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "ImmediateOrCancel"])
class sidevolume_ImmediateOrCancel(



IFunction[IOrderGenerator,IFunction[Side],IFunction[float]]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._sidevolume_Limit import sidevolume_Limit as _order__curried_sidevolume_Limit
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_sidevolume_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, IFunction[Side],IFunction[float]
        
        ]
    }
    def __repr__(self):
        return "sidevolume_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.order._ImmediateOrCancel import ImmediateOrCancel
        proto = self.proto
        return ImmediateOrCancel(proto(side,volume))
    
