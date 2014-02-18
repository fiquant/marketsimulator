from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableFloatIObservableFloat(Observable[float],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[float].__init__(self)
        self.cond = cond if cond is not None else _observableTrue_()
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _const_Float(1.0)
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _const_Float(1.0)
        event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IObservablefloat,
        'elsepart' : IObservablefloat
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._side import Side
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableSideIObservableSide(Observable[Side],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._side import Side
        from marketsim import event
        from marketsim.gen._out.side._observablebuy import observableBuy_ as _side_observableBuy_
        Observable[Side].__init__(self)
        self.cond = cond if cond is not None else _observableTrue_()
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _side_observableSell_()
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _side_observableBuy_()
        event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IObservableSide,
        'elsepart' : IObservableSide
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._ifunction import IFunctionbool
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableFloatIObservableFloat(Observable[float],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[float].__init__(self)
        self.cond = cond if cond is not None else _true_()
        
        self.ifpart = ifpart if ifpart is not None else _const_Float(1.0)
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _const_Float(1.0)
        event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IObservablefloat,
        'elsepart' : IObservablefloat
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanFloatIObservableFloat(Observable[float],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[float].__init__(self)
        self.cond = cond if cond is not None else _observableTrue_()
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _constant_Float(1.0)
        
        self.elsepart = elsepart if elsepart is not None else _const_Float(1.0)
        event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IFunctionfloat,
        'elsepart' : IObservablefloat
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableFloatFloat(Observable[float],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[float].__init__(self)
        self.cond = cond if cond is not None else _observableTrue_()
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _const_Float(1.0)
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IObservablefloat,
        'elsepart' : IFunctionfloat
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction import IFunctionbool
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableSideIObservableSide(Observable[Side],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._true import true_ as _true_
        from marketsim import event
        from marketsim.gen._out.side._observablebuy import observableBuy_ as _side_observableBuy_
        Observable[Side].__init__(self)
        self.cond = cond if cond is not None else _true_()
        
        self.ifpart = ifpart if ifpart is not None else _side_observableSell_()
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _side_observableBuy_()
        event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IObservableSide,
        'elsepart' : IObservableSide
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction import IFunctionSide
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanSideIObservableSide(Observable[Side],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._side import Side
        from marketsim import event
        from marketsim.gen._out.side._observablebuy import observableBuy_ as _side_observableBuy_
        Observable[Side].__init__(self)
        self.cond = cond if cond is not None else _observableTrue_()
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _side_Sell_()
        
        self.elsepart = elsepart if elsepart is not None else _side_observableBuy_()
        event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IFunctionSide,
        'elsepart' : IObservableSide
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction import IFunctionSide
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableSideSide(Observable[Side],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._side import Side
        from marketsim import event
        Observable[Side].__init__(self)
        self.cond = cond if cond is not None else _observableTrue_()
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _side_observableSell_()
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _side_Buy_()
        
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IObservableSide,
        'elsepart' : IFunctionSide
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim.gen._out._ifunction import IFunctionbool
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_BooleanFloatIObservableFloat(Observable[float],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[float].__init__(self)
        self.cond = cond if cond is not None else _true_()
        
        self.ifpart = ifpart if ifpart is not None else _constant_Float(1.0)
        
        self.elsepart = elsepart if elsepart is not None else _const_Float(1.0)
        event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IFunctionfloat,
        'elsepart' : IObservablefloat
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim.gen._out._ifunction import IFunctionbool
from marketsim.gen._out._iobservable import IObservablefloat
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableFloatFloat(Observable[float],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[float].__init__(self)
        self.cond = cond if cond is not None else _true_()
        
        self.ifpart = ifpart if ifpart is not None else _const_Float(1.0)
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IObservablefloat,
        'elsepart' : IFunctionfloat
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanFloatFloat(Observable[float],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import event
        Observable[float].__init__(self)
        self.cond = cond if cond is not None else _observableTrue_()
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _constant_Float(1.0)
        
        self.elsepart = elsepart if elsepart is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IFunctionfloat,
        'elsepart' : IFunctionfloat
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction import IFunctionbool
from marketsim.gen._out._ifunction import IFunctionSide
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_BooleanSideIObservableSide(Observable[Side],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._true import true_ as _true_
        from marketsim import event
        from marketsim.gen._out.side._observablebuy import observableBuy_ as _side_observableBuy_
        Observable[Side].__init__(self)
        self.cond = cond if cond is not None else _true_()
        
        self.ifpart = ifpart if ifpart is not None else _side_Sell_()
        
        self.elsepart = elsepart if elsepart is not None else _side_observableBuy_()
        event.subscribe(self.elsepart, self.fire, self)
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IFunctionSide,
        'elsepart' : IObservableSide
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._iobservable import IObservableSide
from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction import IFunctionbool
from marketsim.gen._out._ifunction import IFunctionSide
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableSideSide(Observable[Side],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._true import true_ as _true_
        from marketsim import event
        Observable[Side].__init__(self)
        self.cond = cond if cond is not None else _true_()
        
        self.ifpart = ifpart if ifpart is not None else _side_observableSell_()
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _side_Buy_()
        
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IObservableSide,
        'elsepart' : IFunctionSide
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._iobservable import IObservablebool
from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction import IFunctionSide
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanSideSide(Observable[Side],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._side import Side
        from marketsim import event
        Observable[Side].__init__(self)
        self.cond = cond if cond is not None else _observableTrue_()
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _side_Sell_()
        
        self.elsepart = elsepart if elsepart is not None else _side_Buy_()
        
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IObservablebool,
        'ifpart' : IFunctionSide,
        'elsepart' : IFunctionSide
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim.gen._out._ifunction import IFunctionbool
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_BooleanFloatFloat(Observable[float],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.ops._all import Observable
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        Observable[float].__init__(self)
        self.cond = cond if cond is not None else _true_()
        
        self.ifpart = ifpart if ifpart is not None else _constant_Float(1.0)
        
        self.elsepart = elsepart if elsepart is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IFunctionfloat,
        'elsepart' : IFunctionfloat
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction import IFunctionbool
from marketsim.gen._out._ifunction import IFunctionSide
from marketsim import registry
@registry.expose(["Ops", "Condition"])
class Condition_BooleanSideSide(Observable[Side],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._true import true_ as _true_
        Observable[Side].__init__(self)
        self.cond = cond if cond is not None else _true_()
        
        self.ifpart = ifpart if ifpart is not None else _side_Sell_()
        
        self.elsepart = elsepart if elsepart is not None else _side_Buy_()
        
        rtti.check_fields(self)
        _Condition_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'cond' : IFunctionbool,
        'ifpart' : IFunctionSide,
        'elsepart' : IFunctionSide
    }
    def __repr__(self):
        return "(if %(cond)s then %(ifpart)s else %(elsepart)s)" % self.__dict__
    
def Condition(cond = None,ifpart = None,elsepart = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim import rtti
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._side import Side
    from marketsim.gen._out._iobservable import IObservableSide
    from marketsim.gen._out._ifunction import IFunctionbool
    from marketsim.gen._out._ifunction import IFunctionSide
    from marketsim.gen._out._iobservable import IObservablebool
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservablefloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservablefloat):
                return Condition_IObservableBooleanIObservableFloatIObservableFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservableSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservableSide):
                return Condition_IObservableBooleanIObservableSideIObservableSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservablefloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservablefloat):
                return Condition_BooleanIObservableFloatIObservableFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionfloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservablefloat):
                return Condition_IObservableBooleanFloatIObservableFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservablefloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionfloat):
                return Condition_IObservableBooleanIObservableFloatFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservableSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservableSide):
                return Condition_BooleanIObservableSideIObservableSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservableSide):
                return Condition_IObservableBooleanSideIObservableSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservableSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionSide):
                return Condition_IObservableBooleanIObservableSideSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionfloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservablefloat):
                return Condition_BooleanFloatIObservableFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservablefloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionfloat):
                return Condition_BooleanIObservableFloatFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionfloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionfloat):
                return Condition_IObservableBooleanFloatFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IObservableSide):
                return Condition_BooleanSideIObservableSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IObservableSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionSide):
                return Condition_BooleanIObservableSideSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IObservablebool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionSide):
                return Condition_IObservableBooleanSideSide(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionfloat):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionfloat):
                return Condition_BooleanFloatFloat(cond,ifpart,elsepart)
    if cond is None or rtti.can_be_casted(cond, IFunctionbool):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunctionSide):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunctionSide):
                return Condition_BooleanSideSide(cond,ifpart,elsepart)
    raise Exception('Cannot find suitable overload for Condition('+str(cond) +':'+ str(type(cond))+','+str(ifpart) +':'+ str(type(ifpart))+','+str(elsepart) +':'+ str(type(elsepart))+')')
