from marketsim import registry
from marketsim.gen._intrinsic.strategy.choose_the_best import _ChooseTheBest_Impl
from marketsim import listOf
from marketsim import ISingleAssetStrategy
from marketsim import IFunction
from marketsim import IAccount
from marketsim import ISingleAssetStrategy
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IAccount
@registry.expose(["Strategy", "ChooseTheBest"])
class ChooseTheBest(_ChooseTheBest_Impl):"""  In some moments of time the most effective strategy
     is chosen and made running; other strategies are suspended.
     It can be considered as a particular case for MultiArmedBandit strategy with
     *corrector* parameter set to *chooseTheBest*
    """ 
    def __init__(self, strategies = None, account = None, performance = None):from marketsim.gen._out.strategy._Noise import Noise as _strategy_Noise
        from marketsim.gen._out.strategy.account.inner._inner_VirtualMarket import inner_VirtualMarket as _strategy_account_inner_inner_VirtualMarket
        from marketsim.gen._out.strategy.weight.trader._trader_EfficiencyTrend import trader_EfficiencyTrend as _strategy_weight_trader_trader_EfficiencyTrend
        from marketsim import rtti
        self.strategies = strategies if strategies is not None else [_strategy_Noise()]
        self.account = account if account is not None else _strategy_account_inner_inner_VirtualMarket()
        self.performance = performance if performance is not None else _strategy_weight_trader_trader_EfficiencyTrend()
        rtti.check_fields(self)
        _ChooseTheBest_Impl.__init__(self)
    
    @property
    def label(self):return repr(self)
    
    _properties = {'strategies' : listOf(ISingleAssetStrategy)
        ,
        'account' : IFunction[IAccount,ISingleAssetStrategy]
        
        ,
        'performance' : IFunction[IFunction[float],IAccount]
        
        
    }
    def __repr__(self):return "ChooseTheBest(%(strategies)s, %(account)s, %(performance)s)" % self.__dict__
    
