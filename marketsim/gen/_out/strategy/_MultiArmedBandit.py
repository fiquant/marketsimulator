from marketsim import IFunction
from marketsim.gen._intrinsic.strategy.multiarmed_bandit import _MultiarmedBandit2_Impl
from marketsim import IAccount
from marketsim import ISingleAssetStrategy
from marketsim import listOf
from marketsim import registry
from marketsim import float
@registry.expose(["Strategy", "MultiArmedBandit"])
class MultiArmedBandit_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountIFunctionFloatIFunctionFloatIFunctionFloatListFloatListFloat(_MultiarmedBandit2_Impl):
    """  In some moments of time the efficiency of the strategies is evaluated
     These efficiencies are mapped into weights using *weight* and *normilizer*
     functions per every strategy and *corrector* for the whole collection of weights
     These weights are used to choose randomly a strategy to run for the next quant of time.
     All other strategies are suspended
    """ 
    def __init__(self, strategies = None, account = None, weight = None, normalizer = None, corrector = None):
        from marketsim.gen._out.strategy.account.inner._inner_virtualmarket import inner_VirtualMarket_ as _strategy_account_inner_inner_VirtualMarket
        from marketsim import rtti
        from marketsim.gen._out.strategy.weight.array._array_identityl import array_IdentityL_ as _strategy_weight_array_array_IdentityL
        from marketsim.gen._out.strategy.weight.trader._trader_efficiencytrend import trader_EfficiencyTrend_Float as _strategy_weight_trader_trader_EfficiencyTrend
        from marketsim.gen._out.strategy._noise import Noise_IEventSideIOrderGenerator as _strategy_Noise
        from marketsim.gen._out.strategy.weight.f._f_atanpow import f_AtanPow_Float as _strategy_weight_f_f_AtanPow
        self.strategies = strategies if strategies is not None else [_strategy_Noise()]
        self.account = account if account is not None else _strategy_account_inner_inner_VirtualMarket()
        self.weight = weight if weight is not None else _strategy_weight_trader_trader_EfficiencyTrend()
        self.normalizer = normalizer if normalizer is not None else _strategy_weight_f_f_AtanPow()
        self.corrector = corrector if corrector is not None else _strategy_weight_array_array_IdentityL()
        rtti.check_fields(self)
        _MultiarmedBandit2_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'strategies' : listOf(ISingleAssetStrategy),
        'account' : IFunction[IAccount,ISingleAssetStrategy],
        'weight' : IFunction[IFunction[float],IAccount],
        'normalizer' : IFunction[IFunction[float],IFunction[float]],
        'corrector' : IFunction[listOf(float),listOf(float)]
    }
    def __repr__(self):
        return "MultiArmedBandit(%(strategies)s, %(account)s, %(weight)s, %(normalizer)s, %(corrector)s)" % self.__dict__
    
def MultiArmedBandit(strategies = None,account = None,weight = None,normalizer = None,corrector = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import listOf
    from marketsim import ISingleAssetStrategy
    from marketsim import IAccount
    if strategies is None or rtti.can_be_casted(strategies, listOf(ISingleAssetStrategy)):
        if account is None or rtti.can_be_casted(account, IFunction[IAccount,ISingleAssetStrategy]):
            if weight is None or rtti.can_be_casted(weight, IFunction[IFunction[float],IAccount]):
                if normalizer is None or rtti.can_be_casted(normalizer, IFunction[IFunction[float],IFunction[float]]):
                    if corrector is None or rtti.can_be_casted(corrector, IFunction[listOf(float),listOf(float)]):
                        return MultiArmedBandit_ListISingleAssetStrategyISingleAssetStrategyIAccountIAccountIFunctionFloatIFunctionFloatIFunctionFloatListFloatListFloat(strategies,account,weight,normalizer,corrector)
    raise Exception('Cannot find suitable overload for MultiArmedBandit('+str(strategies)+','+str(account)+','+str(weight)+','+str(normalizer)+','+str(corrector)+')')
