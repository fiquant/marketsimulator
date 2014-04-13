# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out.strategy.price._iladderstrategy import ILadderStrategy
from marketsim.gen._intrinsic.strategy.ladder import Balancer_Impl
@registry.expose(["Price function", "LadderBalancer"])
class LadderBalancer_strategypriceILadderStrategyInt(ILadderStrategy,Balancer_Impl):
    """ 
    """ 
    def __init__(self, inner = None, maximalSize = None):
        from marketsim.gen._out.strategy.price._laddermm import LadderMM_SideFloatIObservableIOrderInt as _strategy_price_LadderMM_SideFloatIObservableIOrderInt
        from marketsim import deref_opt
        from marketsim import rtti
        self.inner = inner if inner is not None else deref_opt(_strategy_price_LadderMM_SideFloatIObservableIOrderInt())
        self.maximalSize = maximalSize if maximalSize is not None else 20
        rtti.check_fields(self)
        Balancer_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ILadderStrategy,
        'maximalSize' : int
    }
    
    
    
    
    def __repr__(self):
        return "LadderBalancer(%(inner)s, %(maximalSize)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def LadderBalancer(inner = None,maximalSize = None): 
    from marketsim.gen._out.strategy.price._iladderstrategy import ILadderStrategy
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ILadderStrategy):
        if maximalSize is None or rtti.can_be_casted(maximalSize, int):
            return LadderBalancer_strategypriceILadderStrategyInt(inner,maximalSize)
    raise Exception('Cannot find suitable overload for LadderBalancer('+str(inner) +':'+ str(type(inner))+','+str(maximalSize) +':'+ str(type(maximalSize))+')')
