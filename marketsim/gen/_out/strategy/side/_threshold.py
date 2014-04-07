from marketsim import registry
from marketsim.gen._out.strategy.side._rsibis import RSIbis
@registry.expose(["-", "Threshold"])
class Threshold_strategysideRSIbis(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._rsibis import RSIbis_FloatFloatFloat as _strategy_side_RSIbis_FloatFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_RSIbis_FloatFloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : RSIbis
    }
    
    
    def __repr__(self):
        return "Threshold(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    @property
    def dereference(self):
        return self.x.threshold
    
from marketsim import registry
from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
@registry.expose(["-", "Threshold"])
class Threshold_strategysideTrendFollower(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._trendfollower import TrendFollower_FloatFloatIOrderBook as _strategy_side_TrendFollower_FloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_TrendFollower_FloatFloatIOrderBook())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : TrendFollower
    }
    
    
    def __repr__(self):
        return "Threshold(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    @property
    def dereference(self):
        return self.x.threshold
    
from marketsim import registry
from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
@registry.expose(["-", "Threshold"])
class Threshold_strategysideCrossingAverages(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages_FloatFloatFloatIOrderBook as _strategy_side_CrossingAverages_FloatFloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_CrossingAverages_FloatFloatFloatIOrderBook())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : CrossingAverages
    }
    
    
    def __repr__(self):
        return "Threshold(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    @property
    def dereference(self):
        return self.x.threshold
    
from marketsim import registry
from marketsim.gen._out.strategy.side._signal import Signal
@registry.expose(["-", "Threshold"])
class Threshold_strategysideSignal(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._signal import Signal_FloatFloat as _strategy_side_Signal_FloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_Signal_FloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Signal
    }
    
    
    def __repr__(self):
        return "Threshold(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    @property
    def dereference(self):
        return self.x.threshold
    
def Threshold(x = None): 
    from marketsim.gen._out.strategy.side._rsibis import RSIbis
    from marketsim import rtti
    from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
    from marketsim.gen._out.strategy.side._signal import Signal
    from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
    if x is None or rtti.can_be_casted(x, RSIbis):
        return Threshold_strategysideRSIbis(x)
    if x is None or rtti.can_be_casted(x, TrendFollower):
        return Threshold_strategysideTrendFollower(x)
    if x is None or rtti.can_be_casted(x, CrossingAverages):
        return Threshold_strategysideCrossingAverages(x)
    if x is None or rtti.can_be_casted(x, Signal):
        return Threshold_strategysideSignal(x)
    raise Exception('Cannot find suitable overload for Threshold('+str(x) +':'+ str(type(x))+')')
