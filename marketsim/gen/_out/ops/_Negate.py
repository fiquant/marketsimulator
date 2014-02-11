from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import registry
from marketsim.gen._intrinsic.ops import _Negate_Impl
from marketsim import float
@registry.expose(["Ops", "Negate"])
class Negate_IObservableFloat(Observable[float],_Negate_Impl):
    """ 
    """ 
    def __init__(self, x = None):
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
        rtti.check_fields(self)
        _Negate_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float]
    }
    def __repr__(self):
        return "-%(x)s" % self.__dict__
    
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import registry
from marketsim.gen._intrinsic.ops import _Negate_Impl
from marketsim import float
@registry.expose(["Ops", "Negate"])
class Negate_IFunctionFloat(Observable[float],_Negate_Impl):
    """ 
    """ 
    def __init__(self, x = None):
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
        rtti.check_fields(self)
        _Negate_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float]
    }
    def __repr__(self):
        return "-%(x)s" % self.__dict__
    
def Negate(x = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservable[float]):
        return Negate_IObservableFloat(x)
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        return Negate_IFunctionFloat(x)
    raise Exception('Cannot find suitable overload for Negate('+str(x)+')')
