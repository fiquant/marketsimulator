from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionfloatiaccount import IFunctionIFunctionfloatIAccount
@registry.expose(["Strategy", "trader_Score"])
class trader_Score_(IFunctionIFunctionfloatIAccount):
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
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim.gen._out.strategy.weight._score import Score_IAccount as _strategy_weight_Score_IAccount
        trader = trader if trader is not None else _trader_SingleProxy_()
        
        return _strategy_weight_Score_IAccount(trader)
    
def trader_Score(): 
    from marketsim import rtti
    return trader_Score_()
    raise Exception('Cannot find suitable overload for trader_Score('++')')
