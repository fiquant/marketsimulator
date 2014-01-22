from marketsim import registry
from marketsim.gen._intrinsic.observable.on_every_dt import _Observable_Impl
from marketsim import IFunction
@registry.expose(["Basic", "Volume"])
class Volume(_Observable_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._const import const as _const
        from marketsim import rtti
        from marketsim import event
        from marketsim import types
        self.x = x if x is not None else _const()
        rtti.check_fields(self)
        _Observable_Impl.__init__(self)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float]
    }
    def __repr__(self):
        return "[%(x)s]" % self.__dict__
    
