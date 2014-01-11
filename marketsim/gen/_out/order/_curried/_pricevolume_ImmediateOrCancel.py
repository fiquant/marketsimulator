from marketsim import registry
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Order", "ImmediateOrCancel"])
class pricevolume_ImmediateOrCancel(


IFunction[IOrderGenerator,IFunction[float],IFunction[float]]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._pricevolume_Limit import pricevolume_Limit as _order__curried_pricevolume_Limit
        self.proto = proto if proto is not None else _order__curried_pricevolume_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, IFunction[float],IFunction[float]
        ]
    }
    def __repr__(self):
        return "pricevolume_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, price = None,volume = None):
        from marketsim.gen._out.order._ImmediateOrCancel import ImmediateOrCancel
        proto = self.proto
        return ImmediateOrCancel(proto(price,volume))
    
