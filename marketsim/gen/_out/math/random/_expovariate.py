from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Random", "expovariate"])
class expovariate_Float(IFunctionfloat):
    """ 
      Returned values range from 0 to positive infinity
    """ 
    def __init__(self, Lambda = None):
        from marketsim import rtti
        self.Lambda = Lambda if Lambda is not None else 1.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Lambda' : float
    }
    def __repr__(self):
        return "expovariate(%(Lambda)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
    def __call__(self, *args, **kwargs):
        import random
        return random.expovariate(self.Lambda)
    
    def _casts_to(self, dst):
        return expovariate_Float._types[0]._casts_to(dst)
    
def expovariate(Lambda = None): 
    from marketsim import rtti
    if Lambda is None or rtti.can_be_casted(Lambda, float):
        return expovariate_Float(Lambda)
    raise Exception('Cannot find suitable overload for expovariate('+str(Lambda) +':'+ str(type(Lambda))+')')
