# generated with class generator.python.constructor$Import
from marketsim import registry
@registry.expose(["-", "MarketMaker"])
class MarketMaker_FloatFloat(object):
    """ 
    """ 
    def __init__(self, delta = None, volume = None):
        self.delta = delta if delta is not None else 1.0
        self.volume = volume if volume is not None else 20.0
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'delta' : float,
        'volume' : float
    }
    
    
    
    
    def __repr__(self):
        return "MarketMaker(%(delta)s, %(volume)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        rtti.typecheck(float, self.delta)
        rtti.typecheck(float, self.volume)
    
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
    

    def OneSide(self, side = None,sign = None):
        from marketsim.gen._out.strategy.price._oneside import OneSide
        return OneSide(self,side,sign)
    
    @property
    def Delta(self):
        from marketsim.gen._out.strategy.price._delta import Delta
        return Delta(self)
    
    @property
    def TwoSides(self):
        from marketsim.gen._out.strategy.price._twosides import TwoSides
        return TwoSides(self)
    
    @property
    def Volume(self):
        from marketsim.gen._out.strategy.price._volume import Volume
        return Volume(self)
    
    pass
MarketMaker = MarketMaker_FloatFloat
