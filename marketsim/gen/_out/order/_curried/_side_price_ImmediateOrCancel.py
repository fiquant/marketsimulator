from marketsim import registry
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
@registry.expose(["Order", "ImmediateOrCancel"])
class side_price_ImmediateOrCancel(




IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]]):""" 
      Immediate-Or-Cancel order sends an underlying order to the market and
      immediately sends a cancel request for it.
      It allows to combine market and limit order behaviour:
      the order is either executed immediately
      at price equal or better than given one
      either it is cancelled (and consequently never stored in the order queue).
    """ 
    def __init__(self, proto = None):from marketsim.gen._out.order._curried._side_price_Limit import side_price_Limit as _order__curried_side_price_Limit
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_side_price_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):return repr(self)
    
    _properties = {'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side]
        ]
    }
    def __repr__(self):return "side_price_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None):from marketsim.gen._out.order._curried._price_ImmediateOrCancel import price_ImmediateOrCancel
        proto = self.proto
        return price_ImmediateOrCancel(proto(side))
    
