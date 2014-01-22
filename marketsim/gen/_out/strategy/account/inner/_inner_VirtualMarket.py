from marketsim import registry
from marketsim import IAccount
from marketsim import ISingleAssetStrategy
from marketsim import IFunction
@registry.expose(["Strategy", "inner_VirtualMarket"])
class inner_VirtualMarket(IFunction[IAccount, ISingleAssetStrategy]):
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
        return "inner_VirtualMarket" % self.__dict__
    
    def __call__(self, inner = None):
        from marketsim.gen._out.strategy._Noise import Noise as _strategy_Noise
        from marketsim.gen._out.strategy.account._VirtualMarket import VirtualMarket
        inner = inner if inner is not None else _strategy_Noise()
        
        return VirtualMarket(inner)
    
