from marketsim import registry
from marketsim import IAccount
from marketsim import ISingleAssetStrategy
from marketsim import IFunction
@registry.expose(["Strategy", "inner_VirtualMarket"])
class inner_VirtualMarket_(IFunction[IAccount,ISingleAssetStrategy]):
    """   how it would be traded by sending request.evalMarketOrder
      (note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market
      but we want evaluate in any case would it be profitable or not)
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
        return "inner_VirtualMarket" % self.__dict__
    
    def __call__(self, inner = None):
        from marketsim.gen._out.strategy._noise import Noise_IEventSideIOrderGenerator as _strategy_Noise_IEventSideIOrderGenerator
        from marketsim.gen._out.strategy.account._virtualmarket import VirtualMarket_ISingleAssetStrategy as _strategy_account_VirtualMarket_ISingleAssetStrategy
        inner = inner if inner is not None else _strategy_Noise_IEventSideIOrderGenerator()
        
        return _strategy_account_VirtualMarket_ISingleAssetStrategy(inner)
    
def inner_VirtualMarket(): 
    from marketsim import rtti
    return inner_VirtualMarket_()
    raise Exception('Cannot find suitable overload for inner_VirtualMarket('++')')
