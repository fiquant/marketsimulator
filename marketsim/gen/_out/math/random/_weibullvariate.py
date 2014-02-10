from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
@registry.expose(["Random", "weibullvariate"])
class weibullvariate_FloatFloat(Function[float]):
    """ 
    """ 
    def __init__(self, Alpha = None, Beta = None):
        from marketsim import rtti
        self.Alpha = Alpha if Alpha is not None else 1.0
        self.Beta = Beta if Beta is not None else 1.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Alpha' : float,
        'Beta' : float
    }
    def __repr__(self):
        return "weibullvariate(%(Alpha)s, %(Beta)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        import random
        return random.weibullvariate(self.Alpha, self.Beta)
    
    def _casts_to(self, dst):
        return weibullvariate_FloatFloat._types[0]._casts_to(dst)
    
def weibullvariate(Alpha = None,Beta = None): 
    from marketsim import float
    from marketsim import rtti
    if Alpha is None or rtti.can_be_casted(Alpha, float):
        if Beta is None or rtti.can_be_casted(Beta, float):
            return weibullvariate_FloatFloat(Alpha,Beta)
    raise Exception("Cannot find suitable overload")
