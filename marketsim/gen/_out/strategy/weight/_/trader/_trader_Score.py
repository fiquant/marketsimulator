from marketsim import registry
from marketsim import IFunction
from marketsim import IAccount
from marketsim import IFunction
@registry.expose(["Strategy", "trader_Score"])
class trader_Score(IFunction[IFunction[float], IAccount]):
    """ 
    """ 
    def __init__(self):
        pass
    
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
    
