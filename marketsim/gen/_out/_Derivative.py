from marketsim import registry
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.observable.derivative import _Derivative_Impl
from marketsim import IDifferentiable
@registry.expose(["Basic", "Derivative"])
class Derivative(Function[float], _Derivative_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.observable.EW._Avg import Avg
        self.x = x if x is not None else Avg()
        _Derivative_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IDifferentiable
    }
    def __repr__(self):
        return "\\frac{d%(x)s}{dt}" % self.__dict__
    
