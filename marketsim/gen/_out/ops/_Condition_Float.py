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
        from marketsim.gen._out._true import true_ as _true
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim import float
        Observable[float].__init__(self)
        self.cond = cond if cond is not None else _true()
        if isinstance(cond, types.IEvent):
            event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _constant(1.0)
        if isinstance(ifpart, types.IEvent):
            event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _constant(1.0)
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
    from marketsim import IFunction
    from marketsim import bool
    from marketsim import float
    from marketsim import rtti
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunction[float]):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunction[float]):
                return Condition_Float_IFunctionBooleanIFunctionFloatIFunctionFloat(cond,ifpart,elsepart)
    raise Exception('Cannot find suitable overload for Condition_Float('+str(cond)+','+str(ifpart)+','+str(elsepart)+')')
