from marketsim import registry
from marketsim.gen._intrinsic.strategy.combine import _Combine_Impl
from marketsim import ISingleAssetStrategy
from marketsim import ISingleAssetStrategy
@registry.expose(["Strategy", "Combine"])
class Combine(_Combine_Impl):
    """ 
    """ 
    def __init__(self, A = None, B = None):
        from marketsim.gen._out.strategy._Noise import Noise as _strategy_Noise
        from marketsim.gen._out.strategy._Noise import Noise as _strategy_Noise
        from marketsim import rtti
        self.A = A if A is not None else _strategy_Noise()
        self.B = B if B is not None else _strategy_Noise()
        rtti.check_fields(self)
        _Combine_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'A' : ISingleAssetStrategy,
        'B' : ISingleAssetStrategy
    }
    def __repr__(self):
        return "Combine(%(A)s, %(B)s)" % self.__dict__
    
