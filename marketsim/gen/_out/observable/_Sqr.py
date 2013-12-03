from marketsim import registry
from marketsim.gen._out import constant
from marketsim import IObservable
from marketsim import IFunction
from marketsim.ops._all import Observable
from marketsim import context, event, registry, types, _


@registry.expose(['Pow/Log', 'Sqr'])
class Sqr(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None):
        Observable[float].__init__(self)
        self.x = x if x is not None else constant()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction
    }
    def __repr__(self):
        return "{%(x)s}^2" % self.__dict__
    
    _internals = ['impl']
    @property
    def attributes(self):
        return {}
    
    def getImpl(self):
        return self.x*self.x
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
