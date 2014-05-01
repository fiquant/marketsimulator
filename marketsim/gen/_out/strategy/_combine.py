# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._intrinsic.strategy.combine import Combine_Impl
@registry.expose(["Strategy", "Combine"])
class Combine_ISingleAssetStrategyISingleAssetStrategy(ISingleAssetStrategy,Combine_Impl):
    """ **Creates a strategy combining two strategies**
    
      Can be considered as a particular case of Array strategy
    
    Parameters are:
    
    **A**
    
    **B**
    """ 
    def __init__(self, A = None, B = None):
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim import deref_opt
        from marketsim import rtti
        self.A = A if A is not None else deref_opt(_strategy_Empty_())
        self.B = B if B is not None else deref_opt(_strategy_Empty_())
        rtti.check_fields(self)
        Combine_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'A' : ISingleAssetStrategy,
        'B' : ISingleAssetStrategy
    }
    
    
    
    
    def __repr__(self):
        return "Combine(%(A)s, %(B)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.A.bind_ex(self._ctx_ex)
        self.B.bind_ex(self._ctx_ex)
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
        self.A.reset_ex(generation)
        self.B.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        Combine_Impl.bind_impl(self, ctx)
    
    def reset(self):
        Combine_Impl.reset(self)
    
def Combine(A = None,B = None): 
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim import rtti
    if A is None or rtti.can_be_casted(A, ISingleAssetStrategy):
        if B is None or rtti.can_be_casted(B, ISingleAssetStrategy):
            return Combine_ISingleAssetStrategyISingleAssetStrategy(A,B)
    raise Exception('Cannot find suitable overload for Combine('+str(A) +':'+ str(type(A))+','+str(B) +':'+ str(type(B))+')')
