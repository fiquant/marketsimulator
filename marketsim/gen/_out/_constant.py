from marketsim import registry
from marketsim import int
from marketsim import Function
from marketsim import context
@registry.expose(["Basic", "constant"])
class constant_Int(Function[int]):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import rtti
        self.x = x if x is not None else 1
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : int
    }
    def __repr__(self):
        return "C=%(x)s" % self.__dict__
    
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
        from marketsim.gen._out._const import const_Int as _const_Int
        return _const_Int(self.x)
    
from marketsim import registry
from marketsim import float
from marketsim import Function
from marketsim import context
@registry.expose(["Basic", "constant"])
class constant_Float(Function[float]):
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
        from marketsim.gen._out._const import const_Float as _const_Float
        return _const_Float(self.x)
    
def constant(x = None): 
    from marketsim import int
    from marketsim import float
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, int):
        return constant_Int(x)
    if x is None or rtti.can_be_casted(x, float):
        return constant_Float(x)
    raise Exception('Cannot find suitable overload for constant('+str(x)+')')
