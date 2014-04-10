# generated with class generator.python.function$Import
from marketsim import registry
from marketsim import context
@registry.expose(["internal tests", "S1"])
class S1_String(str):
    """ 
    """ 
    def __init__(self, y = None):
        from marketsim import rtti
        self.y = y if y is not None else "abc"
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'y' : str
    }
    
    
    def __repr__(self):
        return "S1(%(y)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        
        self.impl.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        return self.y
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def S1(y = None): 
    from marketsim import rtti
    if y is None or rtti.can_be_casted(y, str):
        return S1_String(y)
    raise Exception('Cannot find suitable overload for S1('+str(y) +':'+ str(type(y))+')')
