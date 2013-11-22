from marketsim import registry, types, ops
import random

@registry.expose(['Random', 'Log normal distribution'])
class lognormvariate(ops.Function[float]):
    """ 
     If you take the natural logarithm of this distribution,
      you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
      |mu| can have any value, and |sigma| must be greater than zero.
    """ 
    def __init__(self, Mu = Some(0.0), Sigma = Some(1.0)):
        self.Mu = Mu
        self.Sigma = Sigma

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
        return random.lognormvariate(self.Mu, self.Sigma)

    def _casts_to(self, dst):
        return lognormvariate._types[0]._casts_to(dst)
