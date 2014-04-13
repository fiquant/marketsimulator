from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class ISuspendableStrategy(ISingleAssetStrategy):
    def Clearable(self, predicate = None):
        from marketsim.gen._out.strategy.price._clearable import Clearable
        return Clearable(self,predicate)
    
    def StopLoss(self, lossFactor = None):
        from marketsim.gen._out.strategy.price._stoploss import StopLoss
        return StopLoss(self,lossFactor)
    
    pass
