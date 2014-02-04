from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import float
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import float
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import float
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
@registry.expose(["Order", "StopLoss"])
class sidevolume_price_StopLoss(IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]
,IFunction[float]]):
    """ 
      StopLoss order is initialised by an underlying order and a maximal acceptable loss factor.
      It keeps track of position and balance change induced by trades of the underlying order and
      if losses from keeping the position exceed certain limit (given by maximum loss factor),
      the meta order clears its position.
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._curried._sidevolume_price_Limit import sidevolume_price_Limit as _order__curried_sidevolume_price_Limit
        from marketsim import rtti
        self.maxloss = maxloss if maxloss is not None else _constant(0.1)
        self.proto = proto if proto is not None else _order__curried_sidevolume_price_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IFunction[float],
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side],IFunction[float]]
    }
    def __repr__(self):
        return "StopLoss(%(maxloss)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.order._curried._price_StopLoss import price_StopLoss
        maxloss = self.maxloss
        proto = self.proto
        return price_StopLoss(maxloss, proto(side,volume))
    
sidevolume_price_StopLoss = sidevolume_price_StopLoss
