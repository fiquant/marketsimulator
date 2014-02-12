from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "Condition"])
class Condition_IFunctionBooleanIObservableFloatIObservableFloat(Observable[float],_Condition_Impl):
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
from marketsim import Side
from marketsim import registry
from marketsim import bool
@registry.expose(["Ops", "Condition"])
class Condition_IFunctionBooleanIObservableSideIObservableSide(Observable[Side],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import types
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out.side.observable._sell import Sell_ as _side_observable_Sell_
        from marketsim import event
        from marketsim.gen._out.side.observable._buy import Buy_ as _side_observable_Buy_
        Observable[Side].__init__(self)
        self.cond = cond if cond is not None else _true_()
        if isinstance(cond, types.IEvent):
            event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _side_observable_Sell_()
        if isinstance(ifpart, types.IEvent):
            event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _side_observable_Buy_()
        if isinstance(elsepart, types.IEvent):
            event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunction[bool],
        'ifpart' : IObservable[Side],
        'elsepart' : IObservable[Side]
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
@registry.expose(["Ops", "Condition"])
class Condition_IFunctionBooleanIObservableFloatIFunctionFloat(Observable[float],_Condition_Impl):
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
@registry.expose(["Ops", "Condition"])
class Condition_IFunctionBooleanIFunctionFloatIObservableFloat(Observable[float],_Condition_Impl):
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
from marketsim import IObservable
from marketsim import Side
from marketsim import registry
from marketsim import bool
@registry.expose(["Ops", "Condition"])
class Condition_IFunctionBooleanIObservableSideSide(Observable[Side],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import types
        from marketsim import Side
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out.side.observable._sell import Sell_ as _side_observable_Sell_
        from marketsim import event
        Observable[Side].__init__(self)
        self.cond = cond if cond is not None else _true_()
        if isinstance(cond, types.IEvent):
            event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _side_observable_Sell_()
        if isinstance(ifpart, types.IEvent):
            event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _side_Buy_()
        if isinstance(elsepart, types.IEvent):
            event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunction[bool],
        'ifpart' : IObservable[Side],
        'elsepart' : IFunction[Side]
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IObservable
from marketsim import Side
from marketsim import registry
from marketsim import bool
@registry.expose(["Ops", "Condition"])
class Condition_IFunctionBooleanSideIObservableSide(Observable[Side],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import types
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._true import true_ as _true_
        from marketsim import event
        from marketsim.gen._out.side.observable._buy import Buy_ as _side_observable_Buy_
        Observable[Side].__init__(self)
        self.cond = cond if cond is not None else _true_()
        if isinstance(cond, types.IEvent):
            event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _side_Sell_()
        if isinstance(ifpart, types.IEvent):
            event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _side_observable_Buy_()
        if isinstance(elsepart, types.IEvent):
            event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunction[bool],
        'ifpart' : IFunction[Side],
        'elsepart' : IObservable[Side]
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import registry
from marketsim import bool
from marketsim import float
@registry.expose(["Ops", "Condition"])
class Condition_IFunctionBooleanIFunctionFloatIFunctionFloat(Observable[float],_Condition_Impl):
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
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import Side
from marketsim import registry
from marketsim import bool
@registry.expose(["Ops", "Condition"])
class Condition_IFunctionBooleanSideSide(Observable[Side],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import types
        from marketsim import Side
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._true import true_ as _true_
        from marketsim import event
        Observable[Side].__init__(self)
        self.cond = cond if cond is not None else _true_()
        if isinstance(cond, types.IEvent):
            event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _side_Sell_()
        if isinstance(ifpart, types.IEvent):
            event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _side_Buy_()
        if isinstance(elsepart, types.IEvent):
            event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunction[bool],
        'ifpart' : IFunction[Side],
        'elsepart' : IFunction[Side]
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
def Condition(cond = None,ifpart = None,elsepart = None): 
    from marketsim import bool
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import IObservable
    from marketsim import float
    from marketsim import Side
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservable[float]):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservable[float]):
                return Condition_IFunctionBooleanIObservableFloatIObservableFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservable[Side]):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservable[Side]):
                return Condition_IFunctionBooleanIObservableSideIObservableSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservable[float]):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunction[float]):
                return Condition_IFunctionBooleanIObservableFloatIFunctionFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunction[float]):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservable[float]):
                return Condition_IFunctionBooleanIFunctionFloatIObservableFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservable[Side]):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunction[Side]):
                return Condition_IFunctionBooleanIObservableSideSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunction[Side]):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservable[Side]):
                return Condition_IFunctionBooleanSideIObservableSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunction[float]):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunction[float]):
                return Condition_IFunctionBooleanIFunctionFloatIFunctionFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunction[Side]):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunction[Side]):
                return Condition_IFunctionBooleanSideSide(cond,ifpart,elsepart)
    raise Exception('Cannot find suitable overload for Condition('+str(cond)+','+str(ifpart)+','+str(elsepart)+')')
