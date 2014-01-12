from marketsim import registry
from marketsim.gen._intrinsic.event import _Every_Impl
from marketsim import IFunction
@registry.expose(["Event", "Every"])
class Every(_Every_Impl):
    """ 
    """ 
    def __init__(self, intervalFunc = None):
        from marketsim.gen._out.mathutils.rnd._expovariate import expovariate as _mathutils_rnd_expovariate
        self.intervalFunc = intervalFunc if intervalFunc is not None else _mathutils_rnd_expovariate(1.0)
        _Every_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'intervalFunc' : IFunction[float]
    }
    def __repr__(self):
        return "Every(%(intervalFunc)s)" % self.__dict__
    
