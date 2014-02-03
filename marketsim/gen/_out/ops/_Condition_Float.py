from marketsim import registry
from marketsim.gen._intrinsic.ops import _ConditionFloat_Impl
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IFunction
@registry.expose(["Ops", "Condition_Float"])
class Condition_Float(_ConditionFloat_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out._true import true as _true
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        self.cond = cond if cond is not None else _true()
        self.ifpart = ifpart if ifpart is not None else _constant(1.0)
        self.elsepart = elsepart if elsepart is not None else _constant(1.0)
        rtti.check_fields(self)
        _ConditionFloat_Impl.__init__(self)
        if isinstance(cond, types.IEvent):
            event.subscribe(self.cond, self.fire, self)
        if isinstance(ifpart, types.IEvent):
            event.subscribe(self.ifpart, self.fire, self)
        if isinstance(elsepart, types.IEvent):
            event.subscribe(self.elsepart, self.fire, self)
    
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
    
