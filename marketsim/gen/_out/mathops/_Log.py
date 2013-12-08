from marketsim import registry
from marketsim.ops._all import Observable
from marketsim import IFunction
@registry.expose(['Log/Pow', 'Log'])
class Log(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out import constant
        from marketsim import event
        from marketsim import types
        Observable[float].__init__(self)
        self.x = x if x is not None else constant(1.0)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction
    }
    def __repr__(self):
        return "log(%(x)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        import math
        x = self.x()
        if x is None: return None
        return math.log(self.x())
    
