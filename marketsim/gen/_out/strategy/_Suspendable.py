from marketsim.gen._intrinsic.strategy.suspendable import _Suspendable_Impl
from marketsim import IFunction
from marketsim import ISingleAssetStrategy
from marketsim import registry
from marketsim import bool
@registry.expose(["Strategy", "Suspendable"])
class Suspendable_ISingleAssetStrategyIFunctionBoolean(_Suspendable_Impl):
    """ 
    """ 
    def __init__(self, inner = None, predicate = None):
        from marketsim.gen._out.strategy._noise import Noise as _strategy_Noise
        from marketsim.gen._out._true import true as _true
        from marketsim import rtti
        self.inner = inner if inner is not None else _strategy_Noise()
        self.predicate = predicate if predicate is not None else _true()
        rtti.check_fields(self)
        _Suspendable_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy,
        'predicate' : IFunction[bool]
    }
    def __repr__(self):
        return "Suspendable(%(inner)s, %(predicate)s)" % self.__dict__
    
def Suspendable(inner = None,predicate = None): 
    from marketsim import ISingleAssetStrategy
    from marketsim import IFunction
    from marketsim import bool
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ISingleAssetStrategy):
        if predicate is None or rtti.can_be_casted(predicate, IFunction[bool]):
            return Suspendable_ISingleAssetStrategyIFunctionBoolean(inner,predicate)
    raise Exception("Cannot find suitable overload")
