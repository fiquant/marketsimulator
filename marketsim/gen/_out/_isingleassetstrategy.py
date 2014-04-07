class ISingleAssetStrategy(object):
    def Combine(self, B = None):
        from marketsim.gen._out.strategy._combine import Combine
        return Combine(self,B)
    
    @property
    def Real(self):
        from marketsim.gen._out.strategy.account._real import Real
        return Real(self)
    
    def Suspendable(self, predicate = None):
        from marketsim.gen._out.strategy._suspendable import Suspendable
        return Suspendable(self,predicate)
    
    def TradeIfProfitable(self, account = None,performance = None):
        from marketsim.gen._out.strategy._tradeifprofitable import TradeIfProfitable
        return TradeIfProfitable(self,account,performance)
    
    @property
    def VirtualMarket(self):
        from marketsim.gen._out.strategy.account._virtualmarket import VirtualMarket
        return VirtualMarket(self)
    
    pass
