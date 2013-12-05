from marketsim import registry
from marketsim import float
from marketsim import float
import random
from marketsim import IObservable
from marketsim import IFunction
from marketsim.ops._function import Function
from marketsim import registry, types
import random


@registry.expose(['Random', 'Gamma distribution'])
class gammavariate(Function[float]):
    """ 
      Conditions on the parameters are |alpha| > 0 and |beta| > 0.
    
      The probability distribution function is: ::
    
                   x ** (alpha - 1) * math.exp(-x / beta)
         pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha
    """ 
    def __init__(self, Alpha = None, Beta = None):
        self.Alpha = Alpha if Alpha is not None else 1.0
        self.Beta = Beta if Beta is not None else 1.0
    
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
    
