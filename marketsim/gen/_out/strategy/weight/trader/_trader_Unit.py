from marketsim import registry
from marketsim import IFunction
from marketsim import float
from marketsim import IAccount
@registry.expose(["Strategy", "trader_Unit"])
class trader_Unit_(IFunction[IFunction[float], IAccount]):
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
        return "trader_Unit" % self.__dict__
    
    def __call__(self, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy as _trader_SingleProxy
        from marketsim.gen._out.strategy.weight._unit import Unit
        trader = trader if trader is not None else _trader_SingleProxy()
        
        return Unit(trader)
    
def trader_Unit(): 
    from marketsim import rtti
    return trader_Unit_()
    raise Exception("Cannot find suitable overload")
