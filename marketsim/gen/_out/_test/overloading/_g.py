# generated with class generator.python.function$Import
from marketsim.gen._out._ifunction._ifunctionint import IFunctionint
from marketsim import context

class g_Int(IFunctionint):
    """ 
    """ 
    def __init__(self, x ):
        from marketsim import rtti
        self.x = x
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionint
    }
    
    
    def __repr__(self):
        return "g(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        self.x.bind_ex(self._ctx_ex)
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
        from marketsim.gen._out._test.overloading._f import f_Int as __test_overloading_f_Int
        from marketsim import deref_opt
        return deref_opt(__test_overloading_f_Int(self.x))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def g(x = None): 
    from marketsim.gen._out._ifunction._ifunctionint import IFunctionint
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IFunctionint):
        return g_Int(x)
    raise Exception('Cannot find suitable overload for g('+str(x) +':'+ str(type(x))+')')
