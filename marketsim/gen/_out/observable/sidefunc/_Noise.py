from marketsim import registry
from marketsim import Side
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import context
@registry.expose(["Side function", "Noise"])
class Noise(Observable[Side]):
    """ 
    """ 
    def __init__(self, side_distribution = None):
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim.gen._out.mathutils.rnd._uniform import uniform
        from marketsim import _
        from marketsim import event
        Observable[Side].__init__(self)
        self.side_distribution = side_distribution if side_distribution is not None else uniform(0.0,1.0)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side_distribution' : IFunction
    }
    def __repr__(self):
        return "Noise_{%(side_distribution)s}" % self.__dict__
    
    _internals = ['impl']
    @property
    def attributes(self):
        return {}
    
    def getImpl(self):
        from marketsim.gen._out.side._Sell import Sell
        from marketsim.gen._out.side._Buy import Buy
        from marketsim.gen._out._const import const
        return (self.side_distribution>const(0.5))[Sell(), Buy()]
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
