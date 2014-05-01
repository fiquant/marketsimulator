# generated with class generator.python.random$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Random", "uniform"])
class uniform_FloatFloat(IFunctionfloat):
    """ **Uniform distribution**
    
    
     Return a random floating point number *N* such that
     *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
     The end-point value *b* may or may not be included in the range depending on
     floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
    
    Parameters are:
    
    **Low**
    
    **High**
    """ 
    def __init__(self, Low = None, High = None):
        from marketsim import rtti
        self.Low = Low if Low is not None else -10.0
        self.High = High if High is not None else 10.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Low' : float,
        'High' : float
    }
    
    
    
    
    def __repr__(self):
        return "uniform(%(Low)s, %(High)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, *args, **kwargs):
        import random
        return random.uniform(self.Low, self.High)
    
    def _casts_to(self, dst):
        return uniform_FloatFloat._types[0]._casts_to(dst)
    
def uniform(Low = None,High = None): 
    from marketsim import rtti
    if Low is None or rtti.can_be_casted(Low, float):
        if High is None or rtti.can_be_casted(High, float):
            return uniform_FloatFloat(Low,High)
    raise Exception('Cannot find suitable overload for uniform('+str(Low) +':'+ str(type(Low))+','+str(High) +':'+ str(type(High))+')')
