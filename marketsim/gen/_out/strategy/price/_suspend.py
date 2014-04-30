# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._isuspendablestrategy import ISuspendableStrategy
from marketsim.gen._intrinsic.strategy.ladder import Suspend_Impl
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
@registry.expose(["Price function", "Suspend"])
class Suspend_ISuspendableStrategyBoolean(ISuspendableStrategy,Suspend_Impl):
    """ 
    """ 
    def __init__(self, inner = None, predicate = None):
        from marketsim.gen._out.strategy.price._laddermm import LadderMM_SideFloatIObservableIOrderInt as _strategy_price_LadderMM_SideFloatIObservableIOrderInt
        from marketsim import deref_opt
        from marketsim.gen._out._false import false_ as _false_
        from marketsim import rtti
        self.inner = inner if inner is not None else deref_opt(_strategy_price_LadderMM_SideFloatIObservableIOrderInt())
        self.predicate = predicate if predicate is not None else deref_opt(_false_())
        rtti.check_fields(self)
        Suspend_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISuspendableStrategy,
        'predicate' : IFunctionbool
    }
    
    
    
    
    def __repr__(self):
        return "Suspend(%(inner)s, %(predicate)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.inner.bind_ex(self._ctx_ex)
        self.predicate.bind_ex(self._ctx_ex)
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
        self.inner.reset_ex(generation)
        self.predicate.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
def Suspend(inner = None,predicate = None): 
    from marketsim.gen._out._isuspendablestrategy import ISuspendableStrategy
    from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ISuspendableStrategy):
        if predicate is None or rtti.can_be_casted(predicate, IFunctionbool):
            return Suspend_ISuspendableStrategyBoolean(inner,predicate)
    raise Exception('Cannot find suitable overload for Suspend('+str(inner) +':'+ str(type(inner))+','+str(predicate) +':'+ str(type(predicate))+')')
