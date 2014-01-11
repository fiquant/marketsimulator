from marketsim import registry
from marketsim.ops._function import Function
from marketsim.gen._out._const import const as _const
from marketsim import context
@registry.expose(["Basic", "constant"])
class constant(Function[float]):
    """ 
    """ 
    def __init__(self, x = None):
        self.x = x if x is not None else 1.0
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : float
    }
    def __repr__(self):
        return "C=%(x)s" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _const(self.x)
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
