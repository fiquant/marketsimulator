from marketsim import registry
from marketsim.gen._out.strategy.position._desiredpositionstrategy import DesiredPositionStrategy
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
@registry.expose(["-", "Bollinger_linear"])
class Bollinger_linear_FloatIObservableFloatISingleAssetTrader(DesiredPositionStrategy):
    """ 
    """ 
    def __init__(self, alpha = None, k = None, trader = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim import rtti
        self.alpha = alpha if alpha is not None else 0.15
        self.k = k if k is not None else deref_opt(_const_Float(0.5))
        self.trader = trader if trader is not None else deref_opt(_trader_SingleProxy_())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float,
        'k' : IObservablefloat,
        'trader' : ISingleAssetTrader
    }
    
    
    
    
    
    
    def __repr__(self):
        return "Bollinger_linear(%(alpha)s, %(k)s, %(trader)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    

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
Bollinger_linear = Bollinger_linear_FloatIObservableFloatISingleAssetTrader
