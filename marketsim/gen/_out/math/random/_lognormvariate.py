from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
@registry.expose(["Random", "lognormvariate"])
class lognormvariate_FloatFloat(Function[float]):
    """ 
     If you take the natural logarithm of this distribution,
      you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
      |mu| can have any value, and |sigma| must be greater than zero.
    """ 
    def __init__(self, Mu = None, Sigma = None):
        from marketsim import rtti
        self.Mu = Mu if Mu is not None else 0.0
        self.Sigma = Sigma if Sigma is not None else 1.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Mu' : float,
        'Sigma' : float
    }
    def __repr__(self):
        return "lognormvariate(%(Mu)s, %(Sigma)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        import random
        return random.lognormvariate(self.Mu, self.Sigma)
    
    def _casts_to(self, dst):
        return lognormvariate_FloatFloat._types[0]._casts_to(dst)
    
def lognormvariate(Mu = None,Sigma = None): 
    from marketsim import float
    from marketsim import rtti
    if Mu is None or rtti.can_be_casted(Mu, float):
        if Sigma is None or rtti.can_be_casted(Sigma, float):
            return lognormvariate_FloatFloat(Mu,Sigma)
    raise Exception('Cannot find suitable overload for lognormvariate('+str(Mu)+','+str(Sigma)+')')
