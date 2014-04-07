from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionifunctionfloat_from_iaccount import IFunctionIFunctionfloat_from_IAccount
@registry.expose(["Strategy", "trader_Unit"])
class trader_Unit_(IFunctionIFunctionfloat_from_IAccount):
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
        return "trader_Unit" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def __call__(self, trader = None):
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy_
        from marketsim import deref_opt
        from marketsim.gen._out.strategy.weight._unit import Unit_IAccount as _strategy_weight_Unit_IAccount
        trader = trader if trader is not None else deref_opt(_trader_SingleProxy_())
        
        return _strategy_weight_Unit_IAccount(trader)
    
def trader_Unit(): 
    from marketsim import rtti
    return trader_Unit_()
    raise Exception('Cannot find suitable overload for trader_Unit('++')')
