# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._intrinsic.event import Every_Impl
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Event", "Every"])
class Every_Float(IEvent,Every_Impl):
    """ **Event that fires every *intervalFunc* moments of time**
    
    
    Parameters are:
    
    **intervalFunc**
    	 interval of time between two events 
    """ 
    def __init__(self, intervalFunc = None):
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.intervalFunc = intervalFunc if intervalFunc is not None else deref_opt(_math_random_expovariate_Float(1.0))
        rtti.check_fields(self)
        Every_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'intervalFunc' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "Every(%(intervalFunc)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.intervalFunc.bind_ex(self._ctx_ex)
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
        self.intervalFunc.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        Every_Impl.bind_impl(self, ctx)
    
    def reset(self):
        Every_Impl.reset(self)
    
def Every(intervalFunc = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if intervalFunc is None or rtti.can_be_casted(intervalFunc, IFunctionfloat):
        return Every_Float(intervalFunc)
    raise Exception('Cannot find suitable overload for Every('+str(intervalFunc) +':'+ str(type(intervalFunc))+')')
