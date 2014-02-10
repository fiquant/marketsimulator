from marketsim.gen._intrinsic.observable.on_every_dt import _ObservableSide_Impl
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import Side
from marketsim import registry
@registry.expose(["Basic", "Side"])
class Side_IFunctionSide(Observable[Side],_ObservableSide_Impl):
    """  Needed since generic functions aren't implemented yet
    """ 
    def __init__(self, x = None):
        from marketsim import types
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell
        from marketsim import event
        Observable[Side].__init__(self)
        self.x = x if x is not None else _side_Sell()
        if isinstance(x, types.IEvent):
            event.subscribe(self.x, self.fire, self)
        rtti.check_fields(self)
        _ObservableSide_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[Side]
    }
    def __repr__(self):
        return "[%(x)s]" % self.__dict__
    
def Side(x = None): 
    from marketsim import IFunction
    from marketsim import Side
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IFunction[Side]):
        return Side_IFunctionSide(x)
    raise Exception("Cannot find suitable overload")
