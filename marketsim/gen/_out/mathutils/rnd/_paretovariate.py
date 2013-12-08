from marketsim import registry
from marketsim.ops._function import Function
from marketsim import float
@registry.expose(['Random', 'Pareto distribution'])
class paretovariate(Function[float]):
    """ 
    """ 
    def __init__(self, Alpha = None):
        self.Alpha = Alpha if Alpha is not None else 1.0
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Alpha' : float
    }
    def __repr__(self):
        return "paretovariate(Alpha = "+repr(self.Alpha)+" )" 
    
    def __call__(self, *args, **kwargs):
        import random
        return random.paretovariate(self.Alpha)
    
    def _casts_to(self, dst):
        return paretovariate._types[0]._casts_to(dst)
    
