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
        from marketsim import rtti
        self.source = source if source is not None else deref_opt(_constant_Float(0.0))
        self.threshold = threshold if threshold is not None else 0.7
        rtti.check_fields(self)
    
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
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        self.source.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    

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
