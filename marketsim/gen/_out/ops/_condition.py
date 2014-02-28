from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableFloatIObservableFloat(Observablefloat,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else deref_opt(_const_Float(1.0))
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else deref_opt(_const_Float(1.0))
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
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim import registry
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableSideIObservableSide(ObservableSide,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import rtti
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._side import Side
        from marketsim import event
        from marketsim.gen._out.side._observablebuy import observableBuy_ as _side_observableBuy_
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_observableSell_())
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_observableBuy_())
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
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableFloatIObservableFloat(Observablefloat,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        
        self.ifpart = ifpart if ifpart is not None else deref_opt(_const_Float(1.0))
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else deref_opt(_const_Float(1.0))
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
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanFloatIObservableFloat(Observablefloat,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else deref_opt(_constant_Float(1.0))
        
        self.elsepart = elsepart if elsepart is not None else deref_opt(_const_Float(1.0))
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
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableFloatFloat(Observablefloat,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else deref_opt(_const_Float(1.0))
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else deref_opt(_constant_Float(1.0))
        
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
from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim import registry
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableSideIObservableSide(ObservableSide,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import rtti
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._true import true_ as _true_
        from marketsim import event
        from marketsim.gen._out.side._observablebuy import observableBuy_ as _side_observableBuy_
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_observableSell_())
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_observableBuy_())
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
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim import registry
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanSideIObservableSide(ObservableSide,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import rtti
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._side import Side
        from marketsim import event
        from marketsim.gen._out.side._observablebuy import observableBuy_ as _side_observableBuy_
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_Sell_())
        
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_observableBuy_())
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
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim import registry
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanIObservableSideSide(ObservableSide,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import rtti
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._side import Side
        from marketsim import event
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_observableSell_())
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_Buy_())
        
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
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
@registry.expose(["Ops", "Condition"])
class Condition_BooleanFloatIObservableFloat(Observablefloat,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        
        self.ifpart = ifpart if ifpart is not None else deref_opt(_constant_Float(1.0))
        
        self.elsepart = elsepart if elsepart is not None else deref_opt(_const_Float(1.0))
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
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableFloatFloat(Observablefloat,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._true import true_ as _true_
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        
        self.ifpart = ifpart if ifpart is not None else deref_opt(_const_Float(1.0))
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else deref_opt(_constant_Float(1.0))
        
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
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanFloatFloat(Observablefloat,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else deref_opt(_constant_Float(1.0))
        
        self.elsepart = elsepart if elsepart is not None else deref_opt(_constant_Float(1.0))
        
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
from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim import registry
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Ops", "Condition"])
class Condition_BooleanSideIObservableSide(ObservableSide,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import rtti
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._true import true_ as _true_
        from marketsim import event
        from marketsim.gen._out.side._observablebuy import observableBuy_ as _side_observableBuy_
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_Sell_())
        
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_observableBuy_())
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
from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim import registry
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Ops", "Condition"])
class Condition_BooleanIObservableSideSide(ObservableSide,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import rtti
        from marketsim.gen._out.side._observablesell import observableSell_ as _side_observableSell_
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._true import true_ as _true_
        from marketsim import event
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_observableSell_())
        event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_Buy_())
        
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
from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim import registry
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Ops", "Condition"])
class Condition_IObservableBooleanSideSide(ObservableSide,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import rtti
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._observabletrue import observableTrue_ as _observableTrue_
        from marketsim.gen._out._side import Side
        from marketsim import event
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_observableTrue_())
        event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_Sell_())
        
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_Buy_())
        
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
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
@registry.expose(["Ops", "Condition"])
class Condition_BooleanFloatFloat(Observablefloat,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out._true import true_ as _true_
        Observablefloat.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        
        self.ifpart = ifpart if ifpart is not None else deref_opt(_constant_Float(1.0))
        
        self.elsepart = elsepart if elsepart is not None else deref_opt(_constant_Float(1.0))
        
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
from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim import registry
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Ops", "Condition"])
class Condition_BooleanSideSide(ObservableSide,_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim import deref_opt
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import rtti
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._true import true_ as _true_
        ObservableSide.__init__(self)
        self.cond = cond if cond is not None else deref_opt(_true_())
        
        self.ifpart = ifpart if ifpart is not None else deref_opt(_side_Sell_())
        
        self.elsepart = elsepart if elsepart is not None else deref_opt(_side_Buy_())
        
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
    from marketsim.gen._out._iobservable._iobservableside import IObservableSide
    from marketsim import rtti
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out._side import Side
    from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
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
