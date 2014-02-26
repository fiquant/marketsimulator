from marketsim.gen._out._ifunction._ifunctioniaccountisingleassetstrategy import IFunctionIAccountISingleAssetStrategy
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import listOf
from marketsim import registry
from marketsim.gen._intrinsic.strategy.choose_the_best import _ChooseTheBest_Impl
from marketsim.gen._out._ifunction._ifunctionifunctionfloatiaccount import IFunctionIFunctionfloatIAccount
@registry.expose(["Strategy", "ChooseTheBest"])
class ChooseTheBest_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat(ISingleAssetStrategy,_ChooseTheBest_Impl):
    """  In some moments of time the most effective strategy
     is chosen and made running; other strategies are suspended.
     It can be considered as a particular case for MultiArmedBandit strategy with
     *corrector* parameter set to *chooseTheBest*
    """ 
    def __init__(self, strategies = None, account = None, performance = None):
        from marketsim.gen._out.strategy._noise import Noise_IEventSideIObservableIOrder as _strategy_Noise_IEventSideIObservableIOrder
        from marketsim.gen._out.strategy.account.inner._inner_virtualmarket import inner_VirtualMarket_ as _strategy_account_inner_inner_VirtualMarket_
        from marketsim.gen._out.strategy.weight.trader._trader_traderefficiencytrend import trader_TraderEfficiencyTrend_Float as _strategy_weight_trader_trader_TraderEfficiencyTrend_Float
        from marketsim import rtti
        self.strategies = strategies if strategies is not None else [_strategy_Noise_IEventSideIObservableIOrder()]
        self.account = account if account is not None else _strategy_account_inner_inner_VirtualMarket_()
        self.performance = performance if performance is not None else _strategy_weight_trader_trader_TraderEfficiencyTrend_Float()
        rtti.check_fields(self)
        _ChooseTheBest_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'strategies' : listOf(ISingleAssetStrategy),
        'account' : IFunctionIAccountISingleAssetStrategy,
        'performance' : IFunctionIFunctionfloatIAccount
    }
    def __repr__(self):
        return "ChooseTheBest(%(strategies)s, %(account)s, %(performance)s)" % self.__dict__
    
def ChooseTheBest(strategies = None,account = None,performance = None): 
    from marketsim.gen._out._ifunction._ifunctioniaccountisingleassetstrategy import IFunctionIAccountISingleAssetStrategy
    from marketsim import rtti
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim.gen._out._ifunction._ifunctionifunctionfloatiaccount import IFunctionIFunctionfloatIAccount
    from marketsim import listOf
    if strategies is None or rtti.can_be_casted(strategies, listOf(ISingleAssetStrategy)):
        if account is None or rtti.can_be_casted(account, IFunctionIAccountISingleAssetStrategy):
            if performance is None or rtti.can_be_casted(performance, IFunctionIFunctionfloatIAccount):
                return ChooseTheBest_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountFloat(strategies,account,performance)
    raise Exception('Cannot find suitable overload for ChooseTheBest('+str(strategies) +':'+ str(type(strategies))+','+str(account) +':'+ str(type(account))+','+str(performance) +':'+ str(type(performance))+')')
