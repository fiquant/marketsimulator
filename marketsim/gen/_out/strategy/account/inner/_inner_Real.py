from marketsim import registry
from marketsim.gen._out._ifunction._ifunctioniaccount_from_isingleassetstrategy import IFunctionIAccount_from_ISingleAssetStrategy
@registry.expose(["Strategy", "inner_Real"])
class inner_Real_(IFunctionIAccount_from_ISingleAssetStrategy):
    """   how orders sent by the strategy have been actually traded
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
        return "inner_Real" % self.__dict__
    
    def __call__(self, inner = None):
        from marketsim.gen._out.strategy._noise import Noise_IEventSideIObservableIOrder as _strategy_Noise_IEventSideIObservableIOrder
        from marketsim import deref_opt
        from marketsim.gen._out.strategy.account._real import Real_ISingleAssetStrategy as _strategy_account_Real_ISingleAssetStrategy
        inner = inner if inner is not None else deref_opt(_strategy_Noise_IEventSideIObservableIOrder())
        
        return _strategy_account_Real_ISingleAssetStrategy(inner)
    
def inner_Real(): 
    from marketsim import rtti
    return inner_Real_()
    raise Exception('Cannot find suitable overload for inner_Real('++')')
