from marketsim import ISingleAssetTrader
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import Volume
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Volume function", "DesiredPosition"])
class DesiredPosition_Optional__IObservable__Float____Optional__ISingleAssetTrader_(Observable[Volume]):
    """ 
    """ 
    def __init__(self, desiredPosition = None, trader = None):
        from marketsim.gen._out._const import const as _const
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim import Volume
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim import event
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
        from marketsim.gen._out.observable._Volume import Volume as _observable_Volume
        from marketsim.gen._out.ops._Sub import Sub as _ops_Sub
        from marketsim.gen._out.trader._Position import Position as _trader_Position
        from marketsim.gen._out.trader._PendingVolume import PendingVolume as _trader_PendingVolume
        return _observable_Volume(_ops_Sub(_ops_Sub(self.desiredPosition,_trader_Position(self.trader)),_trader_PendingVolume(self.trader)))
    
def DesiredPosition(desiredPosition = None,trader = None): 
    return DesiredPosition_Optional__IObservable__Float____Optional__ISingleAssetTrader_(desiredPosition,trader)
