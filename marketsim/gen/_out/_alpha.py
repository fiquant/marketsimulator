from marketsim import registry
from marketsim.gen._out._ew import EW
@registry.expose(["-", "Alpha"])
class Alpha_EW(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._ew import EW_IObservableFloatFloat as _EW_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_EW_IObservableFloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : EW
    }
    def __repr__(self):
        return "EW_{%(alpha)s}(%(source)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.alpha
    
def Alpha(x = None): 
    from marketsim.gen._out._ew import EW
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, EW):
        return Alpha_EW(x)
    raise Exception('Cannot find suitable overload for Alpha('+str(x) +':'+ str(type(x))+')')
