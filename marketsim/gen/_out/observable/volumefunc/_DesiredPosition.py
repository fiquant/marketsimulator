from marketsim import registry
from marketsim import Volume
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import ISingleAssetTrader
from marketsim import context
@registry.expose(["Volume function", "DesiredPosition"])
class DesiredPosition(Observable[Volume]):
    """ 
    """ 
    def __init__(self, desiredPosition = None, trader = None):
        from marketsim import Volume
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.trader._SingleProxy import SingleProxy as _trader_SingleProxy
        from marketsim import _
        from marketsim import event
        Observable[Volume].__init__(self)
        self.desiredPosition = desiredPosition if desiredPosition is not None else _const()
        self.trader = trader if trader is not None else _trader_SingleProxy()
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
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out._ObservableVolume import ObservableVolume as _ObservableVolume
        from marketsim.gen._out.trader._Position import Position as _trader_Position
        from marketsim.gen._out.trader._PendingVolume import PendingVolume as _trader_PendingVolume
        return _ObservableVolume(self.desiredPosition-_trader_Position(self.trader)-_trader_PendingVolume(self.trader))
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
