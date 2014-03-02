class Float(object):
    def RSI_linear(self, k = None,timeframe = None,trader = None):
        from marketsim.gen._out.strategy.position._rsi_linear import RSI_linear
        return RSI_linear(self,k,timeframe,trader)
    
    def gammavariate(self, Beta = None):
        from marketsim.gen._out.math.random._gammavariate import gammavariate
        return gammavariate(self,Beta)
    
    @property
    def constant(self):
        from marketsim.gen._out._constant import constant
        return constant(self)
    
    def normalvariate(self, Sigma = None):
        from marketsim.gen._out.math.random._normalvariate import normalvariate
        return normalvariate(self,Sigma)
    
    def CrossingAverages(self, alpha_2 = None,threshold = None,book = None):
        from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
        return CrossingAverages(self,alpha_2,threshold,book)
    
    @property
    def paretovariate(self):
        from marketsim.gen._out.math.random._paretovariate import paretovariate
        return paretovariate(self)
    
    def TrendFollower(self, threshold = None,book = None):
        from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
        return TrendFollower(self,threshold,book)
    
    @property
    def trader_TraderEfficiencyTrend(self):
        from marketsim.gen._out.strategy.weight.trader._trader_traderefficiencytrend import trader_TraderEfficiencyTrend
        return trader_TraderEfficiencyTrend(self)
    
    def RSIbis(self, timeframe = None,threshold = None):
        from marketsim.gen._out.strategy.side._rsibis import RSIbis
        return RSIbis(self,timeframe,threshold)
    
    def triangular(self, High = None,Mode = None):
        from marketsim.gen._out.math.random._triangular import triangular
        return triangular(self,High,Mode)
    
    def vonmisesvariate(self, Kappa = None):
        from marketsim.gen._out.math.random._vonmisesvariate import vonmisesvariate
        return vonmisesvariate(self,Kappa)
    
    def uniform(self, High = None):
        from marketsim.gen._out.math.random._uniform import uniform
        return uniform(self,High)
    
    def MeanReversion(self, book = None):
        from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
        return MeanReversion(self,book)
    
    @property
    def const(self):
        from marketsim.gen._out._const import const
        return const(self)
    
    def weibullvariate(self, Beta = None):
        from marketsim.gen._out.math.random._weibullvariate import weibullvariate
        return weibullvariate(self,Beta)
    
    def RandomWalk(self, deltaDistr = None,intervalDistr = None,name = None):
        from marketsim.gen._out.math._randomwalk import RandomWalk
        return RandomWalk(self,deltaDistr,intervalDistr,name)
    
    @property
    def expovariate(self):
        from marketsim.gen._out.math.random._expovariate import expovariate
        return expovariate(self)
    
    def lognormvariate(self, Sigma = None):
        from marketsim.gen._out.math.random._lognormvariate import lognormvariate
        return lognormvariate(self,Sigma)
    
    def betavariate(self, Beta = None):
        from marketsim.gen._out.math.random._betavariate import betavariate
        return betavariate(self,Beta)
    
    @property
    def f_AtanPow(self):
        from marketsim.gen._out.strategy.weight.f._f_atanpow import f_AtanPow
        return f_AtanPow(self)
    
    def MarketMaker(self, volume = None):
        from marketsim.gen._out.strategy._marketmaker import MarketMaker
        return MarketMaker(self,volume)
    
    def Bollinger_linear(self, k = None,trader = None):
        from marketsim.gen._out.strategy.position._bollinger_linear import Bollinger_linear
        return Bollinger_linear(self,k,trader)
    
    pass
