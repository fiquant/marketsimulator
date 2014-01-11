from marketsim import registry
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
@registry.expose(["Order", "Peg"])
class price_Peg(

IFunction[IOrderGenerator,IFunction[float]]):
    """ 
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._price_Limit import price_Limit as _order__curried_price_Limit
        self.proto = proto if proto is not None else _order__curried_price_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IOrderGenerator, IFunction[float]]
    }
    def __repr__(self):
        return "price_Peg(%(proto)s)" % self.__dict__
    
    def __call__(self, price = None):
        from marketsim.gen._out.order._Peg import Peg
        proto = self.proto
        return Peg(proto(price))
    
