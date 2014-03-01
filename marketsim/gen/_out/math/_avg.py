from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._intrinsic.moments.ewma import EWMA_Impl
from marketsim.gen._out._ew import EW
@registry.expose(["Statistics", "Avg"])
class Avg_EW(IDifferentiable,EWMA_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._ew import EW_IObservableFloatFloat as _EW_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_EW_IObservableFloatFloat())
        rtti.check_fields(self)
        EWMA_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : EW
    }
    def __repr__(self):
        return "Avg(%(x)s)" % self.__dict__
    
from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._intrinsic.moments.cma import CMA_Impl
from marketsim.gen._out._cumulative import Cumulative
@registry.expose(["Statistics", "Avg"])
class Avg_Cumulative(IDifferentiable,CMA_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._cumulative import Cumulative_IObservableFloat as _Cumulative_IObservableFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_Cumulative_IObservableFloat())
        rtti.check_fields(self)
        CMA_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Cumulative
    }
    def __repr__(self):
        return "Avg(%(x)s)" % self.__dict__
    
from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._intrinsic.moments.ma import MA_Impl
from marketsim.gen._out._moving import Moving
@registry.expose(["Statistics", "Avg"])
class Avg_Moving(IDifferentiable,MA_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._moving import Moving_IObservableFloatFloat as _Moving_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
        MA_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    def __repr__(self):
        return "Avg(%(x)s)" % self.__dict__
    
def Avg(x = None): 
    from marketsim.gen._out._ew import EW
    from marketsim.gen._out._cumulative import Cumulative
    from marketsim.gen._out._moving import Moving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, EW):
        return Avg_EW(x)
    if x is None or rtti.can_be_casted(x, Cumulative):
        return Avg_Cumulative(x)
    if x is None or rtti.can_be_casted(x, Moving):
        return Avg_Moving(x)
    raise Exception('Cannot find suitable overload for Avg('+str(x) +':'+ str(type(x))+')')
