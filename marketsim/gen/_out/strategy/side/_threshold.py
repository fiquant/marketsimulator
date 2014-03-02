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
        return "Threshold(%(x)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.threshold
    
def Threshold(x = None): 
    from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, CrossingAverages):
        return Threshold_strategysideCrossingAverages(x)
    raise Exception('Cannot find suitable overload for Threshold('+str(x) +':'+ str(type(x))+')')
