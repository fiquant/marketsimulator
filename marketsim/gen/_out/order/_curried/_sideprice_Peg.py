from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "Peg"])
class sideprice_Peg(IFunction[IOrderGenerator, IFunction[Side],IFunction[float]

]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._sideprice_Limit import sideprice_Limit
        self.proto = proto if proto is not None else sideprice_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, IFunction[Side],IFunction[float]
        
        ]
    }
    def __repr__(self):
        return "sideprice_Peg(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None,price = None):
        from marketsim.gen._out.order._Peg import Peg
        proto = self.proto
        return Peg(proto(side,price))
    
