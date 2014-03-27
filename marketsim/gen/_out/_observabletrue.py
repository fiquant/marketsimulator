from marketsim import registry
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic._constant import True_Impl
@registry.expose(["Basic", "observableTrue"])
class observableTrue_(Observablebool,True_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim import rtti
        Observablebool.__init__(self)
        
        rtti.check_fields(self)
        True_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "True" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
def observableTrue(): 
    from marketsim import rtti
    return observableTrue_()
    raise Exception('Cannot find suitable overload for observableTrue('++')')
