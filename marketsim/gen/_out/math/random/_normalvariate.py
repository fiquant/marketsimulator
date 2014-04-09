from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Random", "normalvariate"])
class normalvariate_FloatFloat(IFunctionfloat):
    """ **Normal distribution**
    
    
    Parameters are:
    
    **Mu**
    	 |mu| is the mean                  
    
    **Sigma**
    	 |sigma| is the standard deviation 
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
        return "normalvariate(%(Mu)s, %(Sigma)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def __call__(self, *args, **kwargs):
        import random
        return random.normalvariate(self.Mu, self.Sigma)
    
    def _casts_to(self, dst):
        return normalvariate_FloatFloat._types[0]._casts_to(dst)
    
def normalvariate(Mu = None,Sigma = None): 
    from marketsim import rtti
    if Mu is None or rtti.can_be_casted(Mu, float):
        if Sigma is None or rtti.can_be_casted(Sigma, float):
            return normalvariate_FloatFloat(Mu,Sigma)
    raise Exception('Cannot find suitable overload for normalvariate('+str(Mu) +':'+ str(type(Mu))+','+str(Sigma) +':'+ str(type(Sigma))+')')
