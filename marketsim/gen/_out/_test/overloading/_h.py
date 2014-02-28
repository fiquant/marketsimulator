from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionint import IFunctionint
from marketsim import context
@registry.expose(["internal tests", "h"])
class h_(IFunctionint):
    """ 
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "h" % self.__dict__
    
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
        from marketsim.gen._out._constant import constant_Int as _constant_Int
        from marketsim import call
        return call(__test_overloading_f_Int,call(_constant_Int,12))
    
def h(): 
    from marketsim import rtti
    return h_()
    raise Exception('Cannot find suitable overload for h('++')')
