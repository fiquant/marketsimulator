# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._intrinsic.strategy.combine import Array_Impl
from marketsim import listOf
@registry.expose(["Strategy", "Array"])
class Array_ListISingleAssetStrategy(ISingleAssetStrategy,Array_Impl):
    """ **Creates a strategy combining an array of strategies**
    
    
    Parameters are:
    
    **strategies**
    	 strategies to combine 
    """ 
    def __init__(self, strategies = None):
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim import deref_opt
        from marketsim import rtti
        self.strategies = strategies if strategies is not None else [deref_opt(_strategy_Empty_())]
        rtti.check_fields(self)
        Array_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'strategies' : listOf(ISingleAssetStrategy)
    }
    
    
    def __repr__(self):
        return "Array(%(strategies)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        for x in self.strategies: x.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
def Array(strategies = None): 
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim import listOf
    from marketsim import rtti
    if strategies is None or rtti.can_be_casted(strategies, listOf(ISingleAssetStrategy)):
        return Array_ListISingleAssetStrategy(strategies)
    raise Exception('Cannot find suitable overload for Array('+str(strategies) +':'+ str(type(strategies))+')')
