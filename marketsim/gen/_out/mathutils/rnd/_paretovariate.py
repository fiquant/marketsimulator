from marketsim import registry, types, ops
import random

@registry.expose(['Random', 'Pareto distribution'])
class paretovariate(ops.Function[float]):

    """ 
    """ 
    def __init__(self, Alpha = Some(1.0)):
        self.Alpha = Alpha

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Alpha' : float
    }

    def __repr__(self):
        return "paretovariate(Alpha = "+repr(self.Alpha)+" )" 


    def __call__(self, *args, **kwargs):
        return random.paretovariate(self.Alpha)

    def _casts_to(self, dst):
        return paretovariate._types[0]._casts_to(dst)


