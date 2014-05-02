# generated with class generator.python.accessor$Import
from marketsim import registry
from marketsim.gen._out.math._moving import Moving
@registry.expose(["-", "Timeframe"])
class Timeframe_mathMoving(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._moving import Moving_IObservableFloatFloat as _math_Moving_IObservableFloatFloat
        from marketsim import deref_opt
        self.x = x if x is not None else deref_opt(_math_Moving_IObservableFloatFloat())
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    
    
    def __repr__(self):
        return "Moving_{%(timeframe)s}(%(source)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        from marketsim.gen._out.math._moving import Moving
        rtti.typecheck(Moving, self.x)
    
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
    
# generated with class generator.python.accessor$Import
from marketsim import registry
from marketsim.gen._out.math._rsi import RSI
@registry.expose(["-", "Timeframe"])
class Timeframe_mathRSI(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._rsi import RSI_IObservableFloatFloatFloat as _math_RSI_IObservableFloatFloatFloat
        from marketsim import deref_opt
        self.x = x if x is not None else deref_opt(_math_RSI_IObservableFloatFloatFloat())
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : RSI
    }
    
    
    def __repr__(self):
        return "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        from marketsim.gen._out.math._rsi import RSI
        rtti.typecheck(RSI, self.x)
    
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
    from marketsim.gen._out.math._moving import Moving
    from marketsim.gen._out.math._rsi import RSI
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Moving):
        return Timeframe_mathMoving(x)
    if x is None or rtti.can_be_casted(x, RSI):
        return Timeframe_mathRSI(x)
    raise Exception('Cannot find suitable overload for Timeframe('+str(x) +':'+ str(type(x))+')')
