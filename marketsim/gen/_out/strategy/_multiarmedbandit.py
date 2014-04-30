# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount import IFunctionIFunctionfloat_from_IAccount
from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_ifunctionfloat import IFunctionIFunctionfloat_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionlistoffloat_from_listoffloat import IFunctionIFunctionlistOffloat_from_listOffloat
from marketsim.gen._intrinsic.strategy.multiarmed_bandit import MultiarmedBandit2_Impl
from marketsim import listOf
from marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy import IFunctionIAccount_from_ISingleAssetStrategy
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
@registry.expose(["Strategy", "MultiArmedBandit"])
class MultiArmedBandit_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloatFloatFloatListFloatListFloat(ISingleAssetStrategy,MultiarmedBandit2_Impl):
    """ **A composite strategy initialized with an array of strategies.**
    
     In some moments of time the efficiency of the strategies is evaluated
     These efficiencies are mapped into weights using *weight* and *normilizer*
     functions per every strategy and *corrector* for the whole collection of weights
     These weights are used to choose randomly a strategy to run for the next quant of time.
     All other strategies are suspended
    
    Parameters are:
    
    **strategies**
    	 original strategies that can be suspended 
    
    **account**
    	 function creating a virtual account used
    	 to estimate efficiency of the strategy itself 
    
    **weight**
    	 function estimating is the strategy efficient or not 
    
    **normalizer**
    	 function that maps trader efficiency to its weight
    	 that will be used for random choice 
    
    **corrector**
    	 given array of strategy weights corrects them.
    	 for example it may set to 0 all weights except the maximal one 
    """ 
    def __init__(self, strategies = None, account = None, weight = None, normalizer = None, corrector = None):
        from marketsim.gen._out.strategy.account.inner._inner_virtualmarket import inner_VirtualMarket_ as _strategy_account_inner_inner_VirtualMarket_
        from marketsim import rtti
        from marketsim.gen._out.strategy.weight.array._array_identityl import array_IdentityL_ as _strategy_weight_array_array_IdentityL_
        from marketsim.gen._out.strategy.weight.f._f_atanpow import f_AtanPow_Float as _strategy_weight_f_f_AtanPow_Float
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim.gen._out.strategy.weight.trader._trader_traderefficiencytrend import trader_TraderEfficiencyTrend_Float as _strategy_weight_trader_trader_TraderEfficiencyTrend_Float
        from marketsim import deref_opt
        self.strategies = strategies if strategies is not None else [deref_opt(_strategy_Empty_())]
        self.account = account if account is not None else deref_opt(_strategy_account_inner_inner_VirtualMarket_())
        self.weight = weight if weight is not None else deref_opt(_strategy_weight_trader_trader_TraderEfficiencyTrend_Float())
        self.normalizer = normalizer if normalizer is not None else deref_opt(_strategy_weight_f_f_AtanPow_Float())
        self.corrector = corrector if corrector is not None else deref_opt(_strategy_weight_array_array_IdentityL_())
        rtti.check_fields(self)
        MultiarmedBandit2_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'strategies' : listOf(ISingleAssetStrategy),
        'account' : IFunctionIAccount_from_ISingleAssetStrategy,
        'weight' : IFunctionIFunctionfloat_from_IAccount,
        'normalizer' : IFunctionIFunctionfloat_from_IFunctionfloat,
        'corrector' : IFunctionIFunctionlistOffloat_from_listOffloat
    }
    
    
    
    
    
    
    
    
    
    
    def __repr__(self):
        return "MultiArmedBandit(%(strategies)s, %(account)s, %(weight)s, %(normalizer)s, %(corrector)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.account.bind_ex(self._ctx_ex)
        self.weight.bind_ex(self._ctx_ex)
        self.normalizer.bind_ex(self._ctx_ex)
        self.corrector.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
def MultiArmedBandit(strategies = None,account = None,weight = None,normalizer = None,corrector = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctionlistoffloat_from_listoffloat import IFunctionIFunctionlistOffloat_from_listOffloat
    from marketsim import rtti
    from marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy import IFunctionIAccount_from_ISingleAssetStrategy
    from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_ifunctionfloat import IFunctionIFunctionfloat_from_IFunctionfloat
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim import listOf
    from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount import IFunctionIFunctionfloat_from_IAccount
    if strategies is None or rtti.can_be_casted(strategies, listOf(ISingleAssetStrategy)):
        if account is None or rtti.can_be_casted(account, IFunctionIAccount_from_ISingleAssetStrategy):
            if weight is None or rtti.can_be_casted(weight, IFunctionIFunctionfloat_from_IAccount):
                if normalizer is None or rtti.can_be_casted(normalizer, IFunctionIFunctionfloat_from_IFunctionfloat):
                    if corrector is None or rtti.can_be_casted(corrector, IFunctionIFunctionlistOffloat_from_listOffloat):
                        return MultiArmedBandit_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloatFloatFloatListFloatListFloat(strategies,account,weight,normalizer,corrector)
    raise Exception('Cannot find suitable overload for MultiArmedBandit('+str(strategies) +':'+ str(type(strategies))+','+str(account) +':'+ str(type(account))+','+str(weight) +':'+ str(type(weight))+','+str(normalizer) +':'+ str(type(normalizer))+','+str(corrector) +':'+ str(type(corrector))+')')
