from marketsim import registry, types, ops
import random

@registry.expose(['Random', 'Uniform distribution'])
class uniform(ops.Function[float]):
    """ 
     Return a random floating point number *N* such that
     *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
     The end-point value *b* may or may not be included in the range depending on
     floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
    """ 
    def __init__(self, Low  = -10.0, High  = 10.0):
        self.Low = Low
        self.High = High

    @property
    def label(self):
        return repr(self)

    _properties = {
        'Low' : float,
        'High' : float
    }

    def __repr__(self):
        return "uniform(Low = "+repr(self.Low)+" , High = "+repr(self.High)+" )" 


    def __call__(self, *args, **kwargs):
        return random.uniform(self.Low, self.High)

    def _casts_to(self, dst):
        return uniform._types[0]._casts_to(dst)



