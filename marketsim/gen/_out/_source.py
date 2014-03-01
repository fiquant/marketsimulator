from marketsim import registry
from marketsim.gen._out._moving import Moving
@registry.expose(["-", "Source"])
class Source_Moving(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._moving import Moving_IObservableFloatFloat as _Moving_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    def __repr__(self):
        return "Moving_{%(timeframe)s}(%(source)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.source
    
from marketsim import registry
from marketsim.gen._out._ew import EW
@registry.expose(["-", "Source"])
class Source_EW(object):
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
        return self.x.source
    
from marketsim import registry
from marketsim.gen._out._cumulative import Cumulative
@registry.expose(["-", "Source"])
class Source_Cumulative(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._cumulative import Cumulative_IObservableFloat as _Cumulative_IObservableFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_Cumulative_IObservableFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Cumulative
    }
    def __repr__(self):
        return "Source(%(x)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.source
    
def Source(x = None): 
    from marketsim.gen._out._moving import Moving
    from marketsim.gen._out._ew import EW
    from marketsim.gen._out._cumulative import Cumulative
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Moving):
        return Source_Moving(x)
    if x is None or rtti.can_be_casted(x, EW):
        return Source_EW(x)
    if x is None or rtti.can_be_casted(x, Cumulative):
        return Source_Cumulative(x)
    raise Exception('Cannot find suitable overload for Source('+str(x) +':'+ str(type(x))+')')
