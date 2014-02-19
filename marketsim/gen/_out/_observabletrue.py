from marketsim import registry
from marketsim.gen._out._observable import Observablebool
from marketsim.gen._intrinsic._constant import _True_Impl
@registry.expose(["Basic", "observableTrue"])
class observableTrue_(Observablebool,_True_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim.gen._out._observable import Observablebool
        from marketsim import rtti
        Observablebool.__init__(self)
        
        rtti.check_fields(self)
        _True_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "True" % self.__dict__
    
def observableTrue(): 
    from marketsim import rtti
    return observableTrue_()
    raise Exception('Cannot find suitable overload for observableTrue('++')')
