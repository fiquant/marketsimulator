from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "Condition_Float"])
class Condition_Float_IFunctionBooleanIObservableFloatIObservableFloat(Observable[float],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.cond = cond if cond is not None else _true_()
        if isinstance(cond, types.IEvent):
            event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _const_Float(1.0)
        if isinstance(ifpart, types.IEvent):
            event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _const_Float(1.0)
        if isinstance(elsepart, types.IEvent):
            event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunction[bool],
        'ifpart' : IObservable[float],
        'elsepart' : IObservable[float]
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "Condition_Float"])
class Condition_Float_IFunctionBooleanIObservableFloatIFunctionFloat(Observable[float],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.cond = cond if cond is not None else _true_()
        if isinstance(cond, types.IEvent):
            event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _const_Float(1.0)
        if isinstance(ifpart, types.IEvent):
            event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _constant_Float(1.0)
        if isinstance(elsepart, types.IEvent):
            event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunction[bool],
        'ifpart' : IObservable[float],
        'elsepart' : IFunction[float]
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "Condition_Float"])
class Condition_Float_IFunctionBooleanIFunctionFloatIObservableFloat(Observable[float],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.cond = cond if cond is not None else _true_()
        if isinstance(cond, types.IEvent):
            event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _constant_Float(1.0)
        if isinstance(ifpart, types.IEvent):
            event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _const_Float(1.0)
        if isinstance(elsepart, types.IEvent):
            event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunction[bool],
        'ifpart' : IFunction[float],
        'elsepart' : IObservable[float]
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "Condition_Float"])
class Condition_Float_IFunctionBooleanIFunctionFloatIFunctionFloat(Observable[float],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._true import true_ as _true_
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.cond = cond if cond is not None else _true_()
        if isinstance(cond, types.IEvent):
            event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _constant_Float(1.0)
        if isinstance(ifpart, types.IEvent):
            event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _constant_Float(1.0)
        if isinstance(elsepart, types.IEvent):
            event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunction[bool],
        'ifpart' : IFunction[float],
        'elsepart' : IFunction[float]
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
def Condition_Float(cond = None,ifpart = None,elsepart = None): 
    from marketsim import bool
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import IObservable
    from marketsim import float
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservable[float]):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservable[float]):
                return Condition_Float_IFunctionBooleanIObservableFloatIObservableFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservable[float]):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunction[float]):
                return Condition_Float_IFunctionBooleanIObservableFloatIFunctionFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunction[float]):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservable[float]):
                return Condition_Float_IFunctionBooleanIFunctionFloatIObservableFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunction[float]):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunction[float]):
                return Condition_Float_IFunctionBooleanIFunctionFloatIFunctionFloat(cond,ifpart,elsepart)
    raise Exception('Cannot find suitable overload for Condition_Float('+str(cond)+','+str(ifpart)+','+str(elsepart)+')')
