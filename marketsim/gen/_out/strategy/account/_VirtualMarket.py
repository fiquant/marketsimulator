from marketsim import registry
from marketsim.gen._intrinsic.strategy.account import _VirtualMarket_Impl
from marketsim import ISingleAssetStrategy
@registry.expose(["Strategy", "VirtualMarket"])
class VirtualMarket(_VirtualMarket_Impl):
    """   how it would be traded by sending request.evalMarketOrder
      (note: orders sent by a strategy wrapped into an adaptive strategy may not come to the market
      but we want evaluate in any case would it be profitable or not)
    """ 
    def __init__(self, inner = None):
        from marketsim.gen._out.strategy._Noise import Noise as _strategy_Noise
        from marketsim import rtti
        self.inner = inner if inner is not None else _strategy_Noise()
        rtti.check_fields(self)
        _VirtualMarket_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy
    }
    def __repr__(self):
        return "VirtualMarket(%(inner)s)" % self.__dict__
    
