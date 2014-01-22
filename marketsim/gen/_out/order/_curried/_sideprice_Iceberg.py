from marketsim import registry
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "Iceberg"])
class sideprice_Iceberg(



IFunction[IOrderGenerator,IFunction[Side],IFunction[float]]):
    """ 
    """ 
    def __init__(self, lotSize = None, proto = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._curried._sideprice_Limit import sideprice_Limit as _order__curried_sideprice_Limit
        from marketsim import rtti
        self.lotSize = lotSize if lotSize is not None else _constant(10.0)
        self.proto = proto if proto is not None else _order__curried_sideprice_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'lotSize' : IFunction[float],
        'proto' : IFunction[IOrderGenerator, IFunction[Side],IFunction[float]
        
        ]
    }
    def __repr__(self):
        return "sideprice_Iceberg(%(lotSize)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,price = None):
        from marketsim.gen._out.order._Iceberg import Iceberg
        lotSize = self.lotSize
        proto = self.proto
        return Iceberg(lotSize, proto(side,price))
    
