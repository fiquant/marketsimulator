from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
@registry.expose(["Random", "vonmisesvariate"])
class vonmisesvariate(Function[float]):
    """ 
    """ 
    def __init__(self, Mu = None, Kappa = None):
        from marketsim import rtti
        self.Mu = Mu if Mu is not None else 0.0
        self.Kappa = Kappa if Kappa is not None else 0.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Mu' : float,
        'Kappa' : float
    }
    def __repr__(self):
        return "vonmisesvariate(%(Mu)s, %(Kappa)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        import random
        return random.vonmisesvariate(self.Mu, self.Kappa)
    
    def _casts_to(self, dst):
        return vonmisesvariate._types[0]._casts_to(dst)
    
vonmisesvariate = vonmisesvariate
