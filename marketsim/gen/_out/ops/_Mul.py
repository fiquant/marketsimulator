from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.ops import _Mul_Impl
from marketsim import IObservable
from marketsim import registry
from marketsim import float
@registry.expose(["Ops", "Mul"])
class Mul_IObservableFloatIObservableFloat(Observable[float],_Mul_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const_Float as _const
        from marketsim import rtti
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else _const(1.0)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else _const(1.0)
        if isinstance(y, types.IEvent):
            event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _Mul_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'y' : IObservable[float]
    }
    def __repr__(self):
        return "({%(x)s}*{%(y)s})" % self.__dict__
    
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.ops import _Mul_Impl
from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import float
@registry.expose(["Ops", "Mul"])
class Mul_IObservableFloatIFunctionFloat(Observable[float],_Mul_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const_Float as _const
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else _const(1.0)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else _constant(1.0)
        if isinstance(y, types.IEvent):
            event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _Mul_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'y' : IFunction[float]
    }
    def __repr__(self):
        return "({%(x)s}*{%(y)s})" % self.__dict__
    
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.ops import _Mul_Impl
from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import float
@registry.expose(["Ops", "Mul"])
class Mul_IFunctionFloatIObservableFloat(Observable[float],_Mul_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const_Float as _const
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else _constant(1.0)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else _const(1.0)
        if isinstance(y, types.IEvent):
            event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _Mul_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'y' : IObservable[float]
    }
    def __repr__(self):
        return "({%(x)s}*{%(y)s})" % self.__dict__
    
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.ops import _Mul_Impl
from marketsim import IFunction
from marketsim import registry
from marketsim import float
@registry.expose(["Ops", "Mul"])
class Mul_IFunctionFloatIFunctionFloat(Observable[float],_Mul_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else _constant(1.0)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else _constant(1.0)
        if isinstance(y, types.IEvent):
            event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _Mul_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'y' : IFunction[float]
    }
    def __repr__(self):
        return "({%(x)s}*{%(y)s})" % self.__dict__
    
def Mul(x = None,y = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservable[float]):
        if y is None or rtti.can_be_casted(y, IObservable[float]):
            return Mul_IObservableFloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IObservable[float]):
        if y is None or rtti.can_be_casted(y, IFunction[float]):
            return Mul_IObservableFloatIFunctionFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        if y is None or rtti.can_be_casted(y, IObservable[float]):
            return Mul_IFunctionFloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        if y is None or rtti.can_be_casted(y, IFunction[float]):
            return Mul_IFunctionFloatIFunctionFloat(x,y)
    raise Exception('Cannot find suitable overload for Mul('+str(x)+','+str(y)+')')
