from marketsim import registry
from marketsim import bool
from marketsim import IFunction
from marketsim.gen._intrinsic._constant import _True_Impl
@registry.expose(["Basic", "true"])
class true_(IFunction[bool],_True_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        _True_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "True" % self.__dict__
    
def true(): 
    from marketsim import rtti
    return true_()
    raise Exception('Cannot find suitable overload for true('++')')
