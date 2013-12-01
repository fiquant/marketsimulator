from marketsim import registry
from marketsim import IObservable
from marketsim import IFunction
from marketsim.ops._all import Observable
from marketsim.gen._out import const
from marketsim import context, event, registry, types, _


@registry.expose(['Basic', 'constant'])
class constant(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None):
        Observable[float].__init__(self)
        self.x = x if x is not None else 1.0
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : float
    }
    def __repr__(self):
        return "C=%x" % self.__dict__
    
    _internals = ['impl']
    @property
    def attributes(self):
        return {}
    
    def getImpl(self):
        return const(self.x)
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
