from marketsim.gen._intrinsic.ops import _Condition_Impl
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import Side
from marketsim import registry
from marketsim import bool
@registry.expose(["Ops", "Condition_Side"])
class Condition_Side_IFunctionBooleanSideSide(Observable[Side],_Condition_Impl):
    """ 
    """ 
    def __init__(self, cond = None, ifpart = None, elsepart = None):
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim import types
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._true import true as _true
        from marketsim import event
        from marketsim.gen._out.side._Buy import Buy as _side_Buy
        Observable[Side].__init__(self)
        self.cond = cond if cond is not None else _true()
        if isinstance(cond, types.IEvent):
            event.subscribe(self.cond, self.fire, self)
        self.ifpart = ifpart if ifpart is not None else _side_Sell()
        if isinstance(ifpart, types.IEvent):
            event.subscribe(self.ifpart, self.fire, self)
        self.elsepart = elsepart if elsepart is not None else _side_Buy()
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
    
def Condition_Side(cond = None,ifpart = None,elsepart = None): 
    from marketsim import IFunction
    from marketsim import bool
    from marketsim import Side
    from marketsim import rtti
    if cond is None or rtti.can_be_casted(cond, IFunction[bool]):
        if ifpart is None or rtti.can_be_casted(ifpart, IFunction[Side]):
            if elsepart is None or rtti.can_be_casted(elsepart, IFunction[Side]):
                return Condition_Side_IFunctionBooleanSideSide(cond,ifpart,elsepart)
    raise Exception("Cannot find suitable overload")
