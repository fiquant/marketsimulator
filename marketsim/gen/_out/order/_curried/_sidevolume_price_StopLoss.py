from marketsim import registry
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
@registry.expose(["Order", "StopLoss"])
class sidevolume_price_StopLoss(





IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side],IFunction[float]]):
    """ 
    """ 
    def __init__(self, maxloss = None, proto = None):
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.order._curried._sidevolume_price_Limit import sidevolume_price_Limit as _order__curried_sidevolume_price_Limit
        self.maxloss = maxloss if maxloss is not None else _const(0.1)
        self.proto = proto if proto is not None else _order__curried_sidevolume_price_Limit()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'maxloss' : IObservable[float],
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side],IFunction[float]
        
        ]
    }
    def __repr__(self):
        return "sidevolume_price_StopLoss(%(maxloss)s, %(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.order._curried._price_StopLoss import price_StopLoss
        maxloss = self.maxloss
        proto = self.proto
        return price_StopLoss(maxloss, proto(side,volume))
    
