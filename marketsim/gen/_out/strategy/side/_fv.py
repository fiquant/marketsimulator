# generated with class generator.python.accessor$Import
from marketsim import registry
from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
@registry.expose(["-", "Fv"])
class Fv_strategysideFundamentalValue(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_Float as _strategy_side_FundamentalValue_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_FundamentalValue_Float())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : FundamentalValue
    }
    
    
    def __repr__(self):
        return "Fv(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    @property
    def dereference(self):
        return self.x.fv
    
def Fv(x = None): 
    from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, FundamentalValue):
        return Fv_strategysideFundamentalValue(x)
    raise Exception('Cannot find suitable overload for Fv('+str(x) +':'+ str(type(x))+')')
