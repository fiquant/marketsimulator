from marketsim import registry
from marketsim.gen._out.strategy.position._rsi_linear import RSI_linear
@registry.expose(["-", "Timeframe"])
class Timeframe_strategypositionRSI_linear(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.position._rsi_linear import RSI_linear_FloatIObservableFloatFloatISingleAssetTrader as _strategy_position_RSI_linear_FloatIObservableFloatFloatISingleAssetTrader
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_position_RSI_linear_FloatIObservableFloatFloatISingleAssetTrader())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : RSI_linear
    }
    
    
    def __repr__(self):
        return "Timeframe(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    @property
    def dereference(self):
        return self.x.timeframe
    
def Timeframe(x = None): 
    from marketsim.gen._out.strategy.position._rsi_linear import RSI_linear
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, RSI_linear):
        return Timeframe_strategypositionRSI_linear(x)
    raise Exception('Cannot find suitable overload for Timeframe('+str(x) +':'+ str(type(x))+')')
