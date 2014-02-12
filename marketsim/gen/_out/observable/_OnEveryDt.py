from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim.gen._intrinsic.observable.on_every_dt import _OnEveryDt_Impl
from marketsim import registry
from marketsim import float
@registry.expose(["Basic", "OnEveryDt"])
class OnEveryDt_FloatIFunctionFloat(Observable[float],_OnEveryDt_Impl):
    """ 
    """ 
    def __init__(self, dt = None, x = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        Observable[float].__init__(self)
        self.dt = dt if dt is not None else 1.0
        
        self.x = x if x is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
        _OnEveryDt_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'dt' : float,
        'x' : IFunction[float]
    }
    def __repr__(self):
        return "[%(x)s]_dt=%(dt)s" % self.__dict__
    
def OnEveryDt(dt = None,x = None): 
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if dt is None or rtti.can_be_casted(dt, float):
        if x is None or rtti.can_be_casted(x, IFunction[float]):
            return OnEveryDt_FloatIFunctionFloat(dt,x)
    raise Exception('Cannot find suitable overload for OnEveryDt('+str(dt)+','+str(x)+')')
