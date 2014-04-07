from marketsim import registry
from marketsim.gen._out.strategy.position._rsi_linear import RSI_linear
@registry.expose(["-", "Alpha"])
class Alpha_strategypositionRSI_linear(object):
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
        return "Alpha(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    @property
    def dereference(self):
        return self.x.alpha
    
from marketsim import registry
from marketsim.gen._out.strategy.position._bollinger_linear import Bollinger_linear
@registry.expose(["-", "Alpha"])
class Alpha_strategypositionBollinger_linear(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.position._bollinger_linear import Bollinger_linear_FloatIObservableFloatISingleAssetTrader as _strategy_position_Bollinger_linear_FloatIObservableFloatISingleAssetTrader
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_position_Bollinger_linear_FloatIObservableFloatISingleAssetTrader())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Bollinger_linear
    }
    
    
    def __repr__(self):
        return "Alpha(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    @property
    def dereference(self):
        return self.x.alpha
    
def Alpha(x = None): 
    from marketsim.gen._out.strategy.position._rsi_linear import RSI_linear
    from marketsim.gen._out.strategy.position._bollinger_linear import Bollinger_linear
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, RSI_linear):
        return Alpha_strategypositionRSI_linear(x)
    if x is None or rtti.can_be_casted(x, Bollinger_linear):
        return Alpha_strategypositionBollinger_linear(x)
    raise Exception('Cannot find suitable overload for Alpha('+str(x) +':'+ str(type(x))+')')
