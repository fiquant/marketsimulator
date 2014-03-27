from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount import IFunctionIFunctionfloat_from_IAccount
from marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy import IFunctionIAccount_from_ISingleAssetStrategy
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._intrinsic.strategy.choose_the_best import ChooseTheBest_Impl
from marketsim import listOf
from marketsim import registry
@registry.expose(["Strategy", "ChooseTheBest"])
class ChooseTheBest_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat(ISingleAssetStrategy,ChooseTheBest_Impl):
    """  In some moments of time the most effective strategy
     is chosen and made running; other strategies are suspended.
     It can be considered as a particular case for MultiArmedBandit strategy with
     *corrector* parameter set to *chooseTheBest*
    """ 
    def __init__(self, strategies = None, account = None, performance = None):
        from marketsim import deref_opt
        from marketsim import rtti
        from marketsim.gen._out.strategy.weight.trader._trader_traderefficiencytrend import trader_TraderEfficiencyTrend_Float as _strategy_weight_trader_trader_TraderEfficiencyTrend_Float
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim.gen._out.strategy.account.inner._inner_virtualmarket import inner_VirtualMarket_ as _strategy_account_inner_inner_VirtualMarket_
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
        return "ChooseTheBest(%(strategies)s, %(account)s, %(performance)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
