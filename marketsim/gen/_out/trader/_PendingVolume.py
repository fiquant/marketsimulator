from marketsim import registry
from marketsim.gen._intrinsic.trader.props import PendingVolume_Impl
from marketsim import IAccount
@registry.expose(["Trader", "PendingVolume"])
class PendingVolume_Optional__IAccount_(PendingVolume_Impl):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
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
    
PendingVolume = PendingVolume_Optional__IAccount_
