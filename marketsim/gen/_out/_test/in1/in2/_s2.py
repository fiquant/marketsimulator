from marketsim import registry
from marketsim import context
@registry.expose(["internal tests", "S2"])
class S2_(str):
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
        return "S2" % self.__dict__
    
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
        from marketsim.gen._out._test.in1.in2._s1 import S1_String as __test_in1_in2_S1_String
        from marketsim import call
        return call(__test_in1_in2_S1_String,)
    
def S2(): 
    from marketsim import rtti
    return S2_()
    raise Exception('Cannot find suitable overload for S2('++')')
