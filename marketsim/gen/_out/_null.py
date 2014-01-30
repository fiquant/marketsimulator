from marketsim import registry
from marketsim.ops._function import Function
from marketsim.gen._intrinsic._constant import _Null_Impl
@registry.expose(["Basic", "null"])
class null(Function[float], _Null_Impl):""" 
    """ 
    def __init__(self):from marketsim import rtti
        
        rtti.check_fields(self)
        _Null_Impl.__init__(self)
    
    @property
    def label(self):return repr(self)
    
    _properties = {
    }
    def __repr__(self):return "null" % self.__dict__
    
