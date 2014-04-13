from marketsim.gen._out.strategy.price._isuspendablestrategy import ISuspendableStrategy
class ILadderStrategy(ISuspendableStrategy):
    def LadderBalancer(self, maximalSize = None):
        from marketsim.gen._out.strategy.price._ladderbalancer import LadderBalancer
        return LadderBalancer(self,maximalSize)
    
    pass
