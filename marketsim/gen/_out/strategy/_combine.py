from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._intrinsic.strategy.combine import Combine_Impl
@registry.expose(["Strategy", "Combine"])
class Combine_ISingleAssetStrategyISingleAssetStrategy(ISingleAssetStrategy,Combine_Impl):
    """   Can be considered as a particular case of Array strategy
    """ 
    def __init__(self, A = None, B = None):
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim import deref_opt
        from marketsim import rtti
        self.A = A if A is not None else deref_opt(_strategy_Empty_())
        self.B = B if B is not None else deref_opt(_strategy_Empty_())
        rtti.check_fields(self)
        Combine_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'A' : ISingleAssetStrategy,
        'B' : ISingleAssetStrategy
    }
    
    
    
    
    def __repr__(self):
        return "Combine(%(A)s, %(B)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
def Combine(A = None,B = None): 
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim import rtti
    if A is None or rtti.can_be_casted(A, ISingleAssetStrategy):
        if B is None or rtti.can_be_casted(B, ISingleAssetStrategy):
            return Combine_ISingleAssetStrategyISingleAssetStrategy(A,B)
    raise Exception('Cannot find suitable overload for Combine('+str(A) +':'+ str(type(A))+','+str(B) +':'+ str(type(B))+')')
