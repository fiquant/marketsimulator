from marketsim import registry
from marketsim.ops._function import Function
from marketsim import float
from marketsim import float
@registry.expose(["Random", "Von Mises distribution"])
class vonmisesvariate(Function[float]):
    """ 
    """ 
    def __init__(self, Mu = None, Kappa = None):
        self.Mu = Mu if Mu is not None else 0.0
        self.Kappa = Kappa if Kappa is not None else 0.0
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Mu' : float,
        'Kappa' : float
    }
    def __repr__(self):
        return "vonmisesvariate(Mu = "+repr(self.Mu)+" , Kappa = "+repr(self.Kappa)+" )" 
    
    def __call__(self, *args, **kwargs):
        import random
        return random.vonmisesvariate(self.Mu, self.Kappa)
    
    def _casts_to(self, dst):
        return vonmisesvariate._types[0]._casts_to(dst)
    
