from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import ISingleAssetTrader
from marketsim import context
@registry.expose(["Trader's", "RoughPnL"])
class RoughPnL(Observable[float]):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out.observable.trader._SingleProxy import SingleProxy as _observable_trader_SingleProxy
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.trader = trader if trader is not None else _observable_trader_SingleProxy()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : ISingleAssetTrader
    }
    def __repr__(self):
        return "RoughPnL(%(trader)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable._Observable import Observable as _observable_Observable
        from marketsim.gen._out.observable.trader._Balance import Balance as _observable_trader_Balance
        from marketsim.gen._out.observable.orderbook._NaiveCumulativePrice import NaiveCumulativePrice as _observable_orderbook_NaiveCumulativePrice
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader as _observable_orderbook_OfTrader
        from marketsim.gen._out.observable.trader._Position import Position as _observable_trader_Position
        return _observable_Observable(_observable_trader_Balance(self.trader)+_observable_orderbook_NaiveCumulativePrice(_observable_orderbook_OfTrader(self.trader),_observable_trader_Position(self.trader)))
        
        
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
