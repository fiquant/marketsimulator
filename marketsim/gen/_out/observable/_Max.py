from marketsim import IObservable, IFunction, context, event, ops, registry, types, _
from marketsim.ops import constant


@registry.expose(['Basic', 'Max'])
class Max(ops.Observable[float]):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        ops.Observable[float].__init__(self)
        self.x = x if x is not None else constant()
        self.y = y if y is not None else constant()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction,
        'y' : IFunction
    }
    def __repr__(self):
        return "max{%x, %y}" % self.__dict__
    
    _internals = ['impl']
    @property
    def attributes(self):
        return {}
    
    def getImpl(self):
        return (self.x>self.y)[self.x, self.y]
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
