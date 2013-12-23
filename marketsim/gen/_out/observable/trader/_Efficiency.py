from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import ISingleAssetTrader
from marketsim import context
@registry.expose(["Trader's", "Efficiency"])
class Efficiency(Observable[float]):
    """ 
    """ 
    def __init__(self, trader = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out.observable.trader._SingleProxy import SingleProxy
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.trader = trader if trader is not None else SingleProxy()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : ISingleAssetTrader
    }
    def __repr__(self):
        return "Efficiency_{%(trader)s}" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable._Observable import Observable
        from marketsim.gen._out.observable.trader._Balance import Balance
        from marketsim.gen._out.observable.orderbook._CumulativePrice import CumulativePrice
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        from marketsim.gen._out.observable.trader._Position import Position
        return Observable(Balance(self.trader)+CumulativePrice(OfTrader(self.trader),Position(self.trader)))
        
        
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
