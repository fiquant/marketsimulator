from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
class ILadderStrategy(ISingleAssetStrategy):
    def LadderBalancer(self, maximalSize = None):
        from marketsim.gen._out.strategy.price._ladderbalancer import LadderBalancer
        return LadderBalancer(self,maximalSize)
    
    pass
