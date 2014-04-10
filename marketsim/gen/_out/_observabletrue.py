from marketsim import registry
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic._constant import True_Impl
@registry.expose(["Basic", "observableTrue"])
class observableTrue_(Observablebool,True_Impl):
    """ **Trivial observable always returning *True***
    
    
    Parameters are:
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
        return "True" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        
        delattr(self, '_processing_ex')
    
def observableTrue(): 
    from marketsim import rtti
    return observableTrue_()
    raise Exception('Cannot find suitable overload for observableTrue('++')')
