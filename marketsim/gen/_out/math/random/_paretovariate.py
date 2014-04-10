# generated with class generator.python.random$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Random", "paretovariate"])
class paretovariate_Float(IFunctionfloat):
    """ **Pareto distribution**
    
    
    Parameters are:
    
    **Alpha**
    	 |alpha| is the shape parameter
    """ 
    def __init__(self, Alpha = None):
        from marketsim import rtti
        self.Alpha = Alpha if Alpha is not None else 1.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Alpha' : float
    }
    
    
    def __repr__(self):
        return "paretovariate(%(Alpha)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
    def __call__(self, *args, **kwargs):
        import random
        return random.paretovariate(self.Alpha)
    
    def _casts_to(self, dst):
        return paretovariate_Float._types[0]._casts_to(dst)
    
def paretovariate(Alpha = None): 
    from marketsim import rtti
    if Alpha is None or rtti.can_be_casted(Alpha, float):
        return paretovariate_Float(Alpha)
    raise Exception('Cannot find suitable overload for paretovariate('+str(Alpha) +':'+ str(type(Alpha))+')')
