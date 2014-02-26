from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionfloatiaccount import IFunctionIFunctionfloatIAccount
@registry.expose(["Strategy", "trader_TraderEfficiencyTrend"])
class trader_TraderEfficiencyTrend_Float(IFunctionIFunctionfloatIAccount):
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
        return "trader_TraderEfficiencyTrend(%(alpha)s)" % self.__dict__
    
    def __call__(self, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim.gen._out.strategy.weight._traderefficiencytrend import TraderEfficiencyTrend_IAccountFloat as _strategy_weight_TraderEfficiencyTrend_IAccountFloat
        trader = trader if trader is not None else _trader_SingleProxy_()
        alpha = self.alpha
        return _strategy_weight_TraderEfficiencyTrend_IAccountFloat(trader,alpha)
    
def trader_TraderEfficiencyTrend(alpha = None): 
    from marketsim import rtti
    if alpha is None or rtti.can_be_casted(alpha, float):
        return trader_TraderEfficiencyTrend_Float(alpha)
    raise Exception('Cannot find suitable overload for trader_TraderEfficiencyTrend('+str(alpha) +':'+ str(type(alpha))+')')
