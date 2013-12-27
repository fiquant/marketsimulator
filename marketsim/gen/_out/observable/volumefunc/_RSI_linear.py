from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import ISingleAssetTrader
from marketsim import context
@registry.expose(["Volume function", "RSI_linear"])
class RSI_linear(Observable[float]):
    """ 
    """ 
    def __init__(self, alpha = None, k = None, timeframe = None, trader = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const
        from marketsim.gen._out.observable.trader._SingleProxy import SingleProxy
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.alpha = alpha if alpha is not None else 1.0/14.0
        self.k = k if k is not None else const(-0.04)
        self.timeframe = timeframe if timeframe is not None else 1.0
        self.trader = trader if trader is not None else SingleProxy()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float,
        'k' : IObservable[float],
        'timeframe' : float,
        'trader' : ISingleAssetTrader
    }
    def __repr__(self):
        return "RSI_{%(trader)s}(%(alpha)s, %(timeframe)s)*%(k)s" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable.volumefunc._DesiredPosition import DesiredPosition
        from marketsim.gen._out.observable._OnEveryDt import OnEveryDt
        from marketsim.gen._out._const import const
        from marketsim.gen._out.observable._RSI import RSI
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        return DesiredPosition(OnEveryDt(1.0,const(50.0)-RSI(OfTrader(self.trader),self.timeframe,self.alpha))*self.k,self.trader)
        
        
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
