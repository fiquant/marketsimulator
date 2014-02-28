from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import context
@registry.expose(["internal tests", "F"])
class F_Float(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._test.in1.in2._intfunc import IntFunc_ as __test_in1_in2_IntFunc_
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(__test_in1_in2_IntFunc_())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionfloat
    }
    def __repr__(self):
        return "F(%(x)s)" % self.__dict__
    
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
    
def F(x = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        return F_Float(x)
    raise Exception('Cannot find suitable overload for F('+str(x) +':'+ str(type(x))+')')
