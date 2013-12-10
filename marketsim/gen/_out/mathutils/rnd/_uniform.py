from marketsim import registry
from marketsim.ops._function import Function
from marketsim import float
from marketsim import float
@registry.expose(["Random", "Uniform distribution"])
class uniform(Function[float]):
    """ 
     Return a random floating point number *N* such that
     *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
     The end-point value *b* may or may not be included in the range depending on
     floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
    """ 
    def __init__(self, Low = None, High = None):
        self.Low = Low if Low is not None else -10.0
        self.High = High if High is not None else 10.0
    
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
        import random
        return random.uniform(self.Low, self.High)
    
    def _casts_to(self, dst):
        return uniform._types[0]._casts_to(dst)
    
