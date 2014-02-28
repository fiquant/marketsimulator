from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._intrinsic.strategy.suspendable import _Suspendable_Impl
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
@registry.expose(["Strategy", "Suspendable"])
class Suspendable_ISingleAssetStrategyBoolean(ISingleAssetStrategy,_Suspendable_Impl):
    """ 
    """ 
    def __init__(self, inner = None, predicate = None):
        from marketsim.gen._out.strategy._noise import Noise_IEventSideIObservableIOrder as _strategy_Noise_IEventSideIObservableIOrder
        from marketsim import deref_opt
        from marketsim.gen._out._true import true_ as _true_
        from marketsim import rtti
        self.inner = inner if inner is not None else deref_opt(_strategy_Noise_IEventSideIObservableIOrder())
        self.predicate = predicate if predicate is not None else deref_opt(_true_())
        rtti.check_fields(self)
        _Suspendable_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'inner' : ISingleAssetStrategy,
        'predicate' : IFunctionbool
    }
    def __repr__(self):
        return "Suspendable(%(inner)s, %(predicate)s)" % self.__dict__
    
def Suspendable(inner = None,predicate = None): 
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
    from marketsim import rtti
    if inner is None or rtti.can_be_casted(inner, ISingleAssetStrategy):
        if predicate is None or rtti.can_be_casted(predicate, IFunctionbool):
            return Suspendable_ISingleAssetStrategyBoolean(inner,predicate)
    raise Exception('Cannot find suitable overload for Suspendable('+str(inner) +':'+ str(type(inner))+','+str(predicate) +':'+ str(type(predicate))+')')
