from marketsim import registry
from marketsim import int
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic._constant import _Constant_Impl
@registry.expose(["Basic", "const"])
class const_Int(Observable[int],_Constant_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import event
        from marketsim import int
        Observable[int].__init__(self)
        self.x = x if x is not None else 1
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        rtti.check_fields(self)
        _Constant_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : int
    }
    def __repr__(self):
        return "C=%(x)s" % self.__dict__
    
from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic._constant import _Constant_Impl
@registry.expose(["Basic", "const"])
class const_Float(Observable[float],_Constant_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else 1.0
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        rtti.check_fields(self)
        _Constant_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : float
    }
    def __repr__(self):
        return "C=%(x)s" % self.__dict__
    
def const(x = None): 
    from marketsim import int
    from marketsim import float
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, int):
        return const_Int(x)
    if x is None or rtti.can_be_casted(x, float):
        return const_Float(x)
    raise Exception('Cannot find suitable overload for const('+str(x)+')')
