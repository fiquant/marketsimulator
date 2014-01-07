from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import types
from marketsim import Side
@registry.expose(["Order", "StopLoss"])
class side_StopLoss(IFunction[IOrderGenerator, IFunction[Side]
]):
    """ 
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim.gen._out._const import const
        from marketsim.gen._out.order._curried._side_Limit import side_Limit
        self.maxloss = maxloss if maxloss is not None else const(0.1)
        self.proto = proto if proto is not None else side_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IObservable[float],
        'proto' : IFunction[IOrderGenerator, IFunction[Side]
        ]
    }
    def __repr__(self):
        return "side_StopLoss(%(maxloss)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None):
        from marketsim.gen._out.order._StopLoss import StopLoss
        maxloss = self.maxloss
        proto = self.proto
        return StopLoss(maxloss, proto(side))
    
