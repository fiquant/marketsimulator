from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._itrader import ITrader
class ISingleAssetTrader(IAccount,ITrader):
    @property
    def Unit(self):
        from marketsim.gen._out.strategy.weight._unit import Unit
        return Unit(self)
    
    @property
    def TraderEfficiency(self):
        from marketsim.gen._out.strategy.weight._traderefficiency import TraderEfficiency
        return TraderEfficiency(self)
    
    @property
    def Score(self):
        from marketsim.gen._out.strategy.weight._score import Score
        return Score(self)
    
    def TraderEfficiencyTrend(self, alpha = None):
        from marketsim.gen._out.strategy.weight._traderefficiencytrend import TraderEfficiencyTrend
        return TraderEfficiencyTrend(self,alpha)
    
    pass
