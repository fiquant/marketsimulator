from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
@registry.expose(["Random", "betavariate"])
class betavariate_FloatFloat(Function[float]):
    """ 
     Conditions on the parameters are |alpha| > 0 and |beta| > 0.
     Returned values range between 0 and 1.
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
        return "betavariate(%(Alpha)s, %(Beta)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        import random
        return random.betavariate(self.Alpha, self.Beta)
    
    def _casts_to(self, dst):
        return betavariate_FloatFloat._types[0]._casts_to(dst)
    
def betavariate(Alpha = None,Beta = None): 
    from marketsim import float
    from marketsim import rtti
    if Alpha is None or rtti.can_be_casted(Alpha, float):
        if Beta is None or rtti.can_be_casted(Beta, float):
            return betavariate_FloatFloat(Alpha,Beta)
    raise Exception("Cannot find suitable overload")
