from marketsim import registry
from marketsim.gen._out.strategy.position._desiredpositionstrategy import DesiredPositionStrategy
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
@registry.expose(["-", "RSI_linear"])
class RSI_linear_FloatIObservableFloatFloatISingleAssetTrader(DesiredPositionStrategy):
    """ 
    """ 
    def __init__(self, alpha = None, k = None, timeframe = None, trader = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim import rtti
        self.alpha = alpha if alpha is not None else (1.0/14.0)
        self.k = k if k is not None else deref_opt(_const_Float(-0.04))
        self.timeframe = timeframe if timeframe is not None else 1.0
        self.trader = trader if trader is not None else deref_opt(_trader_SingleProxy_())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float,
        'k' : IObservablefloat,
        'timeframe' : float,
        'trader' : ISingleAssetTrader
    }
    def __repr__(self):
        return "RSI_linear(%(alpha)s, %(k)s, %(timeframe)s, %(trader)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    

    @property
    def Timeframe(self):
        from marketsim.gen._out.strategy.position._timeframe import Timeframe
        return Timeframe(self)
    
    @property
    def Trader(self):
        from marketsim.gen._out.strategy.position._trader import Trader
        return Trader(self)
    
    @property
    def DesiredPosition(self):
        from marketsim.gen._out.strategy.position._desiredposition import DesiredPosition
        return DesiredPosition(self)
    
    @property
    def Position(self):
        from marketsim.gen._out.strategy.position._position import Position
        return Position(self)
    
    def Strategy(self, orderFactory = None):
        from marketsim.gen._out.strategy.position._strategy import Strategy
        return Strategy(self,orderFactory)
    
    @property
    def K(self):
        from marketsim.gen._out.strategy.position._k import K
        return K(self)
    
    @property
    def Alpha(self):
        from marketsim.gen._out.strategy.position._alpha import Alpha
        return Alpha(self)
    
    pass
RSI_linear = RSI_linear_FloatIObservableFloatFloatISingleAssetTrader
