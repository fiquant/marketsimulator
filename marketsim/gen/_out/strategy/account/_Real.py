from marketsim import registry
from marketsim.gen._intrinsic.strategy.account import _Account_Impl
from marketsim import ISingleAssetStrategy
@registry.expose(["Strategy", "Real"])
class Real_Optional__ISingleAssetStrategy_(_Account_Impl):
    """   how orders sent by the strategy have been actually traded
    """ 
    def __init__(self, inner = None):
        from marketsim.gen._out.strategy._Noise import Noise as _strategy_Noise
        from marketsim import rtti
        self.inner = inner if inner is not None else _strategy_Noise()
        rtti.check_fields(self)
        _Account_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy
    }
    def __repr__(self):
        return "Real(%(inner)s)" % self.__dict__
    
def Real(inner = None): 
    from marketsim import ISingleAssetStrategy
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ISingleAssetStrategy):
        return Real_Optional__ISingleAssetStrategy_(inner)
    raise Exception("Cannot find suitable overload")
