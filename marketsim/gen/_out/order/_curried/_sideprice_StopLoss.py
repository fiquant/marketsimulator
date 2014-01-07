from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "StopLoss"])
class sideprice_StopLoss(IFunction[IOrderGenerator, IFunction[Side],IFunction[float]

]):
    """ 
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._curried._sideprice_Limit import sideprice_Limit
        self.maxloss = maxloss if maxloss is not None else const(0.1)
        self.proto = proto if proto is not None else sideprice_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IObservable[float],
        'proto' : IFunction[IOrderGenerator, IFunction[Side],IFunction[float]
        
        ]
    }
    def __repr__(self):
        return "sideprice_StopLoss(%(maxloss)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,price = None):
        from marketsim.gen._out.order._StopLoss import StopLoss
        maxloss = self.maxloss
        proto = self.proto
        return StopLoss(maxloss, proto(side,price))
    
