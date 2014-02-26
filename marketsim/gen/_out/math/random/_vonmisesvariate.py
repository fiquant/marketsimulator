from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Random", "vonmisesvariate"])
class vonmisesvariate_FloatFloat(IFunctionfloat):
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
        return vonmisesvariate_FloatFloat._types[0]._casts_to(dst)
    
def vonmisesvariate(Mu = None,Kappa = None): 
    from marketsim import rtti
    if Mu is None or rtti.can_be_casted(Mu, float):
        if Kappa is None or rtti.can_be_casted(Kappa, float):
            return vonmisesvariate_FloatFloat(Mu,Kappa)
    raise Exception('Cannot find suitable overload for vonmisesvariate('+str(Mu) +':'+ str(type(Mu))+','+str(Kappa) +':'+ str(type(Kappa))+')')
