from marketsim import registry
from marketsim.gen._intrinsic.strategy.account import _VirtualMarket_Impl
from marketsim import ISingleAssetStrategy
@registry.expose(["Strategy", "VirtualMarket"])
class VirtualMarket(_VirtualMarket_Impl):
    """ 
    """ 
    def __init__(self, inner = None):
        from marketsim.gen._out.strategy._Noise import Noise as _strategy_Noise
        self.inner = inner if inner is not None else _strategy_Noise()
        _VirtualMarket_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy
    }
    def __repr__(self):
        return "VirtualMarket(%(inner)s)" % self.__dict__
    
