from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.observable.on_every_dt import _Observable_Impl
from marketsim import IFunction
from marketsim import registry
from marketsim import float
@registry.expose(["Basic", "Float"])
class Float_IFunctionFloat(Observable[float],_Observable_Impl):
    """  Needed since generic functions aren't implemented yet
    """ 
    def __init__(self, x = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.x = x if x is not None else _const_Float(1.0)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        rtti.check_fields(self)
        _Observable_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float]
    }
    def __repr__(self):
        return "[%(x)s]" % self.__dict__
    
def Float(x = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IFunction[float]):
        return Float_IFunctionFloat(x)
    raise Exception('Cannot find suitable overload for Float('+str(x)+')')
