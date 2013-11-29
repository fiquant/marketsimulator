from marketsim import registry, types, _
from marketsim.ops._function import Function
from marketsim.gen._intrinsic._constant import _Constant_Impl

@registry.expose(['Basic', 'const'])
class const(Function[float], _Constant_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        self.x = x if x is not None else 1.0

    @property
    def label(self):
        return repr(self)

    _properties = {
        'x' : float
    }

    def __repr__(self):
        return "C=%x" % self.__dict__



