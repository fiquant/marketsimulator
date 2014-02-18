from marketsim import registry
from marketsim.gen._out._side import Side
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.side import _None_Impl
@registry.expose(["Side", "observableNothing"])
class observableNothing_(Observable[Side],_None_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim.gen._out._side import Side
        from marketsim.ops._all import Observable
        from marketsim import rtti
        Observable[Side].__init__(self)
        
        rtti.check_fields(self)
        _None_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "observableNothing" % self.__dict__
    
def observableNothing(): 
    from marketsim import rtti
    return observableNothing_()
    raise Exception('Cannot find suitable overload for observableNothing('++')')
