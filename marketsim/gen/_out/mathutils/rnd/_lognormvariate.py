from marketsim import registry
from marketsim import IObservable
from marketsim import IFunction
from marketsim.ops._function import Function
from marketsim import float
from marketsim import float
from marketsim import registry, types
import random


@registry.expose(['Random', 'Log normal distribution'])
class lognormvariate(Function[float]):
    """ 
     If you take the natural logarithm of this distribution,
      you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
      |mu| can have any value, and |sigma| must be greater than zero.
    """ 
    def __init__(self, Mu = None, Sigma = None):
        self.Mu = Mu if Mu is not None else 0.0
        self.Sigma = Sigma if Sigma is not None else 1.0
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Mu' : float,
        'Sigma' : float
    }
    def __repr__(self):
        return "lognormvariate(Mu = "+repr(self.Mu)+" , Sigma = "+repr(self.Sigma)+" )" 
    
    def __call__(self, *args, **kwargs):
        import random
        return random.lognormvariate(self.Mu, self.Sigma)
    
    def _casts_to(self, dst):
        return lognormvariate._types[0]._casts_to(dst)
    
