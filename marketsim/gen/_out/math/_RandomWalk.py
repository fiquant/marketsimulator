# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.observable.randomwalk import RandomWalk_Impl
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Basic", "RandomWalk"])
class RandomWalk_FloatFloatFloatString(Observablefloat,RandomWalk_Impl):
    """ **A discrete signal with user-defined increments.**
    
    
    Parameters are:
    
    **initialValue**
    	 initial value of the signal 
    
    **deltaDistr**
    	 increment function 
    
    **intervalDistr**
    	 intervals between signal updates 
    
    **name**
    """ 
    def __init__(self, initialValue = None, deltaDistr = None, intervalDistr = None, name = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out.math.random._normalvariate import normalvariate_FloatFloat as _math_random_normalvariate_FloatFloat
        from marketsim import deref_opt
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        Observablefloat.__init__(self)
        self.initialValue = initialValue if initialValue is not None else 0.0
        self.deltaDistr = deltaDistr if deltaDistr is not None else deref_opt(_math_random_normalvariate_FloatFloat(0.0,1.0))
        self.intervalDistr = intervalDistr if intervalDistr is not None else deref_opt(_math_random_expovariate_Float(1.0))
        self.name = name if name is not None else "-random-"
        RandomWalk_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'initialValue' : float,
        'deltaDistr' : IFunctionfloat,
        'intervalDistr' : IFunctionfloat,
        'name' : str
    }
    
    
    
    
    
    
    
    
    
    
    
    
    def __repr__(self):
        return "%(name)s" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.deltaDistr.bind_ex(self._ctx_ex)
        self.intervalDistr.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.deltaDistr.reset_ex(generation)
        self.intervalDistr.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
        rtti.typecheck(float, self.initialValue)
        rtti.typecheck(IFunctionfloat, self.deltaDistr)
        rtti.typecheck(IFunctionfloat, self.intervalDistr)
        rtti.typecheck(str, self.name)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.deltaDistr.registerIn(registry)
        self.intervalDistr.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.registerIn(registry)
                else:
                    v.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        RandomWalk_Impl.bind_impl(self, ctx)
    
    def reset(self):
        RandomWalk_Impl.reset(self)
    
def RandomWalk(initialValue = None,deltaDistr = None,intervalDistr = None,name = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if initialValue is None or rtti.can_be_casted(initialValue, float):
        if deltaDistr is None or rtti.can_be_casted(deltaDistr, IFunctionfloat):
            if intervalDistr is None or rtti.can_be_casted(intervalDistr, IFunctionfloat):
                if name is None or rtti.can_be_casted(name, str):
                    return RandomWalk_FloatFloatFloatString(initialValue,deltaDistr,intervalDistr,name)
    raise Exception('Cannot find suitable overload for RandomWalk('+str(initialValue) +':'+ str(type(initialValue))+','+str(deltaDistr) +':'+ str(type(deltaDistr))+','+str(intervalDistr) +':'+ str(type(intervalDistr))+','+str(name) +':'+ str(type(name))+')')
