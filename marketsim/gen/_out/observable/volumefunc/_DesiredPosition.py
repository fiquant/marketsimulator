from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import ISingleAssetTrader
from marketsim import context
@registry.expose(["Volume function", "DesiredPosition"])
class DesiredPosition(Observable[float]):
    """ 
    """ 
    def __init__(self, desiredPosition = None, trader = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const
        from marketsim.gen._out.observable.trader._SingleProxy import SingleProxy
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.desiredPosition = desiredPosition if desiredPosition is not None else const()
        self.trader = trader if trader is not None else SingleProxy()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'desiredPosition' : IObservable,
        'trader' : ISingleAssetTrader
    }
    def __repr__(self):
        return "Dp_{%(trader)s}(%(desiredPosition)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable.trader._Position import Position
        from marketsim.gen._out.observable.trader._PendingVolume import PendingVolume
        return self.desiredPosition-Position(self.trader)-PendingVolume(self.trader)
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
