from marketsim.gen._out._ifunction._ifunctionint import IFunctionint
from marketsim import context

class f_Int(IFunctionint):
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
        return "f(%(x)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
        return self.x
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import context

class f_Float(IFunctionfloat):
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
        'x' : IFunctionfloat
    }
    def __repr__(self):
        return "f(%(x)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
        return self.x
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def f(x = None): 
    from marketsim.gen._out._ifunction._ifunctionint import IFunctionint
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IFunctionint):
        return f_Int(x)
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        return f_Float(x)
    raise Exception('Cannot find suitable overload for f('+str(x) +':'+ str(type(x))+')')
