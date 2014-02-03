from marketsim import registry
from marketsim import IFunction
from marketsim import IAccount
from marketsim import IFunction
@registry.expose(["Strategy", "trader_EfficiencyTrend"])
class trader_EfficiencyTrend(IFunction[IFunction[float], IAccount]):
    """ 
    """ 
    def __init__(self, alpha = None):
        from marketsim import rtti
        self.alpha = alpha if alpha is not None else 0.15
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float
    }
    def __repr__(self):
        return "trader_EfficiencyTrend(%(alpha)s)" % self.__dict__
    
    def __call__(self, trader = None):
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim.gen._out.strategy.weight._EfficiencyTrend import EfficiencyTrend
        trader = trader if trader is not None else _trader_SingleProxy()
        alpha = self.alpha
        return EfficiencyTrend(trader,alpha)
    
