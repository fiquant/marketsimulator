from marketsim import registry
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._intrinsic.strategy.canceller import Canceller_Impl
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Strategy", "Canceller"])
class Canceller_Float(ISingleAssetStrategy,Canceller_Impl):
    """   and in some moments of time it randomly chooses an order and cancels it
      Note: a similar effect can be obtained using order.WithExpiry meta orders
    """ 
    def __init__(self, cancellationIntervalDistr = None):
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.cancellationIntervalDistr = cancellationIntervalDistr if cancellationIntervalDistr is not None else deref_opt(_math_random_expovariate_Float(1.0))
        rtti.check_fields(self)
        Canceller_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cancellationIntervalDistr' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "Canceller(%(cancellationIntervalDistr)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
def Canceller(cancellationIntervalDistr = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if cancellationIntervalDistr is None or rtti.can_be_casted(cancellationIntervalDistr, IFunctionfloat):
        return Canceller_Float(cancellationIntervalDistr)
    raise Exception('Cannot find suitable overload for Canceller('+str(cancellationIntervalDistr) +':'+ str(type(cancellationIntervalDistr))+')')
