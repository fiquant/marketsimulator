def identityF(): 
    from marketsim.gen._out.strategy.weight.f._f_identityf import f_IdentityF_ as _strategy_weight_f_f_IdentityF_
    from marketsim import rtti
    return _strategy_weight_f_f_IdentityF_()
    raise Exception('Cannot find suitable overload for identityF('++')')
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import context
@registry.expose(["Strategy", "IdentityF"])
class IdentityF_Float(IFunctionfloat):
    """ **identity scaling = f(x)**
    
    
    Parameters are:
    
    **f**
    """ 
    def __init__(self, f = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.f = f if f is not None else deref_opt(_constant_Float(1.0))
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'f' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "IdentityF(%(f)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
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
        return self.f
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def IdentityF(f = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if f is None or rtti.can_be_casted(f, IFunctionfloat):
        return IdentityF_Float(f)
    raise Exception('Cannot find suitable overload for IdentityF('+str(f) +':'+ str(type(f))+')')
