
from marketsim import registry, types, ops
import random
            
@registry.expose(['Random', 'Gamma distribution'])
class gammavariate(ops.Function[float]):
    """ 
      Conditions on the parameters are |alpha| > 0 and |beta| > 0.
    
      The probability distribution function is: ::
    
                   x ** (alpha - 1) * math.exp(-x / beta)
         pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha
    """ 
    def __init__(self, Alpha = Some(1.0), Beta = Some(1.0)):
        self.Alpha = Alpha
        self.Beta = Beta

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Alpha' : float,
        'Beta' : float
    }

    def __repr__(self):
        return "gammavariate(Alpha = "+repr(self.Alpha)+" , Beta = "+repr(self.Beta)+" )" 

    def __call__(self, *args, **kwargs):
        return random.gammavariate(self.Alpha, self.Beta)

    def _casts_to(self, dst):
        return gammavariate._types[0]._casts_to(dst)
