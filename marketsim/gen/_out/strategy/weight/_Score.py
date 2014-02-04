from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.strategy.weight import _Score_Impl
from marketsim import IAccount
@registry.expose(["Strategy", "Score"])
class Score__IAccount(Function[float], _Score_Impl):
    """  Returns difference between them.
    
     TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))
    """ 
    def __init__(self, trader = None):
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim import rtti
        self.trader = trader if trader is not None else _trader_SingleProxy()
        rtti.check_fields(self)
        _Score_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    def __repr__(self):
        return "Score(%(trader)s)" % self.__dict__
    
Score = Score__IAccount
