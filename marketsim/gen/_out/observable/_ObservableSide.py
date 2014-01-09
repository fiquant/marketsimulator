from marketsim import registry
from marketsim.gen._intrinsic.observable.on_every_dt import _ObservableSide_Impl
from marketsim import IFunction
from marketsim import Side
@registry.expose(["Basic", "ObservableSide"])
class ObservableSide(_ObservableSide_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.side._Sell import Sell
        from marketsim import event
        from marketsim import types
        self.x = x if x is not None else Sell()
        _ObservableSide_Impl.__init__(self)
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[Side]
        
    }
    def __repr__(self):
        return "[%(x)s]" % self.__dict__
    
