
from marketsim import registry, types, ops
import random
            
@registry.expose(['Random', 'Beta distribution'])
class betavariate(ops.Function[float]):
    """ 
     Conditions on the parameters are |alpha| > 0 and |beta| > 0.
     Returned values range between 0 and 1.
    """ 
    def __init__(self, Alpha = Some(1.0), Beta = Some(1.0)):
        self.Alpha = Alpha
        self.Beta = Beta

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
        return random.betavariate(self.Alpha, self.Beta)

    def _casts_to(self, dst):
        return betavariate._types[0]._casts_to(dst)
