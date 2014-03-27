from marketsim import registry
from marketsim.gen._out.strategy.side._rsibis import RSIbis
@registry.expose(["-", "Timeframe"])
class Timeframe_strategysideRSIbis(object):
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
        return "Timeframe(%(x)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
    @property
    def dereference(self):
        return self.x.timeframe
    
def Timeframe(x = None): 
    from marketsim.gen._out.strategy.side._rsibis import RSIbis
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, RSIbis):
        return Timeframe_strategysideRSIbis(x)
    raise Exception('Cannot find suitable overload for Timeframe('+str(x) +':'+ str(type(x))+')')
