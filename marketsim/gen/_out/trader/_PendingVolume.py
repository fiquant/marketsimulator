from marketsim.ops._all import Observable
from marketsim import Volume
from marketsim import IAccount
from marketsim import registry
from marketsim.gen._intrinsic.trader.props import PendingVolume_Impl
@registry.expose(["Trader", "PendingVolume"])
class PendingVolume_Optional__IAccount_(Observable[Volume],PendingVolume_Impl):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import Volume
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim import event
        Observable[Volume].__init__(self)
        self.trader = trader if trader is not None else _trader_SingleProxy()
        if isinstance(trader, types.IEvent):
            event.subscribe(self.trader, self.fire, self)
        rtti.check_fields(self)
        PendingVolume_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    def __repr__(self):
        return "PendingVolume(%(trader)s)" % self.__dict__
    
def PendingVolume(trader = None): 
    return PendingVolume_Optional__IAccount_(trader)
