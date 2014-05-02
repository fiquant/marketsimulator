# generated with class generator.python.constructor$Import
from marketsim import registry
from marketsim.gen._out.math._istatdomain import IStatDomain
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["-", "Cumulative"])
class Cumulative_IObservableFloat(IStatDomain):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        self.source = source if source is not None else deref_opt(_const_Float(0.0))
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat
    }
    
    
    def __repr__(self):
        return "Cumulative(%(source)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.source.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.source.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
        rtti.typecheck(IObservablefloat, self.source)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.source.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    

    @property
    def RelStdDev(self):
        from marketsim.gen._out.math._relstddev import RelStdDev
        return RelStdDev(self)
    
    @property
    def Var(self):
        from marketsim.gen._out.math._var import Var
        return Var(self)
    
    @property
    def Avg(self):
        from marketsim.gen._out.math._avg import Avg
        return Avg(self)
    
    @property
    def Source(self):
        from marketsim.gen._out.math._source import Source
        return Source(self)
    
    def MinEpsilon(self, epsilon = None):
        from marketsim.gen._out.math._minepsilon import MinEpsilon
        return MinEpsilon(self,epsilon)
    
    def MaxEpsilon(self, epsilon = None):
        from marketsim.gen._out.math._maxepsilon import MaxEpsilon
        return MaxEpsilon(self,epsilon)
    
    @property
    def StdDev(self):
        from marketsim.gen._out.math._stddev import StdDev
        return StdDev(self)
    
    pass
Cumulative = Cumulative_IObservableFloat
