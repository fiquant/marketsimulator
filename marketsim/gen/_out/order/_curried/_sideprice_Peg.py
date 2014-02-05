from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import IFunction
from marketsim import float
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import float
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "Peg"])
class sideprice_Peg(IFunction[IOrderGenerator,IFunction[Side]
,IFunction[float]]):
    """ 
      A peg order is a particular case of the floating price order
      with the price better at one tick than the best price of the order queue.
      It implies that if several peg orders are sent to the same order queue
      they start to race until being matched against the counterparty orders.
    """ 
    def __init__(self, proto = None):
        from marketsim import IOrderGenerator
        from marketsim import Side
        from marketsim import IFunction
        from marketsim import float
        from marketsim import IFunction
        from marketsim import IFunction
        from marketsim.gen._out.order._curried._side_price_Limit import side_price_Limit as _order__curried_side_price_Limit
        from marketsim import rtti
        IFunction[IOrderGenerator,IFunction[Side]
        ,IFunction[float]].__init__(self)
        self.proto = proto if proto is not None else _order__curried_side_price_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side]]
    }
    def __repr__(self):
        return "Peg(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.order._Peg import Peg
        proto = self.proto
        return Peg(proto(side))
    
sideprice_Peg = sideprice_Peg
