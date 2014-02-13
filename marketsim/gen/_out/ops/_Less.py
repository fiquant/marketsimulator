from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim.gen._intrinsic.ops import _Less_Impl
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "Less"])
class Less_IObservableFloatIObservableFloat(Observable[bool],_Less_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import bool
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[bool].__init__(self)
        self.x = x if x is not None else _const_Float(1.0)
        event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else _const_Float(1.0)
        event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _Less_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'y' : IObservable[float]
    }
    def __repr__(self):
        return "({%(x)s}<{%(y)s})" % self.__dict__
    
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IObservable
from marketsim.gen._intrinsic.ops import _Less_Impl
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "Less"])
class Less_IFunctionFloatIObservableFloat(Observable[bool],_Less_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import bool
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[bool].__init__(self)
        self.x = x if x is not None else _constant_Float(1.0)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else _const_Float(1.0)
        event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _Less_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'y' : IObservable[float]
    }
    def __repr__(self):
        return "({%(x)s}<{%(y)s})" % self.__dict__
    
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IObservable
from marketsim.gen._intrinsic.ops import _Less_Impl
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "Less"])
class Less_IObservableFloatIFunctionFloat(Observable[bool],_Less_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import bool
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[bool].__init__(self)
        self.x = x if x is not None else _const_Float(1.0)
        event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else _constant_Float(1.0)
        if isinstance(y, types.IEvent):
            event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _Less_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'y' : IFunction[float]
    }
    def __repr__(self):
        return "({%(x)s}<{%(y)s})" % self.__dict__
    
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim.gen._intrinsic.ops import _Less_Impl
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "Less"])
class Less_IFunctionFloatIFunctionFloat(Observable[bool],_Less_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim import bool
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import event
        Observable[bool].__init__(self)
        self.x = x if x is not None else _constant_Float(1.0)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        self.y = y if y is not None else _constant_Float(1.0)
        if isinstance(y, types.IEvent):
            event.subscribe(self.y, self.fire, self)
        rtti.check_fields(self)
        _Less_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'y' : IFunction[float]
    }
    def __repr__(self):
        return "({%(x)s}<{%(y)s})" % self.__dict__
    
def Less(x = None,y = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservable[float]):
        if y is None or rtti.can_be_casted(y, IObservable[float]):
            return Less_IObservableFloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        if y is None or rtti.can_be_casted(y, IObservable[float]):
            return Less_IFunctionFloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IObservable[float]):
        if y is None or rtti.can_be_casted(y, IFunction[float]):
            return Less_IObservableFloatIFunctionFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        if y is None or rtti.can_be_casted(y, IFunction[float]):
            return Less_IFunctionFloatIFunctionFloat(x,y)
    raise Exception('Cannot find suitable overload for Less('+str(x)+','+str(y)+')')
