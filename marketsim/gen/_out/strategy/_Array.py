from marketsim import registry
from marketsim.gen._intrinsic.strategy.combine import _Array_Impl
from marketsim import listOf
from marketsim import ISingleAssetStrategy
@registry.expose(["Strategy", "Array"])
class Array(_Array_Impl):
    """ 
    """ 
    def __init__(self, strategies = None):
        from marketsim.gen._out.strategy._Noise import Noise as _strategy_Noise
        from marketsim import rtti
        self.strategies = strategies if strategies is not None else [_strategy_Noise()]
        rtti.check_fields(self)
        _Array_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'strategies' : listOf(ISingleAssetStrategy)
        
    }
    def __repr__(self):
        return "Array(%(strategies)s)" % self.__dict__
    
