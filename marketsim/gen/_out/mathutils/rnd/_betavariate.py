from marketsim import registry
from marketsim.ops._function import Function
@registry.expose(["Random", "Beta distribution"])
class betavariate(Function[float]):
    """ 
     Conditions on the parameters are |alpha| > 0 and |beta| > 0.
     Returned values range between 0 and 1.
    """ 
    def __init__(self, Alpha = None, Beta = None):
        self.Alpha = Alpha if Alpha is not None else 1.0
        self.Beta = Beta if Beta is not None else 1.0
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Alpha' : float,
        'Beta' : float
    }
    def __repr__(self):
        return "betavariate(Alpha = "+repr(self.Alpha)+" , Beta = "+repr(self.Beta)+" )" 
    
    def __call__(self, *args, **kwargs):
        import random
        return random.betavariate(self.Alpha, self.Beta)
    
    def _casts_to(self, dst):
        return betavariate._types[0]._casts_to(dst)
    
