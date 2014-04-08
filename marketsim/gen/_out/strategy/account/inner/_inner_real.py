from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy import IFunctionIAccount_from_ISingleAssetStrategy
@registry.expose(["Strategy", "inner_Real"])
class inner_Real_(IFunctionIAccount_from_ISingleAssetStrategy):
    """ Associated with a strategy account that tracks
    
      how orders sent by the strategy have been actually traded
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
        return "inner_Real" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def __call__(self, inner = None):
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim import deref_opt
        from marketsim.gen._out.strategy.account._real import Real_ISingleAssetStrategy as _strategy_account_Real_ISingleAssetStrategy
        inner = inner if inner is not None else deref_opt(_strategy_Empty_())
        
        return _strategy_account_Real_ISingleAssetStrategy(inner)
    
def inner_Real(): 
    from marketsim import rtti
    return inner_Real_()
    raise Exception('Cannot find suitable overload for inner_Real('++')')
