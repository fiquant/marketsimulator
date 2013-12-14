from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import float
from marketsim import context
@registry.expose(["RSI", "DownMovements"])
class DownMovements(Observable[float]):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out.observable.orderbook._MidPrice import MidPrice
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.source = source if source is not None else MidPrice()
        self.timeframe = timeframe if timeframe is not None else 10.0
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable,
        'timeframe' : float
    }
    def __repr__(self):
        return "Downs_{%(timeframe)s}(%(source)s)" % self.__dict__
    
    _internals = ['impl']
    @property
    def attributes(self):
        return {}
    
    def getImpl(self):
        from marketsim.gen._out.observable._Max import Max
        from marketsim.gen._out._const import const
        from marketsim.gen._out.observable._Lagged import Lagged
        return Max(const(0.0),Lagged(self.source,self.timeframe)-self.source)
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
