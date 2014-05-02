# generated with class generator.python.constructor$Import
from marketsim import registry
from marketsim.gen._out.strategy.side._signalstrategy import SignalStrategy
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["-", "Signal"])
class Signal_FloatFloat(SignalStrategy):
    """ 
    """ 
    def __init__(self, source = None, threshold = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        self.source = source if source is not None else deref_opt(_constant_Float(0.0))
        self.threshold = threshold if threshold is not None else 0.7
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IFunctionfloat,
        'threshold' : float
    }
    
    
    
    
    def __repr__(self):
        return "Signal(%(source)s, %(threshold)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
        rtti.typecheck(IFunctionfloat, self.source)
        rtti.typecheck(float, self.threshold)
    
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
    def Threshold(self):
        from marketsim.gen._out.strategy.side._threshold import Threshold
        return Threshold(self)
    
    @property
    def Side(self):
        from marketsim.gen._out.strategy.side._side import Side
        return Side(self)
    
    def Strategy(self, eventGen = None,orderFactory = None):
        from marketsim.gen._out.strategy.side._strategy import Strategy
        return Strategy(self,eventGen,orderFactory)
    
    @property
    def Source(self):
        from marketsim.gen._out.strategy.side._source import Source
        return Source(self)
    
    @property
    def Signal_Value(self):
        from marketsim.gen._out.strategy.side._signal_value import Signal_Value
        return Signal_Value(self)
    
    pass
Signal = Signal_FloatFloat
