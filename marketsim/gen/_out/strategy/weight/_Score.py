def score(): 
    from marketsim.gen._out.strategy.weight.trader._trader_score import trader_Score_ as _strategy_weight_trader_trader_Score_
    from marketsim import rtti
    return _strategy_weight_trader_trader_Score_()
    raise Exception('Cannot find suitable overload for score('++')')
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._intrinsic.strategy.weight import Score_Impl
from marketsim.gen._out._iaccount import IAccount
@registry.expose(["Strategy", "Score"])
class Score_IAccount(IFunctionfloat,Score_Impl):
    """  Returns difference between them.
    
     TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))
    """ 
    def __init__(self, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim import deref_opt
        from marketsim import rtti
        self.trader = trader if trader is not None else deref_opt(_trader_SingleProxy_())
        rtti.check_fields(self)
        Score_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    def __repr__(self):
        return "Score(%(trader)s)" % self.__dict__
    
def Score(trader = None): 
    from marketsim.gen._out._iaccount import IAccount
    from marketsim import rtti
    if trader is None or rtti.can_be_casted(trader, IAccount):
        return Score_IAccount(trader)
    raise Exception('Cannot find suitable overload for Score('+str(trader) +':'+ str(type(trader))+')')
