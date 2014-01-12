from marketsim import registry
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "Iceberg"])
class sidevolume_Iceberg(



IFunction[IOrderGenerator,IFunction[Side],IFunction[float]]):
    """ 
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.order._curried._sidevolume_Limit import sidevolume_Limit as _order__curried_sidevolume_Limit
        self.lotSize = lotSize if lotSize is not None else _const(10.0)
        self.proto = proto if proto is not None else _order__curried_sidevolume_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IObservable[float],
        'proto' : IFunction[IOrderGenerator, IFunction[Side],IFunction[float]
        
        ]
    }
    def __repr__(self):
        return "sidevolume_Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.order._Iceberg import Iceberg
        lotSize = self.lotSize
        proto = self.proto
        return Iceberg(lotSize, proto(side,volume))
    
