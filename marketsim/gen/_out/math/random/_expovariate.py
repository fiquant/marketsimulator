from marketsim import registry
from marketsim.ops._function import Function
from marketsim import float
@registry.expose(["Random", "Exponential distribution"])
class expovariate(Function[float]):
    """ 
      Returned values range from 0 to positive infinity
    """ 
    def __init__(self, Lambda = None):
        from marketsim import rtti
        self.Lambda = Lambda if Lambda is not None else 1.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Lambda' : float
    }
    def __repr__(self):
        return "expovariate(%(Lambda)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        import random
        return random.expovariate(self.Lambda)
    
    def _casts_to(self, dst):
        return expovariate._types[0]._casts_to(dst)
    
