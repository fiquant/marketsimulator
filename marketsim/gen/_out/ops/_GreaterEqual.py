from marketsim import registry
from marketsim.gen._out._observable import Observablebool
from marketsim.gen._intrinsic.ops import _GreaterEqual_Impl
from marketsim.gen._out._iobservable import IObservablefloat
@registry.expose(["Ops", "GreaterEqual"])
class GreaterEqual_IObservableFloatIObservableFloat(Observablebool,_GreaterEqual_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable import Observablebool
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import rtti
        Observablebool.__init__(self)
        self.x = x if x is not None else _const_Float(1.0)
        event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else _const_Float(1.0)
        event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _GreaterEqual_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat,
        'y' : IObservablefloat
    }
    def __repr__(self):
        return "({%(x)s}>={%(y)s})" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _GreaterEqual_Impl
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable import Observablebool
@registry.expose(["Ops", "GreaterEqual"])
class GreaterEqual_FloatIObservableFloat(Observablebool,_GreaterEqual_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable import Observablebool
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablebool.__init__(self)
        self.x = x if x is not None else _constant_Float(1.0)
        
        self.y = y if y is not None else _const_Float(1.0)
        event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _GreaterEqual_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionfloat,
        'y' : IObservablefloat
    }
    def __repr__(self):
        return "({%(x)s}>={%(y)s})" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _GreaterEqual_Impl
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable import Observablebool
@registry.expose(["Ops", "GreaterEqual"])
class GreaterEqual_IObservableFloatFloat(Observablebool,_GreaterEqual_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable import Observablebool
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablebool.__init__(self)
        self.x = x if x is not None else _const_Float(1.0)
        event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
        _GreaterEqual_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat,
        'y' : IFunctionfloat
    }
    def __repr__(self):
        return "({%(x)s}>={%(y)s})" % self.__dict__
    
from marketsim import registry
from marketsim.gen._out._observable import Observablebool
from marketsim.gen._intrinsic.ops import _GreaterEqual_Impl
from marketsim.gen._out._ifunction import IFunctionfloat
@registry.expose(["Ops", "GreaterEqual"])
class GreaterEqual_FloatFloat(Observablebool,_GreaterEqual_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable import Observablebool
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        Observablebool.__init__(self)
        self.x = x if x is not None else _constant_Float(1.0)
        
        self.y = y if y is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
        _GreaterEqual_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionfloat,
        'y' : IFunctionfloat
    }
    def __repr__(self):
        return "({%(x)s}>={%(y)s})" % self.__dict__
    
def GreaterEqual(x = None,y = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        if y is None or rtti.can_be_casted(y, IObservablefloat):
            return GreaterEqual_IObservableFloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        if y is None or rtti.can_be_casted(y, IObservablefloat):
            return GreaterEqual_FloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        if y is None or rtti.can_be_casted(y, IFunctionfloat):
            return GreaterEqual_IObservableFloatFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        if y is None or rtti.can_be_casted(y, IFunctionfloat):
            return GreaterEqual_FloatFloat(x,y)
    raise Exception('Cannot find suitable overload for GreaterEqual('+str(x) +':'+ str(type(x))+','+str(y) +':'+ str(type(y))+')')
