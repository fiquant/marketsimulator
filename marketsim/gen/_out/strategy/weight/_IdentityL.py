from marketsim import registry
from marketsim import context
@registry.expose(["Strategy", "IdentityL"])
class IdentityL(object):
    """ 
    """ 
    def __init__(self, array = None):
        self.array = array if array is not None else []
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'array' : listOf(float)
    }
    def __repr__(self):
        return "IdentityL(%(array)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return self.array
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
