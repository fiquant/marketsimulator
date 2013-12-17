from marketsim import registry
from marketsim.gen._intrinsic.trader.props import PendingVolume_Impl
from marketsim import ISingleAssetTrader
@registry.expose(["Trader's", "PendingVolume"])
class PendingVolume(PendingVolume_Impl):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim.gen._out.observable.trader._SingleProxy import SingleProxy
        from marketsim import event
        from marketsim import types
        self.trader = trader if trader is not None else SingleProxy()
        PendingVolume_Impl.__init__(self)
        if isinstance(trader, types.IEvent):
            event.subscribe(self.trader, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : ISingleAssetTrader
    }
    def __repr__(self):
        return "PendingVolume_{%(trader)s}" % self.__dict__
    
