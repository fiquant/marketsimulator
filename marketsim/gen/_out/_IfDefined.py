from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IFunction
from marketsim import context
@registry.expose(["Basic", "IfDefined"])
class IfDefined(Observable[float]):
    """ 
    """ 
    def __init__(self, x = None, elsePart = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.x = x if x is not None else _constant()
        self.elsePart = elsePart if elsePart is not None else _constant()
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunction[float],
        'elsePart' : IFunction[float]
    }
    def __repr__(self):
        return "If def(%(x)s) else %(elsePart)s" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out._null import null as _null
        return (self.x<>_null())[self.x, self.elsePart]
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
