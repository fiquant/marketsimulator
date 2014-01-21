from marketsim import registry
from marketsim.gen._intrinsic.strategy.multiarmed_bandit import _MultiarmedBandit2_Impl
from marketsim import listOf
from marketsim import ISingleAssetStrategy
from marketsim import IFunction
from marketsim import IAccount
from marketsim import ISingleAssetStrategy
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IAccount
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
from marketsim import listOf
from marketsim import listOf
@registry.expose(["Strategy", "MultiArmedBandit"])
class MultiArmedBandit(_MultiarmedBandit2_Impl):
    """  In some moments of time the most effective strategy
     is chosen and made running; other strategies are suspended.
     The choice is made randomly among the strategies that have
     a positive efficiency trend, weighted by the efficiency value.
    """ 
    def __init__(self, strategies = None, account = None, weight = None, normalizer = None, corrector = None):
        from marketsim.gen._out.strategy._Noise import Noise as _strategy_Noise
        from marketsim.gen._out.strategy.account.inner._inner_VirtualMarket import inner_VirtualMarket as _strategy_account_inner_inner_VirtualMarket
        from marketsim.gen._out.strategy.weight.trader._trader_EfficiencyTrend import trader_EfficiencyTrend as _strategy_weight_trader_trader_EfficiencyTrend
        from marketsim.gen._out.strategy.weight.f._f_AtanPow import f_AtanPow as _strategy_weight_f_f_AtanPow
        from marketsim.gen._out.strategy.weight.array._array_IdentityL import array_IdentityL as _strategy_weight_array_array_IdentityL
        self.strategies = strategies if strategies is not None else [_strategy_Noise()]
        self.account = account if account is not None else _strategy_account_inner_inner_VirtualMarket()
        self.weight = weight if weight is not None else _strategy_weight_trader_trader_EfficiencyTrend()
        self.normalizer = normalizer if normalizer is not None else _strategy_weight_f_f_AtanPow()
        self.corrector = corrector if corrector is not None else _strategy_weight_array_array_IdentityL()
        _MultiarmedBandit2_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'strategies' : listOf(ISingleAssetStrategy)
        ,
        'account' : IFunction[IAccount,ISingleAssetStrategy]
        
        ,
        'weight' : IFunction[IFunction[float],IAccount]
        
        ,
        'normalizer' : IFunction[IFunction[float],IFunction[float]]
        
        ,
        'corrector' : IFunction[listOf(float),listOf(float)]
        
        
    }
    def __repr__(self):
        return "MultiArmedBandit(%(strategies)s, %(account)s, %(weight)s, %(normalizer)s, %(corrector)s)" % self.__dict__
    
