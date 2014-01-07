from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
@registry.expose(["Order", "ImmediateOrCancel"])
class side_ImmediateOrCancel(IFunction[IOrderGenerator, IFunction[Side]
]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._side_Limit import side_Limit
        self.proto = proto if proto is not None else side_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, IFunction[Side]
        ]
    }
    def __repr__(self):
        return "side_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.order._ImmediateOrCancel import ImmediateOrCancel
        proto = self.proto
        return ImmediateOrCancel(proto(side))
    
