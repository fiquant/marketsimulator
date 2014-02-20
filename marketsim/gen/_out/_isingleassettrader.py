from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._itrader import ITrader
class ISingleAssetTrader(IAccount,ITrader):
    def Unit(self):
        from marketsim.gen._out.strategy.weight._unit import Unit
        return Unit(self)
    
    def Score(self):
        from marketsim.gen._out.strategy.weight._score import Score
        return Score(self)
    
    def EfficiencyTrend(self, alpha = None):
        from marketsim.gen._out.strategy.weight._efficiencytrend import EfficiencyTrend
        return EfficiencyTrend(self,alpha)
    
    def Efficiency(self):
        from marketsim.gen._out.strategy.weight._efficiency import Efficiency
        return Efficiency(self)
    
    pass
