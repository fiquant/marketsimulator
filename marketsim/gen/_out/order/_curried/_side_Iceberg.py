from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
@registry.expose(["Order", "Iceberg"])
class side_Iceberg(IFunction[IOrderGenerator, types.IFunction[Side]
]):
    """ 
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._curried._side_Limit import side_Limit
        self.lotSize = lotSize if lotSize is not None else const(10.0)
        self.proto = proto if proto is not None else side_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IObservable[float],
        'proto' : IFunction[IOrderGenerator, types.IFunction[Side]
        ]
    }
    def __repr__(self):
        return "side_Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.order._Iceberg import Iceberg
        lotSize = self.lotSize
        proto = self.proto
        return Iceberg(lotSize, proto(side))
    
