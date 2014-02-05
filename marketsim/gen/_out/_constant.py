from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim import float
from marketsim import context
@registry.expose(["Basic", "constant"])
class constant_Optional__Float_(Function[float]):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import rtti
        self.x = x if x is not None else 1.0
        rtti.check_fields(self)
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
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out._const import const as _const
        return _const(self.x)
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
constant = constant_Optional__Float_
