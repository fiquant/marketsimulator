from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim.gen._intrinsic._constant import _Null_Impl
@registry.expose(["Basic", "null"])
class null_(Function[float],_Null_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        _Null_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "null" % self.__dict__
    
def null(): 
    from marketsim import rtti
    return null_()
    raise Exception("Cannot find suitable overload")
