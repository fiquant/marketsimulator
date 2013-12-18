from marketsim import registry
from marketsim.ops._function import Function
from marketsim import Side
from marketsim.gen._intrinsic.side import _Buy_Impl
@registry.expose(["Side", "Nothing"])
class Nothing(Function[Side], _Buy_Impl):
    """ 
    """ 
    def __init__(self):
        
        _Buy_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "NoneSide" % self.__dict__
    
