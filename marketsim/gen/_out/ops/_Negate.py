from marketsim import registry
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.ops import _Negate_Impl
from marketsim.gen._out._iobservable import IObservablefloat
@registry.expose(["Ops", "Negate"])
class Negate_IObservableFloat(Observable[float],_Negate_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import rtti
        Observable[float].__init__(self)
        self.x = x if x is not None else _const_Float(1.0)
        event.subscribe(self.x, self.fire, self)
        rtti.check_fields(self)
        _Negate_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat
    }
    def __repr__(self):
        return "-%(x)s" % self.__dict__
    
from marketsim import registry
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.ops import _Negate_Impl
from marketsim.gen._out._ifunction import IFunctionfloat
@registry.expose(["Ops", "Negate"])
class Negate_Float(Observable[float],_Negate_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        Observable[float].__init__(self)
        self.x = x if x is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
        _Negate_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionfloat
    }
    def __repr__(self):
        return "-%(x)s" % self.__dict__
    
def Negate(x = None): 
    from marketsim.gen._out._iobservable import IObservablefloat
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        return Negate_IObservableFloat(x)
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        return Negate_Float(x)
    raise Exception('Cannot find suitable overload for Negate('+str(x) +':'+ str(type(x))+')')
