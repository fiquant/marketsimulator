from marketsim import registry
from marketsim import IFunction
from marketsim import float
from marketsim import IAccount
@registry.expose(["Strategy", "trader_Efficiency"])
class trader_Efficiency_(IFunction[IFunction[float],IAccount]):
    """ 
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
        return "trader_Efficiency" % self.__dict__
    
    def __call__(self, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim.gen._out.strategy.weight._efficiency import Efficiency_IAccount as _strategy_weight_Efficiency_IAccount
        trader = trader if trader is not None else _trader_SingleProxy_()
        
        return _strategy_weight_Efficiency_IAccount(trader)
    
def trader_Efficiency(): 
    from marketsim import rtti
    return trader_Efficiency_()
    raise Exception('Cannot find suitable overload for trader_Efficiency('++')')
