from marketsim import registry
from marketsim import IAccount
from marketsim import ISingleAssetStrategy
from marketsim import IFunction
@registry.expose(["Strategy", "inner_Real"])
class inner_Real_(IFunction[IAccount, ISingleAssetStrategy]):
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
        from marketsim.gen._out.strategy._noise import Noise_IEventSideIOrderGenerator as _strategy_Noise
        from marketsim.gen._out.strategy.account._real import Real_ISingleAssetStrategy as _strategy_account_Real
        inner = inner if inner is not None else _strategy_Noise()
        
        return _strategy_account_Real(inner)
    
def inner_Real(): 
    from marketsim import rtti
    return inner_Real_()
    raise Exception('Cannot find suitable overload for inner_Real('++')')
