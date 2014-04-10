from marketsim import registry
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._intrinsic.side import None_Impl
@registry.expose(["Side", "observableNothing"])
class observableNothing_(ObservableSide,None_Impl):
    """ **Observable always equal to None of type Side**
    
    
    Parameters are:
    """ 
    def __init__(self):
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import rtti
        ObservableSide.__init__(self)
        
        rtti.check_fields(self)
        None_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    def __repr__(self):
        return "observableNothing" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        delattr(self, '_processing_ex')
    
def observableNothing(): 
    from marketsim import rtti
    return observableNothing_()
    raise Exception('Cannot find suitable overload for observableNothing('++')')
