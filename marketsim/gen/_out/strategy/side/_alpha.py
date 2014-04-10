# generated with class generator.python.accessor$Import
from marketsim import registry
from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
@registry.expose(["-", "Alpha"])
class Alpha_strategysideMeanReversion(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._meanreversion import MeanReversion_Float as _strategy_side_MeanReversion_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_MeanReversion_Float())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MeanReversion
    }
    
    
    def __repr__(self):
        return "Alpha(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
    @property
    def dereference(self):
        return self.x.alpha
    
# generated with class generator.python.accessor$Import
from marketsim import registry
from marketsim.gen._out.strategy.side._rsibis import RSIbis
@registry.expose(["-", "Alpha"])
class Alpha_strategysideRSIbis(object):
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
        return "Alpha(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
    @property
    def dereference(self):
        return self.x.alpha
    
# generated with class generator.python.accessor$Import
from marketsim import registry
from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
@registry.expose(["-", "Alpha"])
class Alpha_strategysideTrendFollower(object):
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
        return "Alpha(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
    @property
    def dereference(self):
        return self.x.alpha
    
def Alpha(x = None): 
    from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
    from marketsim.gen._out.strategy.side._rsibis import RSIbis
    from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, MeanReversion):
        return Alpha_strategysideMeanReversion(x)
    if x is None or rtti.can_be_casted(x, RSIbis):
        return Alpha_strategysideRSIbis(x)
    if x is None or rtti.can_be_casted(x, TrendFollower):
        return Alpha_strategysideTrendFollower(x)
    raise Exception('Cannot find suitable overload for Alpha('+str(x) +':'+ str(type(x))+')')
