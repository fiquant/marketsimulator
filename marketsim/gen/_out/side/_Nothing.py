from marketsim import registry
from marketsim import Side
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.side import _None_Impl
@registry.expose(["Side", "Nothing"])
class Nothing_(Function[Side],_None_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        _None_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "Nothing" % self.__dict__
    
def Nothing(): 
    return Nothing_()
