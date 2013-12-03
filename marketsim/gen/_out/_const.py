from marketsim import registry
from marketsim import IObservable
from marketsim import IFunction
from marketsim.ops._function import Function
from marketsim.gen._intrinsic._constant import _Constant_Impl



@registry.expose(['Basic', 'const'])
class const(Function[float], _Constant_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        self.x = x if x is not None else 1.0
        _Constant_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : float
    }
    def __repr__(self):
        return "C=%(x)s" % self.__dict__
    
