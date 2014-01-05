from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Order", "Peg"])
class pricevolume_Peg(IFunction[IOrderGenerator, IFunction[float],IFunction[float]
]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._volumeprice_Limit import volumeprice_Limit
        self.proto = proto if proto is not None else volumeprice_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, IFunction[float],IFunction[float]
        ]
    }
    def __repr__(self):
        return "pricevolume_Peg(%(proto)s)" % self.__dict__
    
    def __call__(self, price = None,volume = None):
        from marketsim.gen._out.order._Peg import Peg
        proto = self.proto
        return Peg(proto(price,volume))
    
