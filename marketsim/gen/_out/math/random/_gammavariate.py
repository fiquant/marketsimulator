from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
@registry.expose(["Random", "gammavariate"])
class gammavariate_FloatFloat(Function[float]):
    """ 
      Conditions on the parameters are |alpha| > 0 and |beta| > 0.
    
      The probability distribution function is: ::
    
                   x ** (alpha - 1) * math.exp(-x / beta)
         pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha
    """ 
    def __init__(self, Alpha = None, Beta = None):
        from marketsim import rtti
        self.Alpha = Alpha if Alpha is not None else 1.0
        self.Beta = Beta if Beta is not None else 1.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Alpha' : float,
        'Beta' : float
    }
    def __repr__(self):
        return "gammavariate(%(Alpha)s, %(Beta)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        import random
        return random.gammavariate(self.Alpha, self.Beta)
    
    def _casts_to(self, dst):
        return gammavariate_FloatFloat._types[0]._casts_to(dst)
    
def gammavariate(Alpha = None,Beta = None): 
    from marketsim import float
    from marketsim import rtti
    if Alpha is None or rtti.can_be_casted(Alpha, float):
        if Beta is None or rtti.can_be_casted(Beta, float):
            return gammavariate_FloatFloat(Alpha,Beta)
    raise Exception('Cannot find suitable overload for gammavariate('+str(Alpha)+','+str(Beta)+')')
