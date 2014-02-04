from marketsim import registry
from marketsim.gen._intrinsic.strategy.canceller import _Canceller_Impl
from marketsim import float
from marketsim import IFunction
@registry.expose(["Strategy", "Canceller"])
class Canceller_Optional________Float_(_Canceller_Impl):
    """   and in some moments of time it randomly chooses an order and cancels it
      Note: a similar effect can be obtained using order.WithExpiry meta orders
    """ 
    def __init__(self, cancellationIntervalDistr = None):
        from marketsim.gen._out.math.random._expovariate import expovariate as _math_random_expovariate
        from marketsim import rtti
        self.cancellationIntervalDistr = cancellationIntervalDistr if cancellationIntervalDistr is not None else _math_random_expovariate(1.0)
        rtti.check_fields(self)
        _Canceller_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cancellationIntervalDistr' : IFunction[float]
    }
    def __repr__(self):
        return "Canceller(%(cancellationIntervalDistr)s)" % self.__dict__
    
Canceller = Canceller_Optional________Float_
