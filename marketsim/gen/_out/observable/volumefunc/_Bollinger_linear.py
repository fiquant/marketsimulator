from marketsim import registry
from marketsim import Volume
from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import ISingleAssetTrader
from marketsim import context
@registry.expose(["Volume function", "Bollinger_linear"])
class Bollinger_linear(Observable[Volume]):
    """ 
    """ 
    def __init__(self, alpha = None, k = None, trader = None):
        from marketsim import Volume
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const
        from marketsim.gen._out.observable.trader._SingleProxy import SingleProxy
        from marketsim import _
        from marketsim import event
        Observable[Volume].__init__(self)
        self.alpha = alpha if alpha is not None else 0.15
        self.k = k if k is not None else const(0.5)
        self.trader = trader if trader is not None else SingleProxy()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float,
        'k' : IObservable[float],
        'trader' : ISingleAssetTrader
    }
    def __repr__(self):
        return "Bollinger_linear(%(alpha)s, %(k)s, %(trader)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable.volumefunc._DesiredPosition import DesiredPosition
        from marketsim.gen._out.observable._OnEveryDt import OnEveryDt
        from marketsim.gen._out.observable.EW._RelStdDev import RelStdDev
        from marketsim.gen._out.observable.orderbook._MidPrice import MidPrice
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        return DesiredPosition(OnEveryDt(1.0,RelStdDev(MidPrice(OfTrader(self.trader)),self.alpha))*self.k,self.trader)
        
        
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
