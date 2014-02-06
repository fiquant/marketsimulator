from marketsim import registry
from marketsim import IFunction
from marketsim import float
from marketsim import IAccount
@registry.expose(["Strategy", "trader_Score"])
class trader_Score_(IFunction[IFunction[float], IAccount]):
    """  Returns difference between them.
    
     TODO: should be UpScore(timeframe, Efficiency(trader)) - DownScore(timeframe, Efficiency(trader))
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "trader_Score" % self.__dict__
    
    def __call__(self, trader = None):
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim.gen._out.strategy.weight._Score import Score
        trader = trader if trader is not None else _trader_SingleProxy()
        
        return Score(trader)
    
trader_Score = trader_Score_
