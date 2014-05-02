# generated with class generator.python.accessor$Import
from marketsim import registry
from marketsim.gen._out.strategy.side._rsibis import RSIbis
@registry.expose(["-", "Timeframe"])
class Timeframe_strategysideRSIbis(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._rsibis import RSIbis_FloatFloatFloat as _strategy_side_RSIbis_FloatFloatFloat
        from marketsim import deref_opt
        self.x = x if x is not None else deref_opt(_strategy_side_RSIbis_FloatFloatFloat())
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : RSIbis
    }
    
    
    def __repr__(self):
        return "Timeframe(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out.strategy.side._rsibis import RSIbis
        rtti.typecheck(RSIbis, self.x)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    @property
    def dereference(self):
        return self.x.timeframe
    
def Timeframe(x = None): 
    from marketsim.gen._out.strategy.side._rsibis import RSIbis
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, RSIbis):
        return Timeframe_strategysideRSIbis(x)
    raise Exception('Cannot find suitable overload for Timeframe('+str(x) +':'+ str(type(x))+')')
