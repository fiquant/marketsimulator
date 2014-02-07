from marketsim import registry
from marketsim import IFunction
from marketsim import float
from marketsim import IAccount
@registry.expose(["Strategy", "trader_EfficiencyTrend"])
class trader_EfficiencyTrend_Optional__Float_(IFunction[IFunction[float], IAccount]):
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
        from marketsim.gen._out.strategy.weight._EfficiencyTrend import EfficiencyTrend
        trader = trader if trader is not None else _trader_SingleProxy()
        alpha = self.alpha
        return EfficiencyTrend(trader,alpha)
    
def trader_EfficiencyTrend(alpha = None): 
    from marketsim import float
    from marketsim import rtti
    if alpha is None or rtti.can_be_casted(alpha, float):
        return trader_EfficiencyTrend_Optional__Float_(alpha)
    raise Exception("Cannot find suitable overload")
