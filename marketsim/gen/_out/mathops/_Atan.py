from marketsim import registry
from marketsim import IObservable
from marketsim import IFunction
from marketsim.ops._all import Observable
from marketsim.ops._all import constant
from marketsim import IFunction



@registry.expose(['Trigonometric', 'Atan'])
class Atan(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out import constant
        from marketsim import event
        from marketsim import types
        Observable[float].__init__(self)
        self.x = x if x is not None else constant(0.0)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction
    }
    def __repr__(self):
        return "atan(%(x)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        import math
        x = self.x()
        if x is None: return None
        return math.atan(self.x())
    
