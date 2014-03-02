class IEvent(object):
    def Signal(self, orderFactory = None,signal = None,threshold = None):
        from marketsim.gen._out.strategy._signal import Signal
        return Signal(self,orderFactory,signal,threshold)
    
    def LiquidityProvider(self, orderFactory = None,initialValue = None,priceDistr = None):
        from marketsim.gen._out.strategy._liquidityprovider import LiquidityProvider
        return LiquidityProvider(self,orderFactory,initialValue,priceDistr)
    
    def RSIbis(self, orderFactory = None,alpha = None,timeframe = None,threshold = None):
        from marketsim.gen._out.strategy._rsibis import RSIbis
        return RSIbis(self,orderFactory,alpha,timeframe,threshold)
    
    def LiquidityProviderSide(self, orderFactory = None,side = None,initialValue = None,priceDistr = None):
        from marketsim.gen._out.strategy._liquidityproviderside import LiquidityProviderSide
        return LiquidityProviderSide(self,orderFactory,side,initialValue,priceDistr)
    
    def Noise(self, orderFactory = None):
        from marketsim.gen._out.strategy._noise import Noise
        return Noise(self,orderFactory)
    
    pass
