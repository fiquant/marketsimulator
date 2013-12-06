from marketsim import registry
from marketsim import IObservable
from marketsim import IFunction
from marketsim.ops._function import Function
from marketsim import float
from marketsim import float
from marketsim import float
from marketsim import registry, types
import random


@registry.expose(['Random', 'Triangular distribution'])
class triangular(Function[float]):
    """ 
     Return a random floating point number *N* such that *low* <= *N* <= *high* and
           with the specified *mode* between those bounds.
           The *low* and *high* bounds default to zero and one.
           The *mode* argument defaults to the midpoint between the bounds,
           giving a symmetric distribution.
    """ 
    def __init__(self, Low = None, High = None, Mode = None):
        self.Low = Low if Low is not None else 0.0
        self.High = High if High is not None else 1.0
        self.Mode = Mode if Mode is not None else 0.5
    
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
        import random
        return random.triangular(self.Low, self.High, self.Mode)
    
    def _casts_to(self, dst):
        return triangular._types[0]._casts_to(dst)
    
