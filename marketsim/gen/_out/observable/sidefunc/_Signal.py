from marketsim import registry
from marketsim import Side
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import context
@registry.expose(["Side function", "Signal"])
class Signal(Observable[Side]):
    """ 
    """ 
    def __init__(self, signal = None, threshold = None):
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant
        from marketsim import _
        from marketsim import event
        Observable[Side].__init__(self)
        self.signal = signal if signal is not None else constant()
        self.threshold = threshold if threshold is not None else 0.7
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'signal' : IFunction,
        'threshold' : float
    }
    def __repr__(self):
        return "SignalSide_{%(threshold)s}(%(signal)s)" % self.__dict__
    
    _internals = ['impl']
    @property
    def attributes(self):
        return {}
    
    def getImpl(self):
        from marketsim.gen._out.side._Buy import Buy
        from marketsim.gen._out.side._Sell import Sell
        from marketsim.gen._out.side._Nothing import Nothing
        from marketsim.gen._out._const import const
        from marketsim.gen._out._const import const
        return (self.signal>const(self.threshold))[Buy(), (self.signal<const(0.0-self.threshold))[Sell(), Nothing()]]
        
        
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
