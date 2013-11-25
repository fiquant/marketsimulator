from marketsim import registry, types, event
import math
from marketsim.ops._all import Observable, const

@registry.expose(['Log/Pow', 'Log'])
class Log(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None):
        Observable[float].__init__(self)
        self.x = x if x is not None else const(1.0)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)

    @property
    def label(self):
        return repr(self)

    _properties = {
        'x' : types.IFunction[float]
    }

    def __repr__(self):
        return "log(%(x)s)" % self.__dict__


    def __call__(self, *args, **kwargs):
        x = self.x()
        if x is None: return None
        return math.log(self.x())


