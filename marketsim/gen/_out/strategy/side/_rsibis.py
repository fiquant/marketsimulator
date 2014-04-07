from marketsim import registry
from marketsim.gen._out.strategy.side._signalstrategy import SignalStrategy
@registry.expose(["-", "RSIbis"])
class RSIbis_FloatFloatFloat(SignalStrategy):
    """ 
    """ 
    def __init__(self, alpha = None, timeframe = None, threshold = None):
        from marketsim import rtti
        self.alpha = alpha if alpha is not None else (1.0/14)
        self.timeframe = timeframe if timeframe is not None else 1.0
        self.threshold = threshold if threshold is not None else 30.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float,
        'timeframe' : float,
        'threshold' : float
    }
    
    
    
    
    
    
    def __repr__(self):
        return "RSIbis(%(alpha)s, %(timeframe)s, %(threshold)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    

    @property
    def Timeframe(self):
        from marketsim.gen._out.strategy.side._timeframe import Timeframe
        return Timeframe(self)
    
    @property
    def Threshold(self):
        from marketsim.gen._out.strategy.side._threshold import Threshold
        return Threshold(self)
    
    @property
    def Side(self):
        from marketsim.gen._out.strategy.side._side import Side
        return Side(self)
    
    def Strategy(self, eventGen = None,orderFactory = None):
        from marketsim.gen._out.strategy.side._strategy import Strategy
        return Strategy(self,eventGen,orderFactory)
    
    @property
    def Signal_Value(self):
        from marketsim.gen._out.strategy.side._signal_value import Signal_Value
        return Signal_Value(self)
    
    @property
    def Alpha(self):
        from marketsim.gen._out.strategy.side._alpha import Alpha
        return Alpha(self)
    
    pass
RSIbis = RSIbis_FloatFloatFloat
