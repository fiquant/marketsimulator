from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
@registry.expose(["Random", "triangular"])
class triangular_FloatFloatFloat(Function[float]):
    """ 
     Return a random floating point number *N* such that *low* <= *N* <= *high* and
           with the specified *mode* between those bounds.
           The *low* and *high* bounds default to zero and one.
           The *mode* argument defaults to the midpoint between the bounds,
           giving a symmetric distribution.
    """ 
    def __init__(self, Low = None, High = None, Mode = None):
        from marketsim import rtti
        self.Low = Low if Low is not None else 0.0
        self.High = High if High is not None else 1.0
        self.Mode = Mode if Mode is not None else 0.5
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Low' : float,
        'High' : float,
        'Mode' : float
    }
    def __repr__(self):
        return "triangular(%(Low)s, %(High)s, %(Mode)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        import random
        return random.triangular(self.Low, self.High, self.Mode)
    
    def _casts_to(self, dst):
        return triangular_FloatFloatFloat._types[0]._casts_to(dst)
    
def triangular(Low = None,High = None,Mode = None): 
    from marketsim import float
    from marketsim import rtti
    if Low is None or rtti.can_be_casted(Low, float):
        if High is None or rtti.can_be_casted(High, float):
            if Mode is None or rtti.can_be_casted(Mode, float):
                return triangular_FloatFloatFloat(Low,High,Mode)
    raise Exception("Cannot find suitable overload")
