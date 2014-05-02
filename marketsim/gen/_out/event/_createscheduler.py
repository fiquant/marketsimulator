# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out.event._ischeduler import IScheduler
from marketsim.gen._intrinsic.scheduler import Scheduler_Impl
@registry.expose(["Event", "createScheduler"])
class createScheduler_Float(IScheduler,Scheduler_Impl):
    """ **Scheduler that manages the future event set.**
    
     Must be a singleton
    
    Parameters are:
    
    **currentTime**
    """ 
    def __init__(self, currentTime = None):
        self.currentTime = currentTime if currentTime is not None else 0.0
        Scheduler_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'currentTime' : float
    }
    
    
    def __repr__(self):
        return "createScheduler(%(currentTime)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        rtti.typecheck(float, self.currentTime)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        
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
        Scheduler_Impl.bind_impl(self, ctx)
    
    def reset(self):
        Scheduler_Impl.reset(self)
    
def createScheduler(currentTime = None): 
    from marketsim import rtti
    if currentTime is None or rtti.can_be_casted(currentTime, float):
        return createScheduler_Float(currentTime)
    raise Exception('Cannot find suitable overload for createScheduler('+str(currentTime) +':'+ str(type(currentTime))+')')
