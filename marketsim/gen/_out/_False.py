from marketsim import registry
from marketsim.ops._function import Function
from marketsim.gen._intrinsic._constant import _False_Impl
@registry.expose(["Basic", "false"])
class false(Function[bool], _False_Impl):
    """ 
    """ 
    def __init__(self):
        
        _False_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "False" % self.__dict__
    
