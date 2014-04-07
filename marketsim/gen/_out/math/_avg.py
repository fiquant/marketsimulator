from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._intrinsic.moments.cma import CMA_Impl
from marketsim.gen._out.math._cumulative import Cumulative
@registry.expose(["Statistics", "Avg"])
class Avg_mathCumulative(IDifferentiable,CMA_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._cumulative import Cumulative_IObservableFloat as _math_Cumulative_IObservableFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_Cumulative_IObservableFloat())
        rtti.check_fields(self)
        CMA_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Cumulative
    }
    
    
    def __repr__(self):
        return "Avg(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._intrinsic.moments.ewma import EWMA_Impl
from marketsim.gen._out.math._ew import EW
@registry.expose(["Statistics", "Avg"])
class Avg_mathEW(IDifferentiable,EWMA_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_EW_IObservableFloatFloat())
        rtti.check_fields(self)
        EWMA_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : EW
    }
    
    
    def __repr__(self):
        return "Avg(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._intrinsic.moments.ma import MA_Impl
from marketsim.gen._out.math._moving import Moving
@registry.expose(["Statistics", "Avg"])
class Avg_mathMoving(IDifferentiable,MA_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._moving import Moving_IObservableFloatFloat as _math_Moving_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
        MA_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    
    
    def __repr__(self):
        return "Avg(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
def Avg(x = None): 
    from marketsim.gen._out.math._cumulative import Cumulative
    from marketsim.gen._out.math._ew import EW
    from marketsim.gen._out.math._moving import Moving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Cumulative):
        return Avg_mathCumulative(x)
    if x is None or rtti.can_be_casted(x, EW):
        return Avg_mathEW(x)
    if x is None or rtti.can_be_casted(x, Moving):
        return Avg_mathMoving(x)
    raise Exception('Cannot find suitable overload for Avg('+str(x) +':'+ str(type(x))+')')
