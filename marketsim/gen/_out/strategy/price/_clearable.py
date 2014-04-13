# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._isuspendablestrategy import ISuspendableStrategy
from marketsim.gen._intrinsic.strategy.ladder import Clearable_Impl
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
@registry.expose(["Price function", "Clearable"])
class Clearable_ISuspendableStrategyBoolean(ISuspendableStrategy,Clearable_Impl):
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
        Clearable_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISuspendableStrategy,
        'predicate' : IFunctionbool
    }
    
    
    
    
    def __repr__(self):
        return "Clearable(%(inner)s, %(predicate)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self._ctx_ex)
                else:
                    v.bind_ex(self._ctx_ex)
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        self.inner.bind_ex(self._ctx_ex)
        self.predicate.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def Clearable(inner = None,predicate = None): 
    from marketsim.gen._out._isuspendablestrategy import ISuspendableStrategy
    from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ISuspendableStrategy):
        if predicate is None or rtti.can_be_casted(predicate, IFunctionbool):
            return Clearable_ISuspendableStrategyBoolean(inner,predicate)
    raise Exception('Cannot find suitable overload for Clearable('+str(inner) +':'+ str(type(inner))+','+str(predicate) +':'+ str(type(predicate))+')')
