from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.ops import Negate_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Ops", "Negate"])
class Negate_IObservableFloat(Observablefloat,Negate_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_const_Float(1.0))
        event.subscribe(self.x, self.fire, self)
        rtti.check_fields(self)
        Negate_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat
    }
    
    
    def __repr__(self):
        return "-%(x)s" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.ops import Negate_Impl
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Ops", "Negate"])
class Negate_Float(Observablefloat,Negate_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_constant_Float(1.0))
        
        rtti.check_fields(self)
        Negate_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "-%(x)s" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
def Negate(x = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        return Negate_IObservableFloat(x)
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        return Negate_Float(x)
    raise Exception('Cannot find suitable overload for Negate('+str(x) +':'+ str(type(x))+')')
