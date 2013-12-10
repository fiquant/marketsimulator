from marketsim import registry
from marketsim.ops._function import Function
from marketsim import float
from marketsim import float
@registry.expose(["Random", "Normal distribution"])
class normalvariate(Function[float]):
    """ 
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
        return "normalvariate(Mu = "+repr(self.Mu)+" , Sigma = "+repr(self.Sigma)+" )" 
    
    def __call__(self, *args, **kwargs):
        import random
        return random.normalvariate(self.Mu, self.Sigma)
    
    def _casts_to(self, dst):
        return normalvariate._types[0]._casts_to(dst)
    
