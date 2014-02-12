from marketsim import registry
from marketsim import bool
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic._constant import _True_Impl
@registry.expose(["Basic", "observableTrue"])
class observableTrue_(Observable[bool],_True_Impl):
    """ 
    """ 
    def __init__(self):
        from marketsim import bool
        from marketsim.ops._all import Observable
        from marketsim import rtti
        Observable[bool].__init__(self)
        
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
