# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._isuspendablestrategy import ISuspendableStrategy
from marketsim.gen._intrinsic.strategy.ladder import StopLoss_Impl
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Price function", "StopLoss"])
class StopLoss_ISuspendableStrategyFloat(ISuspendableStrategy,StopLoss_Impl):
    """ 
    """ 
    def __init__(self, inner = None, lossFactor = None):
        from marketsim.gen._out.strategy.price._laddermm import LadderMM_SideFloatIObservableIOrderInt as _strategy_price_LadderMM_SideFloatIObservableIOrderInt
        from marketsim import deref_opt
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.inner = inner if inner is not None else deref_opt(_strategy_price_LadderMM_SideFloatIObservableIOrderInt())
        self.lossFactor = lossFactor if lossFactor is not None else deref_opt(_constant_Float(0.2))
        rtti.check_fields(self)
        StopLoss_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISuspendableStrategy,
        'lossFactor' : IFunctionfloat
    }
    
    
    
    
    def __repr__(self):
        return "StopLoss(%(inner)s, %(lossFactor)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.lossFactor.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def StopLoss(inner = None,lossFactor = None): 
    from marketsim.gen._out._isuspendablestrategy import ISuspendableStrategy
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ISuspendableStrategy):
        if lossFactor is None or rtti.can_be_casted(lossFactor, IFunctionfloat):
            return StopLoss_ISuspendableStrategyFloat(inner,lossFactor)
    raise Exception('Cannot find suitable overload for StopLoss('+str(inner) +':'+ str(type(inner))+','+str(lossFactor) +':'+ str(type(lossFactor))+')')
