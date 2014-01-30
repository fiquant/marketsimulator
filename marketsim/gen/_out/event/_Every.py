from marketsim import registry
from marketsim.gen._intrinsic.event import _Every_Impl
from marketsim import IFunction
@registry.expose(["Event", "Every"])
class Every(_Every_Impl):""" 
    """ 
    def __init__(self, intervalFunc = None):from marketsim.gen._out.math.random._expovariate import expovariate as _math_random_expovariate
        from marketsim import rtti
        self.intervalFunc = intervalFunc if intervalFunc is not None else _math_random_expovariate(1.0)
        rtti.check_fields(self)
        _Every_Impl.__init__(self)
    
    @property
    def label(self):return repr(self)
    
    _properties = {'intervalFunc' : IFunction[float]
    }
    def __repr__(self):return "Every(%(intervalFunc)s)" % self.__dict__
    
