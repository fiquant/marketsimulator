from marketsim import registry
import random
from marketsim import IObservable
from marketsim import IFunction
from marketsim.ops._function import Function
from marketsim import registry, types
import random


@registry.expose(['Random', 'Exponential distribution'])
class expovariate(Function[float]):
    """ 
      Returned values range from 0 to positive infinity
    """ 
    def __init__(self, Lambda = None):
        self.Lambda = Lambda if Lambda is not None else 1.0
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Lambda' : float
    }
    def __repr__(self):
        return "expovariate(Lambda = "+repr(self.Lambda)+" )" 
    
    def __call__(self, *args, **kwargs):
        return random.expovariate(self.Lambda)
    
    def _casts_to(self, dst):
        return expovariate._types[0]._casts_to(dst)
    
