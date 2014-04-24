# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount import IFunctionIFunctionfloat_from_IAccount
from marketsim import listOf
from marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy import IFunctionIAccount_from_ISingleAssetStrategy
from marketsim.gen._intrinsic.strategy.choose_the_best import ChooseTheBest_Impl
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
@registry.expose(["Strategy", "ChooseTheBest"])
class ChooseTheBest_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat(ISingleAssetStrategy,ChooseTheBest_Impl):
    """ **A composite strategy initialized with an array of strategies.**
    
     In some moments of time the most effective strategy
     is chosen and made running; other strategies are suspended.
     It can be considered as a particular case for MultiArmedBandit strategy with
     *corrector* parameter set to *chooseTheBest*
    
    Parameters are:
    
    **strategies**
    	 original strategies that can be suspended 
    
    **account**
    	 function creating phantom strategy used for efficiency estimation 
    
    **performance**
    	 function estimating is the strategy efficient or not 
    """ 
    def __init__(self, strategies = None, account = None, performance = None):
        from marketsim.gen._out.strategy.account.inner._inner_virtualmarket import inner_VirtualMarket_ as _strategy_account_inner_inner_VirtualMarket_
        from marketsim import rtti
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim.gen._out.strategy.weight.trader._trader_traderefficiencytrend import trader_TraderEfficiencyTrend_Float as _strategy_weight_trader_trader_TraderEfficiencyTrend_Float
        from marketsim import deref_opt
        self.strategies = strategies if strategies is not None else [deref_opt(_strategy_Empty_())]
        self.account = account if account is not None else deref_opt(_strategy_account_inner_inner_VirtualMarket_())
        self.performance = performance if performance is not None else deref_opt(_strategy_weight_trader_trader_TraderEfficiencyTrend_Float())
        rtti.check_fields(self)
        ChooseTheBest_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'strategies' : listOf(ISingleAssetStrategy),
        'account' : IFunctionIAccount_from_ISingleAssetStrategy,
        'performance' : IFunctionIFunctionfloat_from_IAccount
    }
    
    
    
    
    
    
    def __repr__(self):
        return "ChooseTheBest(%(strategies)s, %(account)s, %(performance)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self._ctx_ex)
                else:
                    v.bind_ex(self._ctx_ex)
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        for x in self.strategies: x.bind_ex(self._ctx_ex)
        self.account.bind_ex(self._ctx_ex)
        self.performance.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def ChooseTheBest(strategies = None,account = None,performance = None): 
    from marketsim import rtti
    from marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy import IFunctionIAccount_from_ISingleAssetStrategy
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim import listOf
    from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount import IFunctionIFunctionfloat_from_IAccount
    if strategies is None or rtti.can_be_casted(strategies, listOf(ISingleAssetStrategy)):
        if account is None or rtti.can_be_casted(account, IFunctionIAccount_from_ISingleAssetStrategy):
            if performance is None or rtti.can_be_casted(performance, IFunctionIFunctionfloat_from_IAccount):
                return ChooseTheBest_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat(strategies,account,performance)
    raise Exception('Cannot find suitable overload for ChooseTheBest('+str(strategies) +':'+ str(type(strategies))+','+str(account) +':'+ str(type(account))+','+str(performance) +':'+ str(type(performance))+')')
