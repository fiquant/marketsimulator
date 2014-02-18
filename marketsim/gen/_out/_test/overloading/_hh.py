from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim import context
@registry.expose(["internal tests", "hh"])
class hh_(IFunctionfloat):
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
        return "hh" % self.__dict__
    
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
        from marketsim.gen._out._test.overloading._f import f_Float as __test_overloading_f_Float
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        return __test_overloading_f_Float(_constant_Float(12.2))
    
def hh(): 
    from marketsim import rtti
    return hh_()
    raise Exception('Cannot find suitable overload for hh('++')')
