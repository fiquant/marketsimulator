from marketsim import registry
from marketsim.gen._out import constant
from marketsim import event
from marketsim import types
from marketsim import IFunction
from marketsim import IObservable
from marketsim import IFunction
from marketsim.ops._all import Observable
from marketsim.ops._all import constant
import math



@registry.expose(['Log/Pow', 'Exp'])
class Exp(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None):
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
        return "e^{%(x)s}" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        x = self.x()
        if x is None: return None
        return math.exp(self.x())
    
