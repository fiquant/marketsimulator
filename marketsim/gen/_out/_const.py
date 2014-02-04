from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim.gen._intrinsic._constant import _Constant_Impl
from marketsim import float
@registry.expose(["Basic", "const"])
class const_Optional__Float_(Function[float], _Constant_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import rtti
        self.x = x if x is not None else 1.0
        rtti.check_fields(self)
        _Constant_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : float
    }
    def __repr__(self):
        return "C=%(x)s" % self.__dict__
    
const = const_Optional__Float_
