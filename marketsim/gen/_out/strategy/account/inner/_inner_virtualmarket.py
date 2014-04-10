from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy import IFunctionIAccount_from_ISingleAssetStrategy
@registry.expose(["Strategy", "inner_VirtualMarket"])
class inner_VirtualMarket_(IFunctionIAccount_from_ISingleAssetStrategy):
    """ **Associated with a strategy account that evaluates for every order sent by the strategy**
    
      how it would be traded by sending request.evalMarketOrder
      (note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market
      but we want evaluate in any case would it be profitable or not)
    
    Parameters are:
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
        return "inner_VirtualMarket" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        
        delattr(self, '_processing_ex')
    
    def __call__(self, inner = None):
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim import deref_opt
        from marketsim.gen._out.strategy.account._virtualmarket import VirtualMarket_ISingleAssetStrategy as _strategy_account_VirtualMarket_ISingleAssetStrategy
        inner = inner if inner is not None else deref_opt(_strategy_Empty_())
        
        return _strategy_account_VirtualMarket_ISingleAssetStrategy(inner)
    
def inner_VirtualMarket(): 
    from marketsim import rtti
    return inner_VirtualMarket_()
    raise Exception('Cannot find suitable overload for inner_VirtualMarket('++')')
