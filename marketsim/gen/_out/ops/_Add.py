from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.ops import _Add_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Ops", "Add"])
class Add_IObservableFloatIObservableFloat(Observablefloat,_Add_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim import call
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else call(_const_Float,1.0)
        event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else call(_const_Float,1.0)
        event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _Add_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat,
        'y' : IObservablefloat
    }
    def __repr__(self):
        return "({%(x)s}+{%(y)s})" % self.__dict__
    
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._intrinsic.ops import _Add_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
@registry.expose(["Ops", "Add"])
class Add_FloatIObservableFloat(Observablefloat,_Add_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import call
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else call(_constant_Float,1.0)
        
        self.y = y if y is not None else call(_const_Float,1.0)
        event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _Add_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionfloat,
        'y' : IObservablefloat
    }
    def __repr__(self):
        return "({%(x)s}+{%(y)s})" % self.__dict__
    
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._intrinsic.ops import _Add_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
@registry.expose(["Ops", "Add"])
class Add_IObservableFloatFloat(Observablefloat,_Add_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import call
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else call(_const_Float,1.0)
        event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else call(_constant_Float,1.0)
        
        rtti.check_fields(self)
        _Add_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat,
        'y' : IFunctionfloat
    }
    def __repr__(self):
        return "({%(x)s}+{%(y)s})" % self.__dict__
    
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.ops import _Add_Impl
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Ops", "Add"])
class Add_FloatFloat(Observablefloat,_Add_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import call
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.x = x if x is not None else call(_constant_Float,1.0)
        
        self.y = y if y is not None else call(_constant_Float,1.0)
        
        rtti.check_fields(self)
        _Add_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionfloat,
        'y' : IFunctionfloat
    }
    def __repr__(self):
        return "({%(x)s}+{%(y)s})" % self.__dict__
    
def Add(x = None,y = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        if y is None or rtti.can_be_casted(y, IObservablefloat):
            return Add_IObservableFloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        if y is None or rtti.can_be_casted(y, IObservablefloat):
            return Add_FloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        if y is None or rtti.can_be_casted(y, IFunctionfloat):
            return Add_IObservableFloatFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        if y is None or rtti.can_be_casted(y, IFunctionfloat):
            return Add_FloatFloat(x,y)
    raise Exception('Cannot find suitable overload for Add('+str(x) +':'+ str(type(x))+','+str(y) +':'+ str(type(y))+')')
