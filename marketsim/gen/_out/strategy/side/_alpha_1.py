from marketsim import registry
from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
@registry.expose(["-", "Alpha_1"])
class Alpha_1_strategysideCrossingAverages(object):
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
        return "Alpha_1(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = ctx
        self.x.bindEx(self._ctx_ex)
        delattr(self, '_processing_ex')
    
    @property
    def dereference(self):
        return self.x.alpha_1
    
def Alpha_1(x = None): 
    from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, CrossingAverages):
        return Alpha_1_strategysideCrossingAverages(x)
    raise Exception('Cannot find suitable overload for Alpha_1('+str(x) +':'+ str(type(x))+')')
