from marketsim import registry
from marketsim.gen._intrinsic.observable.on_every_dt import _OnEveryDt_Impl
from marketsim import IFunction
@registry.expose(["Basic", "OnEveryDt"])
class OnEveryDt(_OnEveryDt_Impl):
    """ 
    """ 
    def __init__(self, dt = None, x = None):
        from marketsim.gen._out._constant import constant
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        self.dt = dt if dt is not None else 1.0
        self.x = x if x is not None else constant()
        _OnEveryDt_Impl.__init__(self)
        if isinstance(dt, types.IEvent):
            event.subscribe(self.dt, self.fire, self)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'dt' : float,
        'x' : IFunction
    }
    def __repr__(self):
        return "[%(x)s]_dt=%(dt)s" % self.__dict__
    
