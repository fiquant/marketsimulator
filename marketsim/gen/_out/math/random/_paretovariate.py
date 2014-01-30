from marketsim import registry
from marketsim.ops._function import Function
@registry.expose(["Random", "Pareto distribution"])
class paretovariate(Function[float]):
    """ 
    """ 
    def __init__(self, Alpha = None):
        from marketsim import rtti
        self.Alpha = Alpha if Alpha is not None else 1.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Alpha' : float
    }
    def __repr__(self):
        return "paretovariate(%(Alpha)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        import random
        return random.paretovariate(self.Alpha)
    
    def _casts_to(self, dst):
        return paretovariate._types[0]._casts_to(dst)
    
