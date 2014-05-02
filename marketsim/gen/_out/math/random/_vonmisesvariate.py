# generated with class generator.python.random$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Random", "vonmisesvariate"])
class vonmisesvariate_FloatFloat(IFunctionfloat):
    """ **Von Mises distribution**
    
    
    Parameters are:
    
    **Mu**
    	 |mu| is the mean angle, expressed in radians between 0 and 2|pi|
    
    **Kappa**
    	 |kappa| is the concentration parameter, which must be greater than or equal to zero.
    	      If |kappa| is equal to zero, this distribution reduces
    	      to a uniform random angle over the range 0 to 2|pi|        
    """ 
    def __init__(self, Mu = None, Kappa = None):
        self.Mu = Mu if Mu is not None else 0.0
        self.Kappa = Kappa if Kappa is not None else 0.0
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Mu' : float,
        'Kappa' : float
    }
    
    
    
    
    def __repr__(self):
        return "vonmisesvariate(%(Mu)s, %(Kappa)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
    
    def typecheck(self):
        from marketsim import rtti
        rtti.typecheck(float, self.Mu)
        rtti.typecheck(float, self.Kappa)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, *args, **kwargs):
        import random
        return random.vonmisesvariate(self.Mu, self.Kappa)
    
    def _casts_to(self, dst):
        return vonmisesvariate_FloatFloat._types[0]._casts_to(dst)
    
def vonmisesvariate(Mu = None,Kappa = None): 
    from marketsim import rtti
    if Mu is None or rtti.can_be_casted(Mu, float):
        if Kappa is None or rtti.can_be_casted(Kappa, float):
            return vonmisesvariate_FloatFloat(Mu,Kappa)
    raise Exception('Cannot find suitable overload for vonmisesvariate('+str(Mu) +':'+ str(type(Mu))+','+str(Kappa) +':'+ str(type(Kappa))+')')
