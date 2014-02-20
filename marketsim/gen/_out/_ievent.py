class IEvent(object):
    def PairTrading(self, orderFactory = None,bookToDependOn = None,factor = None):
        from marketsim.gen._out.strategy._pairtrading import PairTrading
        return PairTrading(self,orderFactory,bookToDependOn,factor)
    
    def Signal(self, orderFactory = None,signal = None,threshold = None):
        from marketsim.gen._out.strategy._signal import Signal
        return Signal(self,orderFactory,signal,threshold)
    
    def LiquidityProvider(self, orderFactory = None,initialValue = None,priceDistr = None):
        from marketsim.gen._out.strategy._liquidityprovider import LiquidityProvider
        return LiquidityProvider(self,orderFactory,initialValue,priceDistr)
    
    def CrossingAverages(self, orderFactory = None,ewma_alpha_1 = None,ewma_alpha_2 = None,threshold = None):
        from marketsim.gen._out.strategy._crossingaverages import CrossingAverages
        return CrossingAverages(self,orderFactory,ewma_alpha_1,ewma_alpha_2,threshold)
    
    def TrendFollower(self, orderFactory = None,ewma_alpha = None,threshold = None):
        from marketsim.gen._out.strategy._trendfollower import TrendFollower
        return TrendFollower(self,orderFactory,ewma_alpha,threshold)
    
    def FundamentalValue(self, orderFactory = None,fundamentalValue = None):
        from marketsim.gen._out.strategy._fundamentalvalue import FundamentalValue
        return FundamentalValue(self,orderFactory,fundamentalValue)
    
    def RSIbis(self, orderFactory = None,alpha = None,timeframe = None,threshold = None):
        from marketsim.gen._out.strategy._rsibis import RSIbis
        return RSIbis(self,orderFactory,alpha,timeframe,threshold)
    
    def MeanReversion(self, orderFactory = None,ewma_alpha = None):
        from marketsim.gen._out.strategy._meanreversion import MeanReversion
        return MeanReversion(self,orderFactory,ewma_alpha)
    
    def LiquidityProviderSide(self, orderFactory = None,side = None,initialValue = None,priceDistr = None):
        from marketsim.gen._out.strategy._liquidityproviderside import LiquidityProviderSide
        return LiquidityProviderSide(self,orderFactory,side,initialValue,priceDistr)
    
    def Noise(self, orderFactory = None):
        from marketsim.gen._out.strategy._noise import Noise
        return Noise(self,orderFactory)
    
    pass
