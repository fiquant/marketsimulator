from marketsim import ISingleAssetTrader
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import Volume
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Volume function", "DesiredPosition"])
class DesiredPosition_IObservableFloatISingleAssetTrader(Observable[Volume]):
    """ 
    """ 
    def __init__(self, desiredPosition = None, trader = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim.gen._out._const import const_Float as _const
        from marketsim import rtti
        from marketsim import Volume
        from marketsim import event
        from marketsim.gen._out.trader._singleproxy import SingleProxy_ as _trader_SingleProxy
        Observable[Volume].__init__(self)
        self.desiredPosition = desiredPosition if desiredPosition is not None else _const()
        self.trader = trader if trader is not None else _trader_SingleProxy()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'desiredPosition' : IObservable[float],
        'trader' : ISingleAssetTrader
    }
    def __repr__(self):
        return "DesiredPosition(%(desiredPosition)s, %(trader)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.observable._volume import Volume_IFunctionFloat as _observable_Volume
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatIObservableFloat as _ops_Sub
        from marketsim.gen._out.trader._position import Position_IAccount as _trader_Position
        from marketsim.gen._out.trader._pendingvolume import PendingVolume_IAccount as _trader_PendingVolume
        return _observable_Volume(_ops_Sub(_ops_Sub(self.desiredPosition,_trader_Position(self.trader)),_trader_PendingVolume(self.trader)))
    
def DesiredPosition(desiredPosition = None,trader = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import ISingleAssetTrader
    from marketsim import rtti
    if desiredPosition is None or rtti.can_be_casted(desiredPosition, IObservable[float]):
        if trader is None or rtti.can_be_casted(trader, ISingleAssetTrader):
            return DesiredPosition_IObservableFloatISingleAssetTrader(desiredPosition,trader)
    raise Exception("Cannot find suitable overload")
