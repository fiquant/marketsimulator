from marketsim import registry, types, ops
import random

@registry.expose(['Random', 'Triangular distribution'])
class triangular(ops.Function[float]):

    """ 
     Return a random floating point number *N* such that *low* <= *N* <= *high* and
           with the specified *mode* between those bounds.
           The *low* and *high* bounds default to zero and one.
           The *mode* argument defaults to the midpoint between the bounds,
           giving a symmetric distribution.
    """ 
    def __init__(self, Low  = 0.0, High  = 1.0, Mode  = 0.5):
        self.Low = Low
        self.High = High
        self.Mode = Mode

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Low' : float,
        'High' : float,
        'Mode' : float
    }

    def __repr__(self):
        return "triangular(Low = "+repr(self.Low)+" , High = "+repr(self.High)+" , Mode = "+repr(self.Mode)+" )" 


    def __call__(self, *args, **kwargs):
        return random.triangular(self.Low, self.High, self.Mode)

    def _casts_to(self, dst):
        return triangular._types[0]._casts_to(dst)


