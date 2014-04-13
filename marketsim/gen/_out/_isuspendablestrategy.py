from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class ISuspendableStrategy(ISingleAssetStrategy):
    def StopLoss(self, lossFactor = None):
        from marketsim.gen._out.strategy.price._stoploss import StopLoss
        return StopLoss(self,lossFactor)
    
    pass
